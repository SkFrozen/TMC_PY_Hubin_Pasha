from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Good(Base):
    __tablename__ = "good"

    number = Column(Integer, primary_key=True)
    name = Column(String)
    cost = Column(Float)
    provider_num = Column(Integer, ForeignKey("provider.number"), nullable=False)
    category_num = Column(Integer, ForeignKey("category.number"), nullable=False)
    category = relationship("Category")
    provider = relationship("Provider")

    def __repr__(self):
        return f"name: {self.name} \
        \ncost: {self.cost} \
        \nprovider: {self.provider.company_name} \
        \ncategory: {self.category.name}"
