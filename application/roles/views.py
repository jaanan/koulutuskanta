from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from flask_login import login_required, current_user

from application import app, db
from application.auth.models import User
from application.roles.models import Role
from application.roles.forms import RoleForm

from sqlalchemy.sql import text

@app.route("/roles", methods=["GET"])
@login_required
def roles_index():
    return render_template("roles/roleform.html", roles = Role.query.all())

@app.route("/roles/new/")
@login_required
def roles_form():
    return render_template("roles/roleform.html", form = RoleForm(), roles = Role.query.all())



@app.route("/auth/new/", methods=["GET", "POST"])

def roles_create():
    if request.method == "POST":
        form = RoleForm(request.form)
        #if User.query.filter(User.name == form.name.data).count() > 0:
            #return render_template("roles/roleform.html", form = RoleForm())
        #else:
            #user = User(form.name.data)
            #role = Role(form.role.data)
            #db.session().add(user)
            #db.session().commit()
            #return render_template("roles/rolesform.html", form = RoleForm())
    nimi = User.query.filter(User.name==form.name.data).first()
    
    rooli = Role.query.filter(Role.name==form.role.data).first() 
    
    if not(nimi.name in rooli.users):
    
        nimi.roles.append(rooli)
        db.session.commit()       
  
        return redirect(url_for("roles_index"))

        if (nimi.name in rooli.users):
        return render_template("roles/rolesform.html", form = form,
                               error = "Käyttäjällä on jo rooli")
            
    return render_template("roles/roleform.html", form = RoleForm())
