import click
from flask import Flask
from flask_config import Base
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'admin.login'
login_manager.login_message = 'Login for access this'
login_manager.login_message_category = 'info'

def create_app(class_config=Base):
    app = Flask(__name__)
    app.config.from_object(class_config)
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    from app.admin import bp as admin_bp
    app.register_blueprint(admin_bp)

    return app

from app import models