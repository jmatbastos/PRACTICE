from flask import Flask
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, EmailField, PasswordField, \
 SubmitField
from wtforms.validators import DataRequired, \
 Email, EqualTo, Length

app = Flask(__name__)

# Flask-WTF requires this line
csrf = CSRFProtect(app)

class RegisterUserForm(FlaskForm):
    username = StringField(label=('Name'),
    validators=[DataRequired(message='*Required'),
    Length(min=3,max=64, message='Name should be at least %(min)d characters long')])
    email = EmailField(label=('Email Address'),
    validators=[DataRequired(message='*Required'),
    Email(),
    Length(max=120)])
    password = PasswordField(label=('Password'),
    validators=[DataRequired(message='*Required'),
    Length(min=8, message='Password should be at least %(min)d characters long')])
    passconf = PasswordField(
    label=('Confirm Password'),
    validators=[DataRequired(message='*Required'),
    EqualTo('password', message='Both password fields must be equal!')])
    submit = SubmitField(label=('Submit'))