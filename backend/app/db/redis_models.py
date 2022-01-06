from pydantic_aioredis import Model


class StudentCourse(Model):
    """A course as seen from a student"""

    id: int
    name: str
    attendance_percentage: int


class Student(Model):
    _primary_key_field: int = "id"
    id: int
    name: str
    courses: list[StudentCourse]


class SemesterCourseAttendance(Model):
    name: str
    attendance_percentage: int


class SemesterCourse(Model):
    """A course as seen from a class"""

    id: int
    name: str
    course_attendance: list[SemesterCourseAttendance]


class Semester(Model):
    _primary_key_field: int = "id"
    id: int
    name: str
    courses: list[SemesterCourse]
