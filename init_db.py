from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
login_manager = LoginManager()

def configure_database(app) -> None:
    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()
        
# def register_extensions(app) -> None:
#     db.init_app(app)
#     login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return None


# def create_app(config):
#     app = Flask(__name__)           # Instance of the flask web application
#     app.config.from_object(config)
#     configure_database(app)
#     register_extensions(app)
#     return app