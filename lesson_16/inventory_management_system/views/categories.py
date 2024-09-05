from models.categories import Category


def add_category(session):
    category = input("Enter a category of good: ")
    session.add(Category(name=category))


def delete_category(session):
    number = int(input("Enter the category number: "))
    session.query(Category).filter_by(number=number).delete()


def get_info_category(session):
    name = input("Enter a nam category: ")
    category = session.query(Category).filter(Category.name == name).first()

    if category:
        print(
            f"number:{category.number} \
            \nname: {category.name}"
        )
    else:
        print(f"The {name} was not found")


def search_category(session):
    name = input("Enter part of the name: ")
    categorys = session.query(Category).filter(Category.name.ilike(f"{name}%")).all()
    for category in categorys:
        print(
            f"number:{category.number} \
            \nname: {category.name}"
        )
