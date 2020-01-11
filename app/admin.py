from app import create_app, db, bcrypt
from app.models import *
from app.forms import LoginForm
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required

bp = Blueprint(
    "admin", __name__, url_prefix="/admin", template_folder="templates/admin"
)


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("admin.panel"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("main.index"))
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")
    return render_template("login.html", title="Login", form=form)


@bp.route("/")
@bp.route("/panel")
@login_required
def panel():
    msgs = Message.query.order_by(Message.date.desc()).all()
    return render_template("panel.html", msgs=msgs)


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

