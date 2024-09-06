from models.base import Base, engine
from models.courses import Course, CourseStudent
from models.grades import Grade, StudentGrade
from models.specialties import Specialty
from models.students import Student
from models.teachers import Teacher
from sqlalchemy.orm import sessionmaker

session_pool = sessionmaker(bind=engine)
metadata = Base.metadata


with session_pool() as session:
    pass

if __name__ == "__main__":
    metadata.create_all(engine)
