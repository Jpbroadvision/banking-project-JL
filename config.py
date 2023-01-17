import os

basedir = os.path.abspath(os.path.dirname(__file__))    # Returns the banking-project directory and directory of specified files
                                                        # making its content available to the flask app


class Config:                                               
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///customers.sqlite3'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'customers.sqlite3')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')

    
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.sqlite3')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')

    
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'customers.sqlite3')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}