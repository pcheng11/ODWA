import os
from datetime import timedelta
basedir = os.path.abspath(os.path.dirname(__file__ + "/../../"))
print(basedir)
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'ODWA.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "ODWA"
AWS_ACCESS_KEY = 'ASIASSNXS3TDZDHLRNTA'
AWS_SECRET_KEY = 'rtSDPkAD0hpx4RTeF5FO/PN/lOvv9+yrYY3elMb+'
AWS_SESSION_TOKEN = 'FwoGZXIvYXdzEOn//////////wEaDIBjYRyNFihT8CEt9iLIAcHNl0I50WkgPdjKBt9G0V7iJ9LPxDZWHvyNQL0l6ZgoJkXBHYjsGH2wW4GqB9eTxNppxHFPgojKEImN+FiC2agOlS/fmpEYixZIuB0MwQeBAvMWcjWGyIIPpV3CdbtmJtiBYJZpiJ+lHmBZ4ef4dGpZbGpIs827H8guwPGGQUJGyZaHpLp5Ft1iFLO26xMxqIY4tovYs/LLUw1N2XXCasZG0QtXuhk09e0BwjE1nGMo2Q4W68+8xDhrEgP+D4tPv0pE4ChSw4TyKOmkoPIFMi2eGOCntDwINe+6/kucG1RQ0GLs5HGjAkDuj/Pyuyk0cEVxMignO/PCVj8mquk='
IMAGE_URL_PREFIX = 'https://odwa.s3.amazonaws.com/'