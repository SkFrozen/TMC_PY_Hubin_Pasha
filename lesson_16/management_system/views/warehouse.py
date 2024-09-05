from functools import reduce

from models.categories import Category
from models.goods import Good
from models.orders import Order
from models.providers import Provider
from sqlalchemy import func


def get_info_warehouse(session):
    count_goods = session.query(Good).count()
    count_order = session.query(Order).count()
    count_provider = session.query(Provider).count()
    total_sum_goods = session.query(func.sum(Good.cost)).first()
    orders = (
        session.query(Order, Good.cost).join(Good, Order.good_num == Good.number).all()
    )
    total_sum_orders = reduce(lambda x, obj: x + obj[1], orders, 0)
    print(f"Total goods: {count_goods}")
    print(f"Total orders: {count_order}")
    print(f"Total providers: {count_provider}")
    print(f"Total cost of goods: {total_sum_goods[0]}")
    print(f"Total cost of orders: {total_sum_orders}")


def search_goods_by_category(session):
    category_name = input("Enter a category: ")
    category = session.query(Category).filter_by(name=category_name).first()
    goods = session.query(Good).filter_by(category_num=category.number).all()
    print(goods)
