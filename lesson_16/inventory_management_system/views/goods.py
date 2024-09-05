from models.categories import Category
from models.goods import Good
from models.providers import Provider


def add_good(session):

    name = input("Enter a good name: ")
    cost = input("Enter a good cost: ")
    provider = input("Enter a provider company name: ")
    category = input("Enter a category: ")
    provider_num = session.query(Provider).filter_by(company_name=provider).first()
    category_num = session.query(Category).filter_by(name=category).first()
    session.add(
        Good(
            name=name,
            cost=cost,
            provider=provider_num,
            category=category_num,
        )
    )


def delete_good(session):
    number = int(input("Enter the good number: "))
    session.query(Good).filter_by(number=number).delete(synchronize_session="fetch")


def update_good(session):
    good_name = input("Enter a name of good for update: ")
    prop_update = input("What to change: 'name','cost', 'provider' or 'category'? ")
    new_val = input("Enter a new value: ")
    if prop_update == "provider":
        prop_update = "provider_num"
    elif prop_update == "category":
        prop_update = "category_num"

    session.query(Good).filter(Good.name == good_name).update({prop_update: new_val})


def get_info_good(session):
    name = input("Enter a good name: ")
    good = session.query(Good).filter(Good.name == name).first()
    if good:
        print(good)
    else:
        print(f"The {name} was not found")


def search_good(session):
    name = input("Enter part of the name: ")
    goods = session.query(Good).filter(Good.name.ilike(f"{name}%")).all()
    for good in goods:
        print(good)
        print("-" * 20)
