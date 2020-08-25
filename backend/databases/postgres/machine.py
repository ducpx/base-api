from .base import BaseModel
from sqlalchemy import Column, String


class Machine(BaseModel):
    name = Column(String)
