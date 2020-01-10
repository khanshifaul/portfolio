import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Base(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cSAziGQ4SrzuSmmyOLuky5nqiRJ3i9Q7'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'database.db')
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