from app import create_app, db
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Message

class ContactForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(message="For contact you back it's necessary. Feel free to put valid one."), Email(message='Please input Valid email.')])
    subject = StringField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    sendbtn = SubmitField("Send Message")

    @staticmethod
    def send_message(form):
        msg = Message(name=form.name.data, email=form.email.data, subject=form.subject.data, message=form.message.data)
        db.session.add(msg)
        db.session.commit()

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    login = SubmitField('Login')

