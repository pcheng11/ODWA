from flask import Blueprint, request, session, url_for, render_template, redirect, flash, session
from flask_login import login_required, current_user, login_user, logout_user
from .form import SignupForm, LoginForm
from ..models import User, Photo
from src import db
from werkzeug.security import generate_password_hash, check_password_hash
from config.config import IMAGE_URL_PREFIX

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    print(User.query.all())
    if request.method == "POST":
        if form.validate():
            email = request.form['email']
            password = request.form['password']
            name = request.form['username']
            # check useremail
            existing_user = User.query.filter_by(email=email).first()
            if existing_user is None:
                user = User(name=name,
                            email=email,
                            password_hash=generate_password_hash(password, method='sha256'))
                db.session.add(user)
                db.session.commit()
                return (redirect(url_for('users.login')))
            flash('A user already exists with that email address.')

    return render_template('/signup.html', form=form)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if current_user.is_authenticated:
        return redirect(url_for('users.gallery'))
    if request.method == "POST":
        if form.validate():
            email = request.form['email']
            password = request.form['password']

            # check user email
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                if (check_password_hash(existing_user.password_hash, password)):
                    login_user(existing_user)
                    return redirect(url_for('users.profile'))
                    
            flash('Invalid username/password combination')
    return render_template('login.html', form=form)


@user_blueprint.route('/gallery', methods=['GET'])
@login_required
def gallery():
    photo_names = get_thumbimg()
    print(photo_names)
    return render_template("gallery.html", photo_names = photo_names, prefix = IMAGE_URL_PREFIX)


@user_blueprint.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('landing.landing'))

@user_blueprint.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html', user=current_user.name)


def get_thumbimg():
    photo_names = Photo.query.with_entities(Photo.thumbname).filter_by(userid=current_user.id).all()
    return photo_names

def get_img_and_detectimg(img_name):
    photo_names = Photo.query.with_entities(Photo.picname, Photo.detected_picname).filter_by(userid=current_user.id, thumbname=img_name).all()
    return photo_names

@user_blueprint.route('/img/<string:name>', methods=['GET'])
@login_required
def img(name):
    print(name)
    photo_names = get_img_and_detectimg(name)
    return render_template("img.html", photo_names = photo_names, prefix = IMAGE_URL_PREFIX)