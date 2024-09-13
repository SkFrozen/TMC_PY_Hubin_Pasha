from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Good(Base):
    __tablename__ = "good"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cost = Column(Float, nullable=False)
    provider_num = Column(Integer, ForeignKey("provider.id"), nullable=False)
    category_num = Column(Integer, ForeignKey("category.id"), nullable=False)
    category = relationship("Category")
    provider = relationship("Provider")
