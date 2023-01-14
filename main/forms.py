from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from ..models import Customer

class NewAccount(FlaskForm):
    firstname = StringField('Firstname', validators=[DataRequired(), Length(1, 64)])

    lastname = StringField('Lastname', validators=[DataRequired(), Length(1, 64)])
    
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='Passwords must match.')])
    
    confirm_password = PasswordField('Confirm password', validators=[DataRequired()])

    address = TextAreaField('Address', validators=[DataRequired(), Length(max=200)])

    phone_number = StringField('Phone Number', validators=[DataRequired()])

    submit = SubmitField('Register')

    print(firstname, lastname, email, password, confirm_password, address, phone_number)
    
    # def validate_email(self, field):
    #     if Customer.query.filter_by(email=field.data).first():
    #         raise ValidationError('Email already registered.')
    
    # def validate_username(self, field):
    #     if Customer.query.filter_by(username=field.data).first():
    #         raise ValidationError('Username already in use.')

class CustomerLogin(FlaskForm):
    acc_number = StringField('Account Number', validators=[DataRequired(), Length(1, 32)])
    
    password = PasswordField('Password', validators=[DataRequired()])