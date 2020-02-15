from flask import Blueprint, request, session, url_for, render_template, redirect
from flask_login import login_required, current_user
landing_blueprint = Blueprint('landing', __name__)


@landing_blueprint.route('/')
def landing():
    if current_user.is_authenticated:
        return redirect(url_for('users.gallery'))
    return render_template('landing.html', current_user = current_user)
