from app.config import get_settings
from app.db.redis_models import Semester
from app.db.redis_models import Student
from pydantic_aioredis import RedisConfig
from pydantic_aioredis import Store


store = Store(
    name="KEAPlan",
    redis_config=RedisConfig(db=5, host="redis", port=6379),
    life_span_in_seconds=get_settings().redis_persistence_lifetime,
)
store.register_model(Student)
store.register_model(Semester)
