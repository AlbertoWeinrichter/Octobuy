import os

basedir = os.path.abspath(os.path.dirname(__file__))
local_postgres = "postgresql://{username}:{password}@{host}:{port}/{database}".format(
    username=os.environ["POSTGRES_USERNAME"],
    password=os.environ["POSTGRES_PASSWORD"],
    host=os.environ["POSTGRES_HOST"],
    database=os.environ["POSTGRES_DATABASE"],
    port=os.environ["POSTGRES_PORT"],
)


class BaseConfig:
    """Base configuration."""

    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious")
    JWT_SECRET_KEY = os.getenv("SECRET_KEY", "Caramelo22")
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = local_postgres


class TestingConfig(BaseConfig):
    """Testing configuration."""

    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = local_postgres + "_test"
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""

    SECRET_KEY = "my_precious"
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgresql:///example"
