from pydantic_aioredis import Model
from pydantic_aioredis import RedisConfig
from pydantic_aioredis import Store


class Course(Model):
    id: int
    name: str


class Student(Model):
    _primary_key_field: int = "id"
    id: int
    name: str
    courses: list[Course, str]


# TODO: Isn't implemented yet
class Class(Model):
    _primary_key_field: int = "id"
    id: int
    name: str
    courses: list[Course, list[str, str]]


store = Store(
    name="KEAPlan",
    redis_config=RedisConfig(db=5, host="redis", port=6379),
    life_span_in_seconds=3600,
)
store.register_model(Student)


# Test data
students = [
    Student(
        id=1,
        name="John",
        courses=[
            Course(id=1, name="Python", attendance="60%"),
            Course(id=2, name="Java", attendance="70%"),
            Course(id=3, name="C++", attendance="80%"),
        ],
    ),
    Student(
        id=2,
        name="Jane",
        courses=[
            Course(id=1, name="Python", attendance="65%"),
            Course(id=2, name="Java", attendance="75%"),
            Course(id=3, name="C++", attendance="85%"),
        ],
    ),
]
