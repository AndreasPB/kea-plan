from datetime import datetime
from typing import List
from typing import Optional

from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel


class LecturerClassLink(SQLModel, table=True):
    lecturer_id: Optional[int] = Field(
        default=None, foreign_key="lecturer.id", primary_key=True
    )
    class_id: Optional[int] = Field(
        default=None, foreign_key="studentclass.id", primary_key=True
    )


class StudentClassCourseLink(SQLModel, table=True):
    class_id: Optional[int] = Field(
        default=None, foreign_key="studentclass.id", primary_key=True
    )
    course_id: Optional[int] = Field(
        default=None, foreign_key="course.id", primary_key=True
    )


class StudentAttendanceLink(SQLModel, table=True):
    student_id: Optional[int] = Field(
        default=None, foreign_key="student.id", primary_key=True
    )
    attendance_id: Optional[int] = Field(
        default=None, foreign_key="attendance.id", primary_key=True
    )


class CourseLessonLink(SQLModel, table=True):
    course_id: Optional[int] = Field(
        default=None, foreign_key="course.id", primary_key=True
    )
    lesson_id: Optional[int] = Field(
        default=None, foreign_key="lesson.id", primary_key=True
    )


class StudentClass(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    number_of_students: int

    courses: List["Course"] = Relationship(
        back_populates="student_classes", link_model=StudentClassCourseLink
    )

    lecturers: List["Lecturer"] = Relationship(
        back_populates="student_classes", link_model=LecturerClassLink
    )


class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    class_id: Optional[int] = Field(default=None, foreign_key="studentclass.id")

    attendances: List["Attendance"] = Relationship(
        back_populates="students", link_model=StudentAttendanceLink
    )


class Course(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    category: str

    student_classes: List["StudentClass"] = Relationship(
        back_populates="courses", link_model=StudentClassCourseLink
    )

    lessons: List["Lesson"] = Relationship(
        back_populates="courses", link_model=CourseLessonLink
    )


class Lecturer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    student_classes: List["StudentClass"] = Relationship(
        back_populates="lecturers", link_model=LecturerClassLink
    )


class Lesson(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    start: datetime
    duration: int
    attendance_token: str

    courses: List["Course"] = Relationship(
        back_populates="lessons", link_model=CourseLessonLink
    )


class Attendance(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    time_of_attendance: datetime

    lesson_id: Optional[int] = Field(default=None, foreign_key="lesson.id")

    students: List["Student"] = Relationship(
        back_populates="attendances", link_model=StudentAttendanceLink
    )


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str

    student_id: Optional[int] = Field(default=None, foreign_key="student.id")
