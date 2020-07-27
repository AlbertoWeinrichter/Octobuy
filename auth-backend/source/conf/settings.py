import os

basedir = os.path.abspath(os.path.dirname(__file__))
local_postgres = 'postgresql://{username}:{password}@{host}/{database}'.format(
    username=os.environ["POSTGRES_USERNAME"],
    password=os.environ["POSTGRES_PASSWORD"],
    host=os.environ["POSTGRES_HOST"],
    database=os.environ["POSTGRES_DATABASE"]
)


class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = os.getenv('DEBUG')
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = os.getenv('DEBUG')
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = local_postgres


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = os.getenv('DEBUG')
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = local_postgres + '_test'
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = os.getenv('DEBUG')
    SECRET_KEY = 'my_precious'
    SQLALCHEMY_DATABASE_URI = 'postgresql:///example'
