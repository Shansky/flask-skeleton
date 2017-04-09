from os import getenv


class Config(object):
    """
    Base app configuration
    """
    DEBUG = False
    TESTING = False


class Dev(Config):
    """
    Development app configuration
    """
    DEBUG = True


class Prod(Config):
    """
    Production app configuration
    """
    pass
