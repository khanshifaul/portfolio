from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_config import Base

db = SQLAlchemy()


def create_app(class_config=Base):
    app = Flask(__name__)
    app.config.from_object(class_config)
    db.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
