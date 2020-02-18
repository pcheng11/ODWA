import os
from datetime import timedelta
basedir = os.path.abspath(os.path.dirname(__file__ + "/../../"))
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'ODWA.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "ODWA"
IMAGE_URL_PREFIX = 'https://odwa.s3.amazonaws.com/'
