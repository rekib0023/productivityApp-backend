import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@productivitydbinstance.cgn53psa2l04.us-east-2.rds.amazonaws.com:5432/productivitydb"