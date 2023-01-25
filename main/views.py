import os
from flask import Flask, render_template, request, url_for, redirect 
from flask_login import LoginManager, login_required,login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from main.models import Customer
from main import blueprint

@blueprint.route('/')
def index():
    return render_template('index.html')

@blueprint.route('/register', methods=["GET", "POST"])
def register():
    form = request.form

    # form = NewAccount(request.POST)
    if form.validate_on_submit():
        firstname = form.firstname.data
        othername = form.username.data
        lastname = form.lastname.data
        email = form.email.data
        password = form.password.data
        address = form.address.data
        phone = form.phone_number.data
        acc_number = ''
        check = check_if_user_exist(email)
        if check == False:
            customer = {
                "firstname" : firstname,
                "lastname" : lastname,
                "email" : email,
                "password" : password,
                "address" : address,
                "phone" : phone,
                "acc_number" : acc_number
            }
            db.session.add(customer)
            db.session.commit()
            return redirect(url_for('profile'))
        else:
            return render_template('register.html')
    return render_template('register.html', form=form)

def check_if_user_exist(email):
    user = Customer.query.filter_by(email=email).first()
    if user:
        return "Customer already exists!"
    return False

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
  
@blueprint.route('/user')
def user():
    return render_template('user.html')

@blueprint.route('/profile')
def profile():
    return render_template('profile.html')

@blueprint.route('/cash_bank')
def cash_bank():
    return render_template('cash_bank.html')

@blueprint.route('/digital')
def digital():
    return render_template('digital.html')

@blueprint.route('/crypto')
def crypto():
    return render_template('crypto.html')

