from flask import Flask
# from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
from flask_migrate import Migrate


db = SQLAlchemy()
# mail = Mail()
# login_manager = LoginManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.secret_key = "thisprojectismomandme"  # Change this to a secure secret key in production

    # Database Configuration
    app.config["DEBUG"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///momandme.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    
    # Mail Configuration
    # app.config['MAIL_SERVER']='smtp.gmail.com'
    # app.config['MAIL_PORT'] = 587
    # app.config['MAIL_USERNAME'] = 'vishnujavvaji19@gmail.com'
    # app.config['MAIL_PASSWORD'] = 'aiun nsnp auvd nrbt' #   'oowd hosw eeuv jguy'
    # app.config['MAIL_USE_TLS'] = True
    # app.config['MAIL_USE_SSL'] = False
    # app.config['MAIL_DEFAULT_SENDER'] = 'vishnujavvaji19@gmail.com'

    # mail.init_app(app)

    # Initialize extensions

    db.init_app(app)
    # mail.init_app(app)
    # login_manager.init_app(app)
    migrate.init_app(app, db)
    
    # login_manager.login_view = "views.login"  # Redirect to login page if user is not logged in

    # User Loader Function
    # from app.models import User  # Import User model after db initialization to avoid circular imports

    # @login_manager.user_loader
    # def load_user(user_id):
    #     return User.query.get(int(user_id))

    # Import routes after db initialization to avoid circular imports
    from app.views import views

    # Register blueprints
    app.register_blueprint(views, url_prefix="/")
    


    with app.app_context():
        db.create_all()

    return app