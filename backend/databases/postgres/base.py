from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, String

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return ''.join('_%s' % c if c.isupper() else c
                       for c in cls.__name__).strip('_').lower()
    id = Column(String, primary_key=True)

