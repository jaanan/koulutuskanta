from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import RegistrationForm
from application.auth.forms import LoginForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/new/")
def auth_form():
    return render_template("auth/new.html")

@app.route("/auth/", methods=["POST"])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.name.data, form.username.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return render_template("auth/loginform.html", form = LoginForm())
    return render_template("auth/loginform.html", form = LoginForm())

# @app.route("/auth/new/", methods=['GET', 'POST'])
# def register():
#    form = RegistrationForm(request.form)
#    if request.method == 'POST' and form.validate():
#        user = User(form.name.data, form.username.data,
#                    form.password.data)
#        db_session.add(user)
#        flash('Thanks for registering')
#        return render_template("auth/loginform.html", form = LoginForm())
#    return render_template("auth/loginform.html", form = LoginForm())
