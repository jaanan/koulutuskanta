from flask_login import login_required, current_user
from flask import render_template, request, redirect, url_for
from application import app
from application.auth.models import User
from application.tasks.models import Task
from application.materials.models import Material
from application.tasks.forms import UniteForm

@app.route("/")
def index():
    return render_template("index.html", needs_tasks=User.find_users_with_no_tasks(), all_users=User.find_users(), 
                           all_tasks=Task.find_tasks(), all_materials=Material.find_materials())

@app.route("/tasks/", methods=["GET", "POST"])
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
