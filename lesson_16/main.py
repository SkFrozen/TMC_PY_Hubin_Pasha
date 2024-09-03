from models.base import Base, engine
from models.categories import Category
from models.goods import Good
from models.orders import Order
from models.providers import Provider

metadata = Base.metadata

if __name__ == "__main__":
    metadata.create_all(engine)
