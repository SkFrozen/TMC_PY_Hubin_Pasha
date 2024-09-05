from models.base import Base, engine
from models.categories import Category
from models.goods import Good
from models.orders import Order
from models.providers import Provider
from sqlalchemy.orm import sessionmaker
from views.categories import (
    add_category,
    delete_category,
    get_info_category,
    search_category,
)
from views.goods import add_good, delete_good, get_info_good, search_good, update_good
from views.orders import (
    add_order,
    delete_order,
    get_info_order,
    search_order,
    update_order,
)
from views.providers import (
    add_provider,
    delete_provider,
    get_info_provider,
    search_provider,
    update_provider,
)
from views.warehouse import get_info_warehouse, search_goods_by_category

metadata = Base.metadata

session_pool = sessionmaker(bind=engine)

with session_pool() as session:
    try:
        # add_category(session)
        # add_provider(session)
        # add_good(session)
        # get_info_category(session)
        search_good(session)
        session.commit()
    except Exception as e:
        session.rollback()
        raise ValueError("Query has been canceled, enter the correct info")
# if __name__ == "__main__":
#     metadata.create_all(engine)
