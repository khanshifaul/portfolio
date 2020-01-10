from app import create_app
from flask import Blueprint, render_template, url_for, flash, redirect
from app.forms import ContactForm

bp = Blueprint("main", __name__, template_folder="templates/main")



@bp.route("/", methods=["GET","POST"])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        ContactForm.send_message(form=form)
        flash('Your message has been sent.', category='info')
        return redirect(url_for('main.index'))
    return render_template("index.html", form=form)

