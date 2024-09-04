from models.categories import Category


def add_category(session):
    category = input("Enter a category of good: ")
    session.add(Category(name=category))


def delete_category(session):
    name = input("Enter a category name to delete: ")
    session.query(Category).filter_by(name=name).delete(synchronize_session="fetch")
