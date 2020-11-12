import os


class Config:
    ERROR_404_HELP = False
    SECRET_KEY = os.getenv('APP_SECRET', '&_(+gcl$^3$i&5e(+%c0hacx$chg9t$zs&(wghe9q*f&!+e*2m')
    TEST = "test"

    #SQLALCHEMY_DATABASE_URI = 'sqlite:///tutorial.db'
    #SQLALCHEMY_TRACK_MODIFICATIONS = False

    DOC_USERNAME = 'api'
    DOC_PASSWORD = 'password'


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    #SQLALCHEMY_DATABASE_URI = 'sqlite://'
    TESTING = True
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False


config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig
}