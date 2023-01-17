# from flask_login import LoginManager
# from flask_sqlalchemy import SQLAlchemy


# db = SQLAlchemy()
# login_manager = LoginManager()

# def configure_database(app) -> None:
#     @app.before_first_request
#     def initialize_database():
#         db.create_all()

#     @app.teardown_request
#     def shutdown_session(exception=None):
#         db.session.remove()
        
# def register_extensions(app) -> None:
#     db.init_app(app)
#     login_manager.init_app(app)