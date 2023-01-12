from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_account')
def new_account():
    return render_template('new_account.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/cash_bank')
def cash_bank():
    return render_template('cash_bank.html')

if __name__ == '__main__':
    app.run(debug=True)