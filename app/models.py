from app import create_app, db, bcrypt, login_manager
from datetime import datetime
from flask_login import UserMixin


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), index=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(250), nullable=False)
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f"Message('{self.email}','{self.subject}', '{self.message}')"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"User('{self.id}', '{self.username}', '{self.date_created}')"
