from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user
from flask_security import current_user, login_required, RoleMixin, Security, \
    SQLAlchemyUserDatastore, UserMixin, utils

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RolesForm, RegistrationForm
from flask import flash
from functools import wraps

def required_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if is_accessible() not in roles:
                flash('Authentication error, please check your details and try again','error')
                return redirect(url_for('index'))
            return f(*args, **kwargs)
        return wrapped
    return wrapper

def is_accessible():

    if not (current_user.role == True): 
        return 'not admin'

    return 'admin'  

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Käyttäjää ei löydy tai salasana on virheellinen.")


    login_user(user)
    return redirect(url_for("personal_space"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/new/", methods=["GET", "POST"])

def auth_create():
    if request.method == "POST":
        form = RegistrationForm(request.form)
        if User.query.filter(User.name == form.name.data).count() > 0:
            return render_template("auth/new.html", form = RegistrationForm())
        else:
            user = User(form.name.data, form.username.data, form.password.data)
            db.session().add(user)
            db.session().commit()
            return render_template("auth/loginform.html", form = LoginForm())
    return render_template("auth/new.html", form = RegistrationForm())

@app.route("/auth/personal/", methods=["GET", "POST"])
@login_required
def personal_space():
    return render_template("auth/personal.html")

@app.route("/roles", methods=["GET", "POST"])
@login_required
@required_roles('admin')
def roles_create():
    if request.method == "GET":
        return render_template("roles/roleform.html", form = RolesForm())
    
    form = RolesForm()
    
    if not form.validate():
       return redirect(url_for("personal_space"))  

    user_to_be_changed = User.query.filter(name=form.name.data).first()

    if (user_to_be_changed.role == True):
        user_to_be_changed.role = False
        db.session.commit()

    user_to_be_changed.role = True
    db.session.commit()           
    return render_template("roles/list.html", form = RolesForm())