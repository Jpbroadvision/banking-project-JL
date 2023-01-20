from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
db = SQLAlchemy()

class Customer(UserMixin):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(64), unique=True, index=True)
    lastname = db.Column(db.String(64), unique=True, index=True)
    othername = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))
    address = db.Column(db.String(128), unique=True, index=True)
    phone_number = db.Column(db.Integer, unique=True, index=True)
    acc_number = db.Column(db.Integer, unique=True, index=True)


    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            if hasattr(value, '__iter__') and not isinstance(value, str):
                value = value[0]
            setattr(self, property, value)

@login_manager.user_loader
def load_user(id):
    return Customer.query.filter_by(id=id).first()
