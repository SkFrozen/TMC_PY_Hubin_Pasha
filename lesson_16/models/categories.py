from sqlalchemy import Column, Integer, String

from .base import Base


class Category(Base):
    __tablename__ = "category"

    number = Column(Integer, primary_key=True)
    name = Column(String)
