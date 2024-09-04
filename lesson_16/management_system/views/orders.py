from models.goods import Good
from models.orders import Order
from models.providers import Provider


def add_order(session):
    good_name = input("Enter a name of good: ")
    full_name = input("Enter a full name: ")
    address = input("Enter an adress:")
    notes = input("Enter a notes: ")
    email = input("Enter an email: ")

    good = session.query(Good).filter(Good.name == good_name).first()
    provider = (
        session.query(Provider).filter(Provider.number == good.provider_num).first()
    )
    session.add(
        Order(
            full_name=full_name,
            address=address,
            notes=notes,
            email=email,
            provider=provider,
            good=good,
        )
    )
