from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .base import Base


class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True)
    grade = Column(Integer)
    student = relationship("Student", secondary="student_grade", back_populates="grade")


class StudentGrade(Base):
    __tablename__ = "student_grade"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    grade = Column(Integer, ForeignKey("grades.id"))
