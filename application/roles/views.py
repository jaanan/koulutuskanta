from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from flask_login import login_required, current_user
from application.models import Base, roles_users
from flask import flash

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

    admini = User.query.filter(User.id==1).first()
    
    if not (current_user.name == admini.name): 
        return 'not admin'

    return 'admin'

#@app.route("/roles", methods=["GET"])
#@login_required
#@required_roles('admin')
#def roles_index():
    #return render_template("roles/roleform.html", form = RolesForm())

@app.route("/roles/new/")
@required_roles('admin')
@login_required
def roles_form():
    return render_template("roles/roleform.html", form = RoleForm(), roles = Role.query.all())

@app.route("/roles/new/", methods=["POST"])
@required_roles('admin')
def roles_create():
    form = RoleForm(request.form)
    #if request.method == "POST":
        #form = RoleForm(request.form)
        
    if not form.validate():
        return render_template("roles/roleform.html", form = form) 

    nimi = User.query.filter(User.name==form.name.data).first()
    
    rooli = Role.query.filter(Role.name==form.role.data).first() 
    
    if not(nimi.name in rooli.users):
    
        nimi.roles.append(rooli)
        db.session.commit()       
  
        return redirect(url_for("index"))
            
    return render_template("roles/rolesform.html", form = form, error = "Käyttäjällä on jo rooli")

@app.route("/roles", methods=["GET"])
@login_required
@required_roles('admin')
def roles_index():
    return render_template("roles/list.html", roles = Roles.query.all(), form = RolesForm())

@app.route("/kurssimateriaalitaulu", methods=["GET", "POST"])
@login_required
@required_roles('admin')
def role_maker():
    form = RolesForm(request.form)
    
    if not form.validate():
       return render_template("roles/list.html", form = form)    


    rooli = Role(form.name.data, form.discription.data)
    db.session.add(rooli)
    db.session.commit()
return render_template("roles_index", form = RolesForm())
