from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(String, primary_key=True)

