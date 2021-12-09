from app.db.psql_models import Attendance
from app.db.psql_models import Course
from app.db.psql_models import Lecturer
from app.db.psql_models import Lesson
from app.db.psql_models import Student
from app.db.psql_models import StudentClass
from sqlmodel import select
from sqlmodel import Session


# StudentClass
def get_studentclass_by_id(db: Session, studentclass_id: int):
    return db.get(StudentClass, studentclass_id)


def create_studentclass(db: Session, studentclass: StudentClass):
    db_studentclass = StudentClass(
            id=studentclass.id,
            name=studentclass.name,
            number_of_students=studentclass.number_of_students,
            courses=studentclass.courses,
            lecturers=studentclass.lecturers
    )
    db.add(db_studentclass)
    db.commit()
    db.refresh(db_studentclass)
    return db_studentclass


def update_studentclass_by_id(db: Session, studentclass_id: int):
    ...


def delete_studentclass_by_id(db: Session, studentclass_id: int):
    db.delete(db.get(StudentClass, studentclass_id))
    db.commit()


# Student

def get_student_by_id(db: Session, student_id: int):
    return db.exec(select(Student, StudentClass)
                   .join(StudentClass)
                   .where(Student.id == student_id)).one()


def create_student(db: Session, student: Student):
    db_student = Student(
            id=student.id,
            name=student.name,
            class_id=student.class_id,
            attendances=student.attendances
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def update_student_by_id(db: Session, student_id: int):
    ...


def delete_student_by_id(db: Session, student_id: int):
    db.delete(db.get(Student, student_id))
    db.commit()


# Course
def get_course_by_id(db: Session, course_id: int):
    return db.get(Course, course_id)


def create_course(db: Session, course: Course):
    db_course = Course(
            id=course.id,
            name=course.name,
            category=course.category,
            student_classes=course.student_classes,
            lessons=course.lessons
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def update_course_by_id(db: Session, course_id: int):
    ...


def delete_course_by_id(db: Session, course_id: int):
    db.delete(db.get(Course, course_id))
    db.commit()


# Lecturer
def get_lecturer_by_id(db: Session, lecturer_id: int):
    return db.get(Lecturer, lecturer_id)


def create_lecturer(db: Session, lecturer: Lecturer):
    db_lecturer = Lecturer(
            id=lecturer.id,
            name=lecturer.name,
            student_classes=lecturer.student_classes,
    )
    db.add(db_lecturer)
    db.commit()
    db.refresh(db_lecturer)
    return db_lecturer


def update_lecturer_by_id(db: Session, lecturer_id: int):
    ...


def delete_lecturer_by_id(db: Session, lecturer_id: int):
    db.delete(db.get(Lecturer, lecturer_id))
    db.commit()


# Lesson
def get_lesson_by_id(db: Session, lesson_id: int):
    return db.get(Lesson, lesson_id)


def create_lesson(db: Session, lesson: Lesson):
    db_lesson = Lesson(
            id=lesson.id,
            start=lesson.start,
            duration=lesson.duration,
            attendance_token=lesson.attendance_token,
            courses=lesson.courses,
    )
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)
    return db_lesson


def update_lesson_by_id(db: Session, lesson_id: int):
    ...


def delete_lesson_by_id(db: Session, lesson_id: int):
    db.delete(db.get(Lesson, lesson_id))
    db.commit()


# Attendance
def get_attendance_by_id(db: Session, attendance_id: int):
    return db.get(Attendance, attendance_id)


def create_attendance(db: Session, attendance: Attendance):
    db_attendance = Attendance(
            id=attendance.id,
            time_of_attendance=attendance.time_of_attendance,
            lesson_id=attendance.lesson_id,
            students=attendance.students,
    )
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance


def update_attendance_by_id(db: Session, attendance_id: int):
    ...


def delete_attendance_by_id(db: Session, attendance_id: int):
    db.delete(db.get(Attendance, attendance_id))
    db.commit()
