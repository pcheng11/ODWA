import os
from datetime import timedelta
basedir = os.path.abspath(os.path.dirname(__file__ + "/../../"))
print(basedir)
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'ODWA.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "ODWA"
AWS_ACCESS_KEY = 'ASIASSNXS3TDV4SVLCRS'
AWS_SECRET_KEY = '5XrHQ3+kFiFGen/fGublBvuIklg5pAqynwqiwpa2'
AWS_SESSION_TOKEN = 'FwoGZXIvYXdzEA0aDOo0jwWvGVK/wy0ZTiLIAeNNNQ71zf0dqLJ2Hy0jQ2Xg40zfvtPfE3F2C3LbB2AD9eqoQZttY3jr2m+v+WljTnRug4rAMJiIrd1f8Mm8eeQ+aTzfZDFGG9FqcYttGpFZJCVf3HWFmQCnZNkEM63blRDB10DqNL/Qq8uIN1+CJ3uQoj3tut6KDZ8iLEjDiOYf22DZbO7lih5dspEr+s0UToVI7ePsll7vGshkA7m9janYXjEQf4Oy/+pS/Pngy0ubs2T8+CuDHyMHB5MnKJkZPYYrkF0RKJeHKLKFqPIFMi24f3FcNQhMr2r+WPzgVdhz3KDebqqLX4euuEXyLz+6Ub8gqVCJu0cs9zLr4n4='
IMAGE_URL_PREFIX = 'https://odwa.s3.amazonaws.com/'
