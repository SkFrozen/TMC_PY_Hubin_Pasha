from models.categories import Category
from models.goods import Good
from models.providers import Provider


def add_good(session, name: str, cost: float, provider: str, category: str):

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


def delete_good(session, id):
    session.query(Good).filter_by(id=id).delete()


def update_good(session, name, cost, provider, category):

    session.query(Good).filter(Good.name == good_name).update({prop_update: new_val})


def get_info_good(session, id):
    good = session.query(Good).filter(Good.id == id).first()
    return good


def search_good(session):
    name = input("Enter part of the name: ")
    goods = session.query(Good).filter(Good.name.ilike(f"{name}%")).all()
    for good in goods:
        print(good)
        print("-" * 20)
