from .base import BaseModel, Person
from sqlalchemy import Column, String

from ...common.constants import STRING_LENGTH


class User(BaseModel, Person):
    status = Column(String(STRING_LENGTH['EX_SHORT']),
                    default='active', index=True)

    avatar_url = Column(String(STRING_LENGTH['LARGE']))

    # for migration
    old_id = Column(String(STRING_LENGTH['LONG']))
