from pydantic_aioredis import Model
from pydantic_aioredis import RedisConfig
from pydantic_aioredis import Store


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


class ClassCourseAttendance(Model):
    name: str
    attendance_percentage: int


class ClassCourse(Model):
    """A course as seen from a class"""
    id: int
    name: str
    course_attendance: list[ClassCourseAttendance]


class Class(Model):
    _primary_key_field: int = "id"
    id: int
    name: str
    courses: list[ClassCourse]


store = Store(
    name="KEAPlan",
    redis_config=RedisConfig(db=5, host="redis", port=6379),
    life_span_in_seconds=3600,
)
store.register_model(Student)
store.register_model(Class)
