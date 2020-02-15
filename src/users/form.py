from wtforms import (Form, StringField,
                     SubmitField,
                     PasswordField,
                     DateField)
from wtforms.validators import (DataRequired,
                                Email,
                                EqualTo)

class SignupForm(Form):
    username = StringField('Username', [DataRequired()])
    email = StringField('Email', [Email(message='Not a valid email address'), DataRequired()])
    password = PasswordField('Password', [DataRequired(message="Please enter a password")])
    confirmPassword = PasswordField('Repeat Password', [DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign Up')


class LoginForm(Form):
    email = StringField('Email', validators=[Email(message='Not a valid email address.'), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
