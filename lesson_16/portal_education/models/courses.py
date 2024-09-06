from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Course(Base):
    __tablename__ = "course"

    title = Column(String, primary_key=True)
    specialty_id = Column(String, ForeignKey("specialty.title"))
    specialty = relationship("Specialty")
    student = relationship(
        "Student", secondary="course_student", back_populates="course"
    )


class CourseStudent(Base):
    __tablename__ = "course_student"

    id = Column(Integer, primary_key=True)
    student = Column(Integer, ForeignKey("student.id"))
    course = Column(String, ForeignKey("course.title"))
