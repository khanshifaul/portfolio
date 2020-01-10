from app import create_app
from flask import Blueprint, render_template, url_for
from app.forms import ContactForm

bp = Blueprint("main", __name__, template_folder="templates/main")



@bp.route("/")
def index():
    form = ContactForm()
    return render_template("index.html", form=form)

