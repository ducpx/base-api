from .base import BaseModel
from sqlalchemy import Column, String


class User(BaseModel):
    __tablename__ = 'test'
    name = Column(String)
