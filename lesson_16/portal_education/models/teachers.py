from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Teacher(Base):
    __tablename__ = "teacher"

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    email = Column(String)
    classroom = Column(Integer)
    course_id = Column(String, ForeignKey("course.title"))
    course = relationship("Course")
