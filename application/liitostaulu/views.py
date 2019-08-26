from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from wtforms import BooleanField, StringField, validators
from flask_login import login_required, current_user
from application.models import Base, material2task


from application import app, db
from application.materials.models import Material
from application.tasks.models import Task
from application.liitostaulu.forms import UniteForm

from sqlalchemy.sql import text

@app.route("/liitostaulu", methods=["GET"])
@login_required
def liitostaulu_index():
    return render_template("liitostaulu/liitostauluform.html", form = UniteForm())

@app.route("/liitostaulu", methods=["GET", "POST"])
@login_required
def unite_create():
    form = UniteForm(request.form)
    
    if not form.validate():
       return render_template("tasks/new.html", form = form)    

    p = Task(form.task.data)

    c = Material(form.material.data)
        
    p.taskmaterials.append(c)
    db.session.commit()        
  
    return redirect(url_for("tasks_index"))
