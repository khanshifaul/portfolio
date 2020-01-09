import os


class Base(object):
    DEBUG = False
    TESTING = False


class Production(Base):
    DEBUG = False
    TESTING = False


class Staging(Base):
    DEBUG = True
    TESTING = False


class Development(Base):
    DEBUG = True
    TESTING = True


class Testing(Base):
    DEBUG = False
    TESTING = True