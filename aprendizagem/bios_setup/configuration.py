import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SECRET_KEY = 'bios_setup-key'

# SQLALCHEMY_DATABASE_URI = 'sqlite:///../app.db'
#SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://sisBIOS:93fsv20t@SQLServer'
SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://gbi:fpf@1212@SQLServer'
