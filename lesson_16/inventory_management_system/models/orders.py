from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    notes = Column(String, nullable=True)
    email = Column(String, nullable=False)
    provider_email = Column(String, default="IMS-seller@gmail.com")
    status = Column(String, nullable=False)
    good_num = Column(Integer, ForeignKey("good.id"), nullable=False)
    good = relationship("Good")
