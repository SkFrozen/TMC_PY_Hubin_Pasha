import re

from sqlalchemy import Column, Integer, String

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
        """Method recieves provider data, session object.
        Adds provider to DB
        """
        cls.__validate_data(first_name, last_name, email, company_name)

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
        Creates dictionary of the provider data and returns it.
        """
        provider = session.query(Provider).filter_by(id=id).first()
        json_data = {
            "id": provider.id,
            "first_name": provider.first_name,
            "last_name": provider.last_name,
            "email": provider.email,
            "company_name": provider.company_name,
        }

        return json_data

    @staticmethod
    def __validate_data(first_name, last_name, email, company_name):
        if first_name == "" or last_name == "" or email == "" or company_name == "":
            raise ValueError("Error: an empty field is prohibited")
        elif re.search(r"[^\w ]", first_name) and re.search(r"[^\w ]", last_name):
            raise ValueError("Name must be from a to z, 0 to 9 or with an underscore")
        elif not re.match(r"^[-\w\.]+@[-\w\.]+\.[-\w]+$", email):
            raise ValueError("Email must contain 'a-z', 'A-Z', '0-9','@', '_.'")

    def update(
        self,
        first_name: str,
        last_name: str,
        email: str,
        company_name: str,
        session: object,
    ):
        """Method recieves new provider data and updates provider record"""
        self.__validate_data(first_name, last_name, email, company_name)
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
