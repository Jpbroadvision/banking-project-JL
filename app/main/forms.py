from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from ..models import Customer

class NewAccount(Form):
    username = StringField('Firstname', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, ' 'numbers, dots or underscores')])

    username = StringField('Lastname', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, ' 'numbers, dots or underscores')])
    
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='Passwords must match.')])
    
    password2 = PasswordField('Confirm password', validators=[DataRequired()])

    address = TextAreaField(u'Address', validators=[DataRequired(), Length(max=200)])

    phone_number = StringField('Phone Number', validators=[DataRequired()])

    submit = SubmitField('Register')
    
    def validate_email(self, field):
        if Customer.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
    
    def validate_username(self, field):
        if Customer.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

class CustomerLogin(Form):
    acc_number = StringField('Account Number', validators=[DataRequired(), Length(1, 64)])
    
    password = PasswordField('Password', validators=[DataRequired()])