import os


class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI", "mysql+pymysql://user:pass@localhost:3306/mercury_watch"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:5173")
    CACHE_TTL = int(os.getenv("CACHE_TTL", "3600"))
    PAGE_SIZE = int(os.getenv("PAGE_SIZE", "20"))
    MAX_LIMIT = int(os.getenv("MAX_LIMIT", "1000"))
    MAX_OFFSET = int(os.getenv("MAX_OFFSET", "10000"))
    RATE_LIMIT = os.getenv("RATE_LIMIT", "60/minute")


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    DEBUG = False
