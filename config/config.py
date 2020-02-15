import os
from datetime import timedelta
basedir = os.path.abspath(os.path.dirname(__file__ + "/../../"))
print(basedir)
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'ODWA.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "ODWA"
AWS_ACCESS_KEY = 'ASIASSNXS3TD3S2O4BYR'
AWS_SECRET_KEY = 'bfiM/xdaMirIrfebmtFd1dwVW6AAxjFEylC8RL+q'
AWS_SESSION_TOKEN = 'FwoGZXIvYXdzEK///////////wEaDAkoBSWTPOolYEXq2yLIAbZV4VeSvPsyH5VmrDgMmL6yIHzjjTTq3UMnNmgIXS09bNchScgxgqfQTtIJcvR4ImQji4QtdRxzbJ0irCcaHpmDJqzyjJky+axYCMsHhT1aStuK3K3XfDqgIMYoDIu7WVk/ofGbXbsrkzb7TxGX866n9drL5bEQezlRp+BYzCiNLwg8KkWSwre68HhsqWSdhmp8M8SkhZrYgjefFhLMf+tRSgCHINycoZAxYimKJ7ilM7+p6VQvf3laaOlwDeWi/7STWjmIVkJWKL+zk/IFMi3Q202euU/nte5079NYh6B26xixgbeEju4EyeoMBuc7F+DKyksGWh3Gn6AZMHM='
IMAGE_URL_PREFIX = 'https://odwa.s3.amazonaws.com/'