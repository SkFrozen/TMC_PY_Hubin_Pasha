from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Provider(Base):
    __tablename__ = "provider"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
