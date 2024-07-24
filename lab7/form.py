from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo
import re



class RegisterForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Length(min=2, max=50)])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password'), Length(min=8, max=20)])

    submit = SubmitField("Register")


    def validate_password(self, field):
        password = field.data
        errors = []

        #check for one lowercase letter
        if not re.search(r'[a-z]', password):
            errors.append('Password must contain at least one lowercase letter.')
        #check for one uppercase letter
        if not re.search(r'[A-Z]', password): 
            errors.append('Password must contain at least one uppercase letter.')
        #check for password to end in a number
        if not re.search(r'\d$', password):  
            errors.append('Password must end with a number.')

        if errors: 
            raise ValidationError(' '.join(errors)) 



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    submit = SubmitField("Log In")


