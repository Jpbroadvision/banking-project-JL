from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
boostrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)