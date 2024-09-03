from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Provider(Base):
    __tablename__ = "provider"

    number = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    company_name = Column(String)
    good_num = Column(Integer, ForeignKey("good.number"))
    goods = relationship("Good", back_populates="provider")
