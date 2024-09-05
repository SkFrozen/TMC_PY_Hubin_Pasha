from models.goods import Good
from models.orders import Order
from models.providers import Provider


def add_order(session):
    good_name = input("Enter a name of good: ")
    full_name = input("Enter your full name: ")
    address = input("Enter your adress:")
    notes = input("Enter a notes: ")
    email = input("Enter your email: ")

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


def update_order(session):
    number = int(input("Enter the order number: "))
    prop_update = input(
        "What to change: 'full_name', "
        + "'address', 'notes','email', "
        + "'provider_num', 'good_num': "
    )
    new_val = input("Enter a new value: ")
    order = (
        session.query(Order)
        .filter(Order.number == number)
        .update({prop_update: new_val})
    )


def get_info_order(session):
    name = input("Enter a full name: ")
    order = session.query(Order).filter_by(full_name=name).first()
    provider = session.query(Provider).get(order.provider_num)
    good = session.query(Good).get(order.good_num)
    if order:
        print(
            f"number: {order.number}\
            \nfull_name: {order.full_name}\
            \naddress: {order.address}\
            \nnotes: {order.notes}\
            \nemail: {order.email}\
            \nprovider: {provider.company_name}\
            \ngood: {good.name}"
        )
    else:
        print("The order was not found")


def delete_order(session):
    number = int(input("Enter the order number: "))
    session.query(Order).filter_by(number=number).delete()


def search_order(session):
    name = input("Enter part of the name: ")
    orders = session.query(Order).filter(Order.full_name.ilike(f"{name}%")).all()
    provider = session.query(Provider).get(order.provider_num)
    good = session.query(Good).get(order.good_num)
    for order in orders:
        print(
            f"number: {order.number}\
        \nfull_name: {order.full_name}\
        \naddress: {order.address}\
        \nnotes: {order.notes}\
        \nemail: {order.email}\
        \nprovider: {provider.company_name}\
        \ngood: {good.name}"
        )
