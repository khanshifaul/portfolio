import os


class Base(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'secret'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(Base):
    DEBUG = False
    TESTING = False


class Staging(Base):
    DEBUG = True
    TESTING = False


class Development(Base):
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'dev'


class Testing(Base):
    DEBUG = False
    TESTING = True