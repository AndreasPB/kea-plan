import string
from enum import Enum
from functools import lru_cache
from pathlib import Path

from pydantic import BaseSettings


class Environment(str, Enum):
    DEVELOPMENT = "development"
    TESTING = "testing"
    PRODUCTION = "production"


class Settings(BaseSettings):
    """
    Settings will be overwritten by any environment variables
    matching the variable names below
    """
    environment: Environment = Environment.DEVELOPMENT
    keaplan_url: str = "localhost"
    token_size: int = 4
    token_chars: str = string.ascii_uppercase + string.digits

    # TODO: Read up on getting data back into memory from disk when lifetime is hit
    # Whole day in seconds: 3600 * 24 = 86400
    redis_persistence_lifetime: int = 86400

    psql_user: str = "postgres"
    psql_pwd: str = "postgres"

    class Config:
        env_file = Path("../.env")


@lru_cache
def get_settings() -> Settings:
    return Settings()
