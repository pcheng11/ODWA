__author__ = 'victor cheng'

from flask import Flask, render_template
# from flask_images import Images
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_session import Session
import boto3
from config.config import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_SESSION_TOKEN
from yolo.yolo import init_yolo
# bootstrap = Bootstrap(app)

app = Flask(__name__)
db = SQLAlchemy()
login_manager = LoginManager()
s3 = boto3.resource('s3', aws_access_key_id=AWS_ACCESS_KEY,
                    aws_secret_access_key=AWS_SECRET_KEY,
                    aws_session_token=AWS_SESSION_TOKEN)
ln, net, LABELS, COLORS = init_yolo()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.config')

    # Initialize Plugins
    db.init_app(app)
    Bootstrap(app)
    login_manager.init_app(app)
    # images = Images(app)

    Migrate(app, db)
    with app.app_context():

        # Import parts of our application
        from .landing.view import landing_blueprint
        from .users.view import user_blueprint
        from .upload.view import upload_blueprint
        app.register_blueprint(landing_blueprint)
        app.register_blueprint(user_blueprint, url_prefix='/users')
        app.register_blueprint(upload_blueprint)
        # Create Database Models
        db.create_all()

        return app

app = create_app()