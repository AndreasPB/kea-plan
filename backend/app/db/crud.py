from app.db.psql_models import Attendance
from app.db.psql_models import Course
from app.db.psql_models import CourseLessonLink
from app.db.psql_models import Lecturer
from app.db.psql_models import LecturerClassLink
from app.db.psql_models import Lesson
from app.db.psql_models import Student
from app.db.psql_models import StudentClass
from app.db.psql_models import StudentClassCourseLink
from app.db.psql_models import User
from sqlmodel import select
from sqlmodel import Session


# StudentClass
def get_studentclass_by_id(db: Session, studentclass_id: int):
    return db.get(StudentClass, studentclass_id)


def get_studentclasses(db: Session):
    return db.exec(select(StudentClass)).all()


def create_studentclass(db: Session, studentclass: StudentClass):
    db_studentclass = StudentClass(**studentclass.dict())
    db.add(db_studentclass)
    db.commit()
    db.refresh(db_studentclass)
    return db_studentclass


def update_studentclass_by_id(db: Session, studentclass_id: int):
    raise NotImplementedError("Update student not implemented")


def delete_studentclass_by_id(db: Session, studentclass_id: int):
    db.delete(db.get(StudentClass, studentclass_id))
    db.commit()


# Student
def get_student_by_id(db: Session, student_id: int):
    # return db.exec(select(Student, StudentClass)
    #                .join(StudentClass)
    #                .where(Student.id == student_id)).one()
    return db.get(Student, student_id)


def get_students(db: Session):
    return db.exec(select(Student)).all()


def create_student(db: Session, student: Student):
    db_student = Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def update_student_by_id(db: Session, student_id: int):
    raise NotImplementedError("Update student not implemented")


def delete_student_by_id(db: Session, student_id: int):
    db.delete(db.get(Student, student_id))
    db.commit()


# Course
def get_course_by_id(db: Session, course_id: int):
    return db.get(Course, course_id)


def get_courses(db: Session):
    return db.exec(select(Course)).all()


def create_course(db: Session, course: Course):
    db_course = Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def update_course_by_id(db: Session, course_id: int):
    raise NotImplementedError("Update course not implemented")


def delete_course_by_id(db: Session, course_id: int):
    db.delete(db.get(Course, course_id))
    db.commit()


# Lecturer
def get_lecturer_by_id(db: Session, lecturer_id: int):
    return db.get(Lecturer, lecturer_id)


def get_lecturers(db: Session):
    return db.exec(select(Lecturer)).all()


def create_lecturer(db: Session, lecturer: Lecturer):
    db_lecturer = Lecturer(**lecturer.dict())
    db.add(db_lecturer)
    db.commit()
    db.refresh(db_lecturer)
    return db_lecturer


def update_lecturer_by_id(db: Session, lecturer_id: int):
    raise NotImplementedError("Update lecturer not implemented")


def delete_lecturer_by_id(db: Session, lecturer_id: int):
    db.delete(db.get(Lecturer, lecturer_id))
    db.commit()


# Lesson
def get_lesson_by_id(db: Session, lesson_id: int):
    return db.get(Lesson, lesson_id)


def get_lesson_by_token(db: Session, token: str):
    with db:
        statement = select(Lesson).where(Lesson.attendance_token == token)
        return db.exec(statement).first()


def get_lessons(db: Session):
    return db.exec(select(Lesson)).all()


def create_lesson(db: Session, lesson: Lesson):
    db_lesson = Lesson(**lesson.dict())
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)
    return db_lesson


def update_lesson_by_id(db: Session, lesson_id: int):
    raise NotImplementedError("Update lesson not implemented")


def delete_lesson_by_id(db: Session, lesson_id: int):
    db.delete(db.get(Lesson, lesson_id))
    db.commit()


# Attendance
def get_attendance_by_id(db: Session, attendance_id: int):
    # return db.exec(select(Attendance, Lesson)
    #                .join(Lesson)
    #                .where(Attendance.id == attendance_id)).one()
    return db.get(Attendance, attendance_id)


def get_attendances(db: Session):
    return db.exec(select(Attendance)).all()


def get_attendances_by_lesson_id(db: Session, lesson_id: int):
    with db:
        statement = (
            select(Attendance, Student.name)
            .where(Attendance.lesson_id == lesson_id)
            .join(Student)
        )
        return db.exec(statement).all()


def create_attendance(db: Session, attendance: Attendance):
    db_attendance = Attendance(**attendance.dict())
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance


def update_attendance_by_id(db: Session, attendance_id: int):
    raise NotImplementedError("Update attendance not implemented")


def delete_attendance_by_id(db: Session, attendance_id: int):
    db.delete(db.get(Attendance, attendance_id))
    db.commit()


# User
def create_user(db: Session, user: User):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.exec(select(User)).all()


def get_user_by_id(db: Session, user_id: int):
    return db.get(User, user_id)


def get_user_by_username(db: Session, username: str) -> User:
    with db:
        statement = select(User).where(User.username == username)
        return db.exec(statement).first()


# LecturerClassLink
def get_lecturer_studentclass_by_id(db: Session, lecturer_id: int):
    return db.exec(
        select(StudentClass).join(LecturerClassLink).where(Lecturer.id == lecturer_id)
    ).all()


def get_lecturer_classes(db: Session):
    return db.exec(select(LecturerClassLink)).all()


def create_lecturer_studentclass(db: Session, lecturer_studentclass: LecturerClassLink):
    db_lecturer_class = LecturerClassLink(**lecturer_studentclass.dict())
    db.add(db_lecturer_class)
    db.commit()
    db.refresh(db_lecturer_class)
    return db_lecturer_class


# StudentClassCourseLink
def get_studentclass_course_by_id(db: Session, studentclass_id: int):
    return db.exec(
        select(Course)
        .join(StudentClassCourseLink)
        .where(StudentClass.id == studentclass_id)
    ).all()


def get_studentclass_courses(db: Session):
    return db.exec(select(StudentClassCourseLink)).all()


def create_studentclass_course(
    db: Session, studentclass_course: StudentClassCourseLink
):
    db_studentclass_course = StudentClassCourseLink(**studentclass_course.dict())
    db.add(db_studentclass_course)
    db.commit()
    db.refresh(db_studentclass_course)
    return db_studentclass_course


# CourseLessonLink
def get_course_lessons_by_id(db: Session, course_id: int):
    return db.exec(
        select(Lesson).join(CourseLessonLink).where(Course.id == course_id)
    ).all()


def get_course_lessons(db: Session):
    return db.exec(select(CourseLessonLink)).all()


def create_course_lesson(db: Session, course_lesson: CourseLessonLink):
    db_course_lesson = CourseLessonLink(**course_lesson.dict())
    db.add(db_course_lesson)
    db.commit()
    db.refresh(db_course_lesson)
    return db_course_lesson
