import click
from app import db, bcrypt
from app.models import User
from flask.cli import with_appcontext
from getpass import getpass


def register(app):
    @app.cli.group()
    def user():
        pass

    @user.command()
    def create():
        username = input("Enter Username: ")
        password = getpass("Enter Password: ")
        confirm_password = input("Confirm Password: ")
        if password == confirm_password:
            pw_hash = bcrypt.generate_password_hash(password).decode("utf-8")
            user = User(username=username, password=pw_hash)
            db.session.add(user)
            db.session.commit()
            print("\nUser creation successful.")
        else:
            print("Password didn't match.")

