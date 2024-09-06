from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    email = Column(String)
    student_card = Column(Integer)
    specialty_id = Column(String, ForeignKey("specialty.title"))
    specialty = relationship("Specialty")
    grade = relationship("Grade", secondary="student_grade", back_populates="student")
    course = relationship(
        "Course", secondary="course_student", back_populates="student"
    )
