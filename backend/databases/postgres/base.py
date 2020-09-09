import uuid
from datetime import datetime

from sqlalchemy.ext.compiler import compiles
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, String, DateTime, Boolean, Integer, event
from sqlalchemy.sql import expression

from backend.common.constants import DATE_FORMAT, STRING_LENGTH

Base = declarative_base()


class UtcNow(expression.FunctionElement):
    type = DateTime()


@compiles(UtcNow, 'postgresql')
def get_now(element, compiler, **kw):
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"


def model_oncreate_listener(mapper, connection, instance):
    instance.created_at = UtcNow()
    instance.updated_at = UtcNow()


def model_onupdate_listener(mapper, connection, instance):
    instance.created_at = instance.created_at
    instance.updated_at = UtcNow()
    if instance.deleted is True:
        instance.deleted_at = UtcNow()


class Serializer(object):

    def parse_value(self, value):
        if value is None:
            return None
        if isinstance(value, datetime):
            return value.strftime(DATE_FORMAT)
        return value


class BaseModel(Base, Serializer):
    __abstract__ = True

    @declared_attr
    def __tablename__(self):
        return ''.join('_%s' % c if c.isupper() else c
                       for c in self.__name__).strip('_').lower()

    id = Column(String(STRING_LENGTH['UUID4']), primary_key=True, default=lambda: str(uuid.uuid4()))

    created_at = Column(DateTime, server_default=UtcNow())
    updated_at = Column(DateTime, server_default=UtcNow())

    deleted = Column(Boolean, default=False)
    deleted_at = Column(DateTime,)

    @classmethod
    def convert_from_dict(cls, data, origin=None):
        if origin:
            if not isinstance(origin, cls):
                raise Exception('Invalid origin object of %s.' % cls.__name__)
            result = origin
        else:
            result = cls()
        all_fields = cls.__table__.columns
        for field_name in all_fields.keys():
            value = data.get(field_name)
            if value is None:
                continue
            if value == getattr(result, field_name, None):
                continue
            setattr(result, field_name, value)
        return result


class Person(object):
    name = Column(String(STRING_LENGTH['LONG']), index=True)
    email = Column(String(STRING_LENGTH['LONG']), index=True)
    address = Column(String(STRING_LENGTH['LONG']))
    gender = Column(String(STRING_LENGTH['EX_SHORT']), index=True)
    phone = Column(String(STRING_LENGTH['EX_SHORT']), index=True)


event.listen(BaseModel, 'before_insert', model_oncreate_listener, propagate=True)
event.listen(BaseModel, 'before_update', model_onupdate_listener, propagate=True)
