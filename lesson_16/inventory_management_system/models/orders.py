from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Order(Base):
    __tablename__ = "order"

    number = Column(Integer, primary_key=True)
    full_name = Column(String)
    address = Column(String)
    notes = Column(String)
    email = Column(String)
    provider_num = Column(Integer, ForeignKey("provider.number"))
    good_num = Column(Integer, ForeignKey("good.number"))
    provider = relationship("Provider")
    good = relationship("Good")
