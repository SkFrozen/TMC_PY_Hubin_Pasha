from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine("sqlite:///db.sqlite", echo=True)
Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    books = relationship("Book", back_populates="author")

    def __repr__(self):
        return f"Author: {self.first_name} {self.last_name}"


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")
    sales = relationship("Sale", back_populates="book")

    def __repr__(self):
        return f"Book: {self.title}"


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    book_id = Column(Integer, ForeignKey("books.id"))
    book = relationship("Book", back_populates="sales")

    def __repr__(self):
        return f"Sales quantity: {self.quantity}"


metadata = Base.metadata

if __name__ == "__main__":
    metadata.create_all(engine)
