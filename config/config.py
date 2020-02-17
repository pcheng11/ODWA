import os
from datetime import timedelta
basedir = os.path.abspath(os.path.dirname(__file__ + "/../../"))
print(basedir)
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'ODWA.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "ODWA"
AWS_ACCESS_KEY = 'ASIASSNXS3TDQUBDFLHM'
AWS_SECRET_KEY = 'HUB7upc4RHO9ir6s5yqW863tRkTMGQN2SZ3Ah2em'
AWS_SESSION_TOKEN = 'FwoGZXIvYXdzEAkaDIUoqtDKd7uC2H5KfyLIAZaKrYaYDR1bk1stlRqTIcEOmS1pNx5v//w0cg5K79a5LLTjkGpfCQpxgD2kXnWdTHx3SMyIJJdpTzYyabti13BxBkHVFz7e9oUjev0EQ3v/992Ee5KKsx/pjONfS3bF0t+NlA0IAEGPiC39bnEHGWr0yxg4+z4Rq9R6Zxq4ho64IGdQI9nrlM07BTru3Or+odeNSbVo4+r7KuV0UMlvQK87SZFZbdpamDtKkHy8s8RYn723nPDtpUfUKgN7i7Gjal2Q8ryYVW7uKM6np/IFMi2VxF3Hwk37E5/70QryV2/KjkImDP3iVoSshXPiVTbTCLljoPokE9DLVap5tww='
IMAGE_URL_PREFIX = 'https://odwa.s3.amazonaws.com/'
