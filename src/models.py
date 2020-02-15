from flask_login import UserMixin
from . import db
from src import login_manager

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    name = db.Column(db.String(120))
    password_hash = db.Column(db.String(128))

    def __init__(self, name, email, password_hash):
        self.email = email
        self.name = name
        self.password_hash = password_hash

    def __repr__(self):
        return '<User {}, {}>'.format(self.email, self.id)

class Photo(UserMixin, db.Model):
    __tablename__ = 'photos'
    userid = db.Column(db.Integer)
    picname = db.Column(db.String(120), primary_key=True)
    detected_picname = db.Column(db.String(120))
    thumbname = db.Column(db.String(120))

    def __init__(self, userid, picname, detected_picname, thumbname):
        self.userid = userid
        self.picname = picname
        self.detected_picname = detected_picname
        self.thumbname = thumbname

    def __repr__(self):
        return '<Photo {}, {}, {}>'.format(self.picname, self.detected_picname, self.thumbname)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
