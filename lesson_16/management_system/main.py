from models.base import Base, engine
from models.categories import Category
from models.goods import Good
from models.orders import Order
from models.providers import Provider
from sqlalchemy.orm import sessionmaker
from views.categories import add_category, delete_category
from views.goods import add_good, delete_good, get_info_good, update_good
from views.orders import add_order
from views.providers import add_provider, delete_provider, update_provider

metadata = Base.metadata

session_pool = sessionmaker(bind=engine)

with session_pool() as session:
    try:
        # add_category(session)
        # add_provider(session)
        # add_good(session)
        get_info_good(session)
        session.commit()
    except Exception as e:
        session.rollback()
        raise ValueError("Query has been canceled")
# if __name__ == "__main__":
#     metadata.create_all(engine)
