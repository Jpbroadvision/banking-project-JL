from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

app = Flask(__name__)
Bootstrap(app)
login_manager = LoginManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_account')
def new_account():
    return render_template('new_account.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error=''
    if request.method == 'POST':
        if request.form['acc_number'] != '0123456789' or request.form['password'] != 'password':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('user'))
    return render_template('login.html', error=error)
  
@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/cash_bank')
def cash_bank():
    return render_template('cash_bank.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500    

if __name__ == '__main__':
    app.run(debug=True)

