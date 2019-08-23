from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.materials.models import Material
from application.tasks.models import Task
from application.liitostaulu.forms import UniteForm

@app.route("/liitostaulu", methods=["GET"])
def liitostaulu_index():
    return render_template("liitostauluform.html")

@app.route("/liitostaulu", methods=["GET", "POST"])
@login_required
def unite_create():
    form = UniteForm(request.form)
    
    if not form.validate():
       return render_template("tasks/new.html", form = form)    

    p = Task(form.task.data)
    m = Task.query.filter(Task.name == form.task.data).count()
    
    if m == 0:
        p.account_id = current_user.id

        db.session().add(p)
        db.session().commit()

    c = Material(form.material.data)
    
    m = Material.query.filter(Material.name == form.material.data).count()
    
    if m == 0:
        db.session().add(c)
        db.session().commit()
        
    p.material2task.append(c)
    db.session.add(p)
    db.session.commit()        
  
    return redirect(url_for("tasks_index"))
