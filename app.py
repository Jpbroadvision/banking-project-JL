from flask import Flask, render_template, request, url_for, redirect 
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
# from init_db import configure_database, register_extensions
from forms import NewAccount
from models import Customer

app = Flask(__name__)           # Instance of the flask web application
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.sqlite3'
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
login_manager = LoginManager(app)
# configure_database(app)
# register_extensions(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_account')
def new_account():
    return render_template('new_account.html')

@app.route('/register', method=["GET", "POST"])
def register():
    form = NewAccount(request.POST)
    # error=''
    if request.method == 'POST' and form.validate():
        firstname = form.firstname.data
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
            db.session.add(Customer(**customer))
            db.session.commit()
            return redirect(url_for('profile'))
        else:
            return render_template('register.html')        #, error=check)
    return render_template('register.html')               #, error=error)

def check_if_user_exist(email):
    user = Customer.query.filter_by(email=email).first()
    if user:
        return "Customer already exists!"
    return False

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')#, error=error)
    # error=''
    # if request.method == 'POST':
    #     if request.form['acc_number'] or request.form['password'] != 'password':
    #         error = 'Invalid Credentials. Please try again.'
    #     else:
    #         return redirect(url_for('user'))
    
  
@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/cash_bank')
def cash_bank():
    return render_template('cash_bank.html')

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html')

# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html') 

if __name__ == '__main__':
    app.run(debug=True)         #debug-True' automatically detects changes and updtaes the application with no need to rerun.