import os
from datetime import timedelta
DB_PASSWORD = 'WBGCI3ElWecukBooRzaH'
DB_ENDPOINT = 'odwa-db.c8he8i54iqnw.us-east-1.rds.amazonaws.com'
DB_MASTER = 'admin'
DB_NAME = 'odwadb'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(DB_MASTER, DB_PASSWORD, DB_ENDPOINT, DB_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "ODWA"
IMAGE_URL_PREFIX = 'https://odwa.s3.amazonaws.com/'

