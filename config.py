import os
from datetime import timedelta


class Config(object):
    VERSION = "0.0.1"


    DB_HOST = 'localhost'
    DB_DATABASE = 'gino'

    # https://python-gino.org/docs/en/1.0/reference/extensions/sanic.html?highlight=sanic
    # DB_PORT
    # DB_USER
    # DB_PASSWORD
    # DB_ECHO
    # DB_POOL_MIN_SIZE
    # DB_POOL_MAX_SIZE
    # DB_USE_CONNECTION_FOR_REQUEST
    # DB_KWARGS


    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT
    PROPAGATE_EXCEPTIONS = True
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=8)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=6)
    JWT_ERROR_MESSAGE_KEY = "message"


class DevelopmentConfig(Config):
    # Statement for enabling the development environment
    DEBUG = True
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=6)

    # Use a secure, unique and absolutely secret key for signing the data.
    CSRF_SESSION_KEY = "secret"
    # Secret key for signing cookies
    SECRET_KEY = "=!w-tp!0xuqscy*6^er*@l$5s#pu$#*17upk=dg-i_03@##=_)"
    # JWT Secret Key
    JWT_SECRET_KEY = "jwt-secret-string"

    # Define the database we are working with
    POSTGRES = {
        "user": "dev_user",
        "pw": "dev_pass",
        "db": "dev_db",
        "host": "localhost",
        "port": "5432",
    }
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES
    )
    DATABASE_CONNECT_OPTIONS = {}


class TestingConfig(Config):
    # Statement for enabling the development environment
    DEBUG = False

    # Use a secure, unique and absolutely secret key for signing the data.
    CSRF_SESSION_KEY = "testing"
    # Secret key for signing cookies
    SECRET_KEY = "=!w-tp!0xuqscy*6^er*@l$5s#pu$#*17upk=dg-i_03@##=_)"
    # JWT Secret Key
    JWT_SECRET_KEY = "jwt-testing-string"

    # Define the database we are working with
    POSTGRES = {
        "user": "dev_user",
        "pw": "dev_pass",
        "db": "dev_db",
        "host": "localhost",
        "port": "5432",
    }
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES
    )
    DATABASE_CONNECT_OPTIONS = {}


class ProductionConfig(Config):
    # Statement for enabling the development environment
    DEBUG = False
    try:
        # Use a secure, unique and absolutely secret key for signing the data.
        CSRF_SESSION_KEY = os.environ["CSRF_SESSION_KEY"]
        # Secret key for signing cookies
        SECRET_KEY = os.environ["SECRET_KEY"]
        # JWT Secret Key
        JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]

        SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
        # DATABASE_CONNECT_OPTIONS = {}
    except Exception as e:
        print("PRODUCTION CONFIG ENVIRONMENT VARIABLES HAVE ISSUES =>> " + str(e))


del os  # noqa: E305
