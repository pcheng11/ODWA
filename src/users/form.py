from wtforms import (Form, StringField,
                     SubmitField,
                     PasswordField,
                     DateField)
from wtforms.validators import (DataRequired,
                                Email,
                                EqualTo)

class SignupForm(Form):
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired(message="Please enter a password")])
    confirmPassword = PasswordField('Repeat Password', [DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign Up')


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
