from sqlalchemy import Column, Integer, String

from .base import Base


class Specialty(Base):
    __tablename__ = "specialty"

    title = Column(String, primary_key=True)
