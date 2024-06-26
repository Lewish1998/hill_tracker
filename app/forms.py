from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField, TimeField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, Optional
import sqlalchemy as sa
from app import db
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')
    
    
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, message='Username must be at least 4 characters long')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message='Password must be at least 8 characters long')])
    password2 = PasswordField(
        'Password Confirm', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(
            User.username == username.data))
        if user is not None:
            raise ValidationError('Please use a different username.')
        
    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(
            User.email == email.data))
        if user is not None:
            raise ValidationError('Please use a different email address.')
        

class AddNewHillForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    distance = DecimalField('Distance', places=2, validators=[Optional()])
    height = DecimalField('Height', places=2, validators=[Optional()])
    latitude = DecimalField('Latitude', validators=[Optional()])
    longitude = DecimalField('Longitude', validators=[Optional()])
    time = StringField('Time', validators=[Optional()])
    submit = SubmitField('Add')
    

class EditHillForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    distance = DecimalField('Distance', places=2, validators=[Optional()])
    height = DecimalField('Height', places=2, validators=[Optional()])
    latitude = DecimalField('Latitude', validators=[Optional()])
    longitude = DecimalField('Longitude', validators=[Optional()])
    submit = SubmitField('Save Changes')