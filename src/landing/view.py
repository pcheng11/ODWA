from flask import Blueprint, request, session, url_for, render_template, redirect
from flask_login import login_required, current_user
from src.util import record_http_request
from datetime import datetime
landing_blueprint = Blueprint('landing', __name__)
'''
    Landing Page
'''
@landing_blueprint.route('/')
def landing():
    record_http_request(datetime.now(), 'landing/')
    return render_template('landing.html', current_user=current_user)
