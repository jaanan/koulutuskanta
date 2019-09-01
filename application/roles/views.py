from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from flask_login import login_required, current_user
from application.models import Base, roles_users

from application import app, db
from application.auth.models import User
from application.roles.models import Role
from application.roles.forms import RoleForm

from sqlalchemy.sql import text
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
    
    m = User.query.filter(User.id==1)
    
    if not (current_user.name == m.name)
        return 'not admin'

    #res = roles_users.query.filter(roles_users.id==current_user.id).first()
    #stmt = text('SELECT Account.name FROM Account'
                    #' LEFT JOIN roles_users ON role_users."Account.id" = Role.id'
                    #' LEFT JOIN Account ON role_users."account.id" = Account.id'
                    #' WHERE current_user.id = Account.id')
                    
    #res = db.engine.execute(stmt)
    
    #stmt = text('SELECT role.name FROM Role'
                    #' LEFT JOIN roles_users ON role_users."role.id" = Role.id'
                    #' LEFT JOIN Account ON role_users."account.id" = Account.id'
                    #' WHERE current_user.id = Account.id')
                    
    #result.name = db.engine.execute(stmt)

    #response = []
    #for row in res:
        #response.append({"id":row[0]})

    return 'admin'

@app.route("/roles", methods=["GET"])
@login_required
@required_roles('admin')
def roles_index():
    return render_template("roles/roleform.html", form = RoleForm())

@app.route("/roles/new/")
@login_required
def roles_form():
    return render_template("roles/roleform.html", form = RoleForm(), roles = Role.query.all())



@app.route("/roles/new/", methods=["GET", "POST"])

def roles_create():
    if request.method == "POST":
        form = RoleForm(request.form)

    nimi = User.query.filter(User.name==form.name.data).first()
    
    rooli = Role.query.filter(Role.name==form.role.data).first() 
    
    if not(nimi.name in rooli.users):
    
        nimi.roles.append(rooli)
        db.session.commit()       
  
        return redirect(url_for("roles_index"))
            
    return render_template("roles/rolesform.html", form = form, error = "Käyttäjällä on jo rooli")
