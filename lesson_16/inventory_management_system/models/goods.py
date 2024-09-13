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
    def create(
        cls, name: str, cost: float, provider: str, category: str, session: object
    ):
        """Method recieves data about good, finds provider_id, category_id.
        It connects to DB, creates and records godd
        """

        provider_id = session.query(Provider).filter_by(company_name=provider).first()
        category_id = session.query(Category).filter_by(name=category).first()

        session.add(
            Good(name=name, cost=cost, provider=provider_id, category=category_id)
        )

    @classmethod
    def get_info(cls, id: int, session: object) -> dict:
        """Method recieves id of the good, connects to the DB
        requests good, provider, category. Returns dict with data about good
        """

        good = session.query(Good).filter(Good.id == id).first()
        provider = (
            session.query(Provider).filter(Provider.id == good.provider_num).first()
        )
        category = (
            session.query(Category).filter(Category.id == good.category_num).first()
        )
        json_good = {
            "id": good.id,
            "name": good.name,
            "cost": good.cost,
            "provider": provider.company_name,
            "category": category.name,
        }

        return json_good

    @classmethod
    def get_good_by_id(cls, id: int, session: object) -> object:
        """Method recieves object id, requestes object and returns it"""
        good = session.query(Good).filter_by(id=id).first()
        return good

    def update(
        self, name: str, cost: float, provider: str, category: str, session: object
    ):
        """Method recieves data about good, finds provider_id, category_id."""

        provider = session.query(Provider).filter_by(company_name=provider).first()
        category = session.query(Category).filter_by(name=category).first()
        session.query(Good).filter_by(id=self.id).update(
            {
                "name": name,
                "cost": cost,
                "provider_num": provider.id,
                "category_num": category.id,
            }
        )

    def delete(self, id: int, session: object):
        session.query(Good).filter_by(id=id).delete()
