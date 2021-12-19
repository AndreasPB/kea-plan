from datetime import datetime

from app.db.crud import get_attendance_by_id
from app.db.crud import get_attendances
from app.db.crud import get_course_by_id
from app.db.crud import get_course_lessons
from app.db.crud import get_course_lessons_by_id
from app.db.crud import get_courses
from app.db.crud import get_lecturer_by_id
from app.db.crud import get_lecturer_classes
from app.db.crud import get_lecturer_studentclass_by_id
from app.db.crud import get_lecturers
from app.db.crud import get_lesson_by_id
from app.db.crud import get_lessons
from app.db.crud import get_student_attendances
from app.db.crud import get_student_attendances_by_id
from app.db.crud import get_student_by_id
from app.db.crud import get_studentclass_by_id
from app.db.crud import get_studentclass_course_by_id
from app.db.crud import get_studentclass_courses
from app.db.crud import get_studentclasses
from app.db.crud import get_students
from app.db.psql import engine
from app.db.psql_models import Attendance
from app.db.psql_models import Course
from app.db.psql_models import CourseLessonLink
from app.db.psql_models import Lecturer
from app.db.psql_models import LecturerClassLink
from app.db.psql_models import Lesson
from app.db.psql_models import Student
from app.db.psql_models import StudentAttendanceLink
from app.db.psql_models import StudentClass
from app.db.psql_models import StudentClassCourseLink
from sqlmodel import Session

test_students = [
    Student(
        id=1,
        name="John",
    ),
    Student(
        id=2,
        name="Jane",
    ),
    Student(
        id=3,
        name="Bob",
    ),
    Student(
        id=4,
        name="Alice",
    ),
]

test_studentclasses = [
    StudentClass(
        id=1,
        name="Student Class 1",
        number_of_students=2,
    ),
    StudentClass(
        id=2,
        name="Student Class 2",
        number_of_students=2,
    ),
]

test_courses = [
    Course(
        id=1,
        name="Math",
        category="Category 1",
    ),
    Course(
        id=2,
        name="English",
        category="Category 2",
    ),
    Course(
        id=3,
        name="Psysics",
        category="Category 3",
    ),
]


test_lecturers = [
    Lecturer(id=1, name="Hans"),
    Lecturer(id=2, name="Peter"),
    Lecturer(id=3, name="Emil"),
]

test_lessons = [
    Lesson(
        id=1,
        name="Lesson 1",
        start=datetime(2020, 10, 10, 8, 30),
        duration=240,
        attendance_token="1111",
    ),
    Lesson(
        id=2,
        name="Lesson 2",
        start=datetime(2020, 10, 11, 8, 30),
        duration=240,
        attendance_token="2222",
    ),
    Lesson(
        id=3,
        name="Lesson 3",
        start=datetime(2020, 10, 12, 8, 30),
        duration=240,
        attendance_token="3333",
    ),
    Lesson(
        id=4,
        name="Lesson 4",
        start=datetime(2020, 10, 11, 12, 30),
        duration=180,
        attendance_token="4444",
    ),
    Lesson(
        id=5,
        name="Lesson 5",
        start=datetime(2020, 10, 12, 12, 30),
        duration=180,
        attendance_token="5555",
    ),
]

test_attendances = [
    Attendance(
        id=1,
        time_of_attendance=datetime(2020, 10, 10, 8, 30),
        lesson_id=1,
    ),
    Attendance(
        id=2,
        time_of_attendance=datetime(2020, 10, 10, 8, 30),
        lesson_id=2,
    ),
    Attendance(
        id=3,
        time_of_attendance=datetime(2020, 10, 10, 9, 30),
        lesson_id=3,
    ),
    Attendance(
        id=4,
        time_of_attendance=datetime(2020, 10, 10, 12, 30),
        lesson_id=4,
    ),
    Attendance(
        id=5,
        time_of_attendance=datetime(2020, 10, 10, 13, 30),
        lesson_id=5,
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


test_student_attendance_links = [
    StudentAttendanceLink(
        student_id=1,
        attendance_id=1,
    ),
    StudentAttendanceLink(
        student_id=2,
        attendance_id=1,
    ),
    StudentAttendanceLink(
        student_id=3,
        attendance_id=2,
    ),
    StudentAttendanceLink(
        student_id=4,
        attendance_id=2,
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
        with Session(engine) as session:
            if not get_student_by_id(session, 1):
                session.add_all(test_students)

            if not get_studentclass_by_id(session, 1):
                session.add_all(test_studentclasses)

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

            if not get_student_attendances_by_id(db=session, student_id=1):
                session.add_all(test_student_attendance_links)

            if not get_course_lessons_by_id(db=session, course_id=1):
                session.add_all(test_course_lesson_links)

            session.commit()
    except Exception as e:
        print(e)
        return False

    return True


def teardown_psql() -> bool:
    try:
        with Session(engine) as session:
            lecturer_class_links = get_lecturer_classes(session)
            studentclass_course_links = get_studentclass_courses(session)
            student_attendance_links = get_student_attendances(session)
            course_lesson_links = get_course_lessons(session)

            for lecturer_class in lecturer_class_links:
                session.delete(lecturer_class)

            for studentclass_course in studentclass_course_links:
                session.delete(studentclass_course)

            for student_attendance in student_attendance_links:
                session.delete(student_attendance)

            for course_lesson in course_lesson_links:
                session.delete(course_lesson)

            session.commit()

        with Session(engine) as session:
            attendances = get_attendances(session)

            for attendance in attendances:
                session.delete(attendance)

            session.commit()

        with Session(engine) as session:
            students = get_students(session)
            studentclasses = get_studentclasses(session)
            courses = get_courses(session)
            lecturers = get_lecturers(session)
            lessons = get_lessons(session)

            for student in students:
                session.delete(student)

            for studentclass in studentclasses:
                session.delete(studentclass)

            for course in courses:
                session.delete(course)

            for lecturer in lecturers:
                session.delete(lecturer)

            for lesson in lessons:
                session.delete(lesson)

            session.commit()
    except Exception as e:
        print(e)
        return False

    return True
