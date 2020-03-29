import os


DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'tododo')
DB_USER = os.getenv('DB_USER', 'tododo')
DB_PASS = os.getenv('DB_PASS', 'tododo')


class Config(object):
    """Parent configuration class."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'tododo')
    # APP_SETINGS = os.environ.get('APP_SETTINGS') or 'development'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{host}:{port}/{db}'.format(user=DB_USER, pw=DB_PASS,
                                                                                            host=DB_HOST, port=DB_PORT,
                                                                                            db=DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Configuration for development."""
    DEBUG = True


class TestingConfig(Config):
    """Configuration for testing, with a separate test database."""
    TESTING = True
    TEST_DB_USER = 'test_tododo'
    TEST_DB_NAME = 'test_tododo'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{host}:{port}/{db}'.format(user=TEST_DB_USER, pw=DB_PASS,
                                                                                            host=DB_HOST, port=DB_PORT,
                                                                                            db=TEST_DB_NAME)
    DEBUG = True


class ProductionConfig(Config):
    """Configuration for production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
