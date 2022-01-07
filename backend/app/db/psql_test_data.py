from datetime import datetime

from app.db.crud import get_attendance_by_id
from app.db.crud import get_course_by_id
from app.db.crud import get_course_lessons_by_id
from app.db.crud import get_lecturer_by_id
from app.db.crud import get_lecturer_studentclass_by_id
from app.db.crud import get_lesson_by_id
from app.db.crud import get_student_by_id
from app.db.crud import get_studentclass_by_id
from app.db.crud import get_studentclass_course_by_id
from app.db.psql import engine
from app.db.psql_models import Attendance
from app.db.psql_models import Course
from app.db.psql_models import CourseLessonLink
from app.db.psql_models import Lecturer
from app.db.psql_models import LecturerClassLink
from app.db.psql_models import Lesson
from app.db.psql_models import SQLModel
from app.db.psql_models import Student
from app.db.psql_models import StudentClass
from app.db.psql_models import StudentClassCourseLink
from sqlmodel import Session


test_studentclasses = [
    StudentClass(
        name="Student Class 1",
        number_of_students=2,
    ),
    StudentClass(
        name="Student Class 2",
        number_of_students=2,
    ),
]

test_students = [
    Student(
        name="John",
        class_id=1,
    ),
    Student(
        name="Jane",
        class_id=1,
    ),
    Student(
        name="Bob",
        class_id=2,
    ),
    Student(
        name="Alice",
        class_id=2,
    ),
]

test_courses = [
    Course(
        name="Math",
        category="Category 1",
    ),
    Course(
        name="English",
        category="Category 2",
    ),
    Course(
        name="Psysics",
        category="Category 3",
    ),
]


test_lecturers = [
    Lecturer(name="Hans"),
    Lecturer(name="Peter"),
    Lecturer(name="Emil"),
]

test_lessons = [
    Lesson(
        name="Lesson 1",
        start=datetime(2020, 10, 10, 8, 30),
        duration=240,
        attendance_token="a111",
    ),
    Lesson(
        name="Lesson 2",
        start=datetime(2020, 10, 11, 8, 30),
        duration=240,
        attendance_token="b222",
    ),
    Lesson(
        name="Lesson 3",
        start=datetime(2020, 10, 12, 8, 30),
        duration=240,
        attendance_token="c333",
    ),
    Lesson(
        name="Lesson 4",
        start=datetime(2020, 10, 11, 12, 30),
        duration=180,
        attendance_token="d444",
    ),
    Lesson(
        name="Lesson 5",
        start=datetime(2020, 10, 12, 12, 30),
        duration=180,
        attendance_token="e555",
    ),
]

test_attendances = [
    Attendance(
        time_of_attendance=datetime(2020, 10, 10, 8, 30),
        lesson_id=1,
        student_id=1,
    ),
    Attendance(
        time_of_attendance=datetime(2020, 10, 10, 8, 30),
        lesson_id=2,
        student_id=2,
    ),
    Attendance(
        time_of_attendance=datetime(2020, 10, 10, 9, 30),
        lesson_id=3,
        student_id=3,
    ),
    Attendance(
        time_of_attendance=datetime(2020, 10, 10, 12, 30),
        lesson_id=4,
        student_id=4,
    ),
    Attendance(
        time_of_attendance=datetime(2020, 10, 10, 13, 30),
        lesson_id=5,
        student_id=1,
    ),
]

test_lecturer_class_links = [
    LecturerClassLink(
        lecturer_id=1,
        class_id=1,
    ),
    LecturerClassLink(
        lecturer_id=2,
        class_id=1,
    ),
    LecturerClassLink(
        lecturer_id=3,
        class_id=2,
    ),
]

test_studentclass_course_links = [
    StudentClassCourseLink(
        class_id=1,
        course_id=1,
    ),
    StudentClassCourseLink(
        class_id=1,
        course_id=2,
    ),
    StudentClassCourseLink(
        class_id=2,
        course_id=3,
    ),
]


test_course_lesson_links = [
    CourseLessonLink(
        course_id=1,
        lesson_id=1,
    ),
    CourseLessonLink(
        course_id=2,
        lesson_id=2,
    ),
    CourseLessonLink(
        course_id=3,
        lesson_id=3,
    ),
]


def setup_psql_test_data() -> bool:
    try:
        SQLModel.metadata.create_all(engine)

        with Session(engine) as session:
            if not get_studentclass_by_id(session, 1):
                session.add_all(test_studentclasses)

            if not get_student_by_id(session, 1):
                session.add_all(test_students)

            if not get_course_by_id(session, 1):
                session.add_all(test_courses)

            if not get_lecturer_by_id(session, 1):
                session.add_all(test_lecturers)

            if not get_lesson_by_id(session, 1):
                session.add_all(test_lessons)

            session.commit()
    except Exception as e:
        print(e)
        return False

    return True


def setup_psql_test_attendances() -> bool:
    try:
        with Session(engine) as session:
            if not get_attendance_by_id(session, 1):
                session.add_all(test_attendances)

            session.commit()
    except Exception as e:
        print(e)
        return False

    return True


def setup_psql_test_links() -> bool:
    try:
        with Session(engine) as session:
            if not get_lecturer_studentclass_by_id(db=session, lecturer_id=1):
                session.add_all(test_lecturer_class_links)

            if not get_studentclass_course_by_id(db=session, studentclass_id=1):
                session.add_all(test_studentclass_course_links)

            if not get_course_lessons_by_id(db=session, course_id=1):
                session.add_all(test_course_lesson_links)

            session.commit()
    except Exception as e:
        print(e)
        return False

    return True


def teardown_psql() -> bool:
    try:
        # TODO: Breaks setup_psql_test_data() when run - fix
        SQLModel.metadata.drop_all(engine)
    except Exception as e:
        print(e)
        return False

    return True
