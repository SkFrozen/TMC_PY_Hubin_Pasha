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

    @classmethod
    def add(
        cls,
        first_name: str,
        last_name: str,
        email: str,
        company_name: str,
        session: object,
    ):
        """Method recieves data about provider.
        Requests to DB to add provider
        """
        if first_name == "" or last_name == "" or email == "" or company_name == "":
            raise ValueError("Error: an empty field is prohibited")

        session.add(
            Provider(
                first_name=first_name,
                last_name=last_name,
                email=email,
                company_name=company_name,
            )
        )

    @classmethod
    def get_provider_by_id(cls, id: int, session: object) -> object:
        """Method recieves object id, requests object and returns it"""
        provider = session.query(Provider).filter_by(id=id).first()
        return provider

    @classmethod
    def get_info(cls, id: int, session: object) -> object:
        """Method recieves provider id, requests it.
        Creates dictionary of provider data returns it.
        """
        provider = session.query(Provider).filter_by(id=id).first()
        json_porvider = {
            "id": provider.id,
            "first_name": provider.first_name,
            "last_name": provider.last_name,
            "email": provider.email,
            "company_name": provider.company_name,
        }

        return json_porvider

    def update(
        self,
        first_name: str,
        last_name: str,
        email: str,
        company_name: str,
        session: object,
    ):
        """Method recieves new data about provider and requests update it"""
        if first_name == "" or last_name == "" or email == "" or company_name == "":
            raise ValueError("Error: an empty field is prohibited")
        session.query(Provider).filter_by(id=self.id).update(
            {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "company_name": company_name,
            }
        )

    def delete(self, session: object):
        session.query(Provider).filter_by(id=self.id).delete()
