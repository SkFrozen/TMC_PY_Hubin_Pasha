from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Good(Base):
    __tablename__ = "good"

    number = Column(Integer, primary_key=True)
    name = Column(String)
    cost = Column(Float)
    count = Column(Integer)
    provider_num = Column(Integer, ForeignKey("provider.number"))
    category_num = Column(Integer, ForeignKey("category.number"))
    category = relationship("Category")
    provider = relationship("Provider", back_populates="goods")
