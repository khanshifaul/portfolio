from app import create_app, db
from datetime import datetime

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(250), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Message('{self.email}','{self.subject}', '{self.message}')"