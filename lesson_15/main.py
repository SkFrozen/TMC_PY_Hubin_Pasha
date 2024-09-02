from create_db import Author, Book, Sale
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///db.sqlite", echo=True)
session_pool = sessionmaker(bind=engine)


with session_pool() as session:
    # authors = [
    #     Author(first_name="Ivan", last_name="Turgenev"),
    #     Author(first_name="Leo", last_name="Tolstoy"),
    #     Author(first_name="Friedrich", last_name="Engels"),
    #     Author(first_name="Stephen", last_name="King"),
    # ]
    # session.add_all(authors)
    # turgenev = session.query(Author).filter_by(last_name="Turgenev").first()
    # tolstoy = session.query(Author).filter_by(last_name="Tolstoy").first()
    # engels = session.query(Author).filter_by(last_name="Engels").first()

    # books = [
    #     Book(title="Mumu", author=turgenev),
    #     Book(title="Fathers and sons", author=turgenev),
    #     Book(title="War and peace", author=tolstoy),
    #     Book(title="Anna Karenina", author=tolstoy),
    #     Book(title="Childhood", author=tolstoy),
    #     Book(title="Anti-Duhring", author=engels),
    #     Book(title="The communist manifesto", author=engels),
    #     Book(title="English Dictionary"),
    #     Book(title="French Dictionary"),
    # ]

    # session.add_all(books)

    # mumu = session.query(Book).filter_by(title="Mumu").first()
    # war_and_peace = session.query(Book).filter_by(title="War and peace").first()
    # anti_duhring = session.query(Book).filter_by(title="Anti-Duhring").first()
    # anna_karenina = session.query(Book).filter_by(title="Anna Karenina").first()

    # sales = [
    #     Sale(quantity=100, book=mumu),
    #     Sale(quantity=250, book=war_and_peace),
    #     Sale(quantity=75, book=anti_duhring),
    #     Sale(quantity=125, book=anna_karenina),
    # ]
    # session.add_all(sales)

    # inner_join = (
    #     session.query(Book, Author).join(Book, Author.id == Book.author_id).all()
    # )
    # left_join = (
    #     session.query(Author, Book)
    #     .join(Book, Author.id == Book.author_id, isouter=True)
    #     .all()
    # )
    # right_join = (
    #     session.query(Book, Author)
    #     .join(Author, Author.id == Book.author_id, isouter=True)
    #     .all()
    # )

    # print("INNER JOIN")
    # for book in inner_join:
    #     print(book)

    # print("LEFT JOIN")
    # for author in left_join:
    #     print(author)

    # print("RIGHT JOIN")
    # for book in right_join:
    #     print(book)

    # multi_join = (
    #     session.query(Book, Author, Sale)
    #     .join(Author, Author.id == Book.author_id)
    #     .join(Sale, Book.id == Sale.book_id)
    # )

    # print("MULTI_JOIN")
    # for join in multi_join:
    #     print(join)

    # left_multi_join = (
    #     session.query(Author, Book, Sale)
    #     .join(Book, Author.id == Book.author_id, isouter=True)
    #     .join(Sale, Book.id == Sale.book_id, isouter=True)
    # )

    # print("LEFT_MULTI_JOIN")
    # for join in left_multi_join:
    #     print(join)

    session.commit()
