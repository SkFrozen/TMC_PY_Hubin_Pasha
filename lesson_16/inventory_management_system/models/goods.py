import re

from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base
from .categories import Category
from .providers import Provider


class Good(Base):
    __tablename__ = "good"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cost = Column(Float, nullable=False)
    provider_num = Column(Integer, ForeignKey("provider.id"), nullable=False)
    category_num = Column(Integer, ForeignKey("category.id"), nullable=False)
    category = relationship("Category")
    provider = relationship("Provider")

    @classmethod
    def add(cls, name: str, cost: float, provider: str, category: str, session: object):
        """Method recieves data about good, requests provider, category
        and adds good to DB
        """
        cls.__validate_data(name, cost, provider, category)

        session.add(
            Good(name=name, cost=cost, provider_num=provider, category_num=category)
        )

    @classmethod
    def get_info(cls, id: int, session: object) -> dict:
        """Method recieves id of the good, requests good, provider, category.
        Creates dictionary of the good and returns it.
        """

        good = (
            session.query(Good)
            .filter(Good.id == id)
            .join(Category, Category.id == Good.category_num)
            .join(Provider, Provider.id == Good.provider_num)
            .first()
        )
        json_data = {
            "id": good.id,
            "name": good.name,
            "cost": good.cost,
            "provider": good.provider.company_name,
            "category": good.category.name,
            "provider_id": good.provider.id,
            "category_id": good.category.id,
        }

        return json_data

    @classmethod
    def get_good_by_id(cls, id: int, session: object) -> object:
        """Method recieves object id, requests object and returns it"""
        good = session.query(Good).filter_by(id=id).first()
        return good

    @staticmethod
    def __validate_data(name, cost, provider, category):
        if name == "" or cost == "" or provider == "" or category == "":
            raise ValueError("Error: an empty field is prohibited")
        elif re.search(r"[^\w ]", name):
            raise ValueError("Name must be from a to z, 0 to 9 or with an underscore")
        elif re.search(r"[^\d\.]", cost):
            raise ValueError("Cost must be from 0 to 9 and separated by the '.'")

    def update(
        self, name: str, cost: float, provider: str, category: str, session: object
    ):
        """Method recieves new data about good, requests provider, category.
        Updates good record
        """
        self.__validate_data(name, cost, provider, category)
        session.query(Good).filter_by(id=self.id).update(
            {
                "name": name,
                "cost": cost,
                "provider_num": provider,
                "category_num": category,
            }
        )

    def delete(self, session: object):
        session.query(Good).filter_by(id=self.id).delete()
