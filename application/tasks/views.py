from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.tasks.models import Task
from application.tasks.forms import TaskForm
from application.tasks.forms import UniteForm

@app.route("/tasks", methods=["GET"])
def tasks_index():
    return render_template("tasks/list.html", tasks = Task.query.all())

@app.route("/tasks/new/")
@login_required
def tasks_form():
    return render_template("tasks/new.html", form = TaskForm())
  
@app.route("/tasks/<task_id>/", methods=["POST"])
@login_required
def tasks_set_done(task_id):

    t = Task.query.get(task_id)
    if t.done == True:
        t.done = False
    elif t.done == False:
        t.done = True    
    db.session().commit()
  
    return redirect(url_for("tasks_index"))

@app.route("/tasks/", methods=["POST"])
@login_required
def tasks_create():
    form = TaskForm(request.form)
    
    if not form.validate():
        return render_template("tasks/new.html", form = form)    

    t = Task(form.name.data)
    t.done = form.done.data
    m = Task.query.filter(Task.name == form.name.data).count()
    
    if m > 0:
        return redirect(url_for("tasks_index"))
    else:
        t.done = form.done.data
        t.account_id = current_user.id

        db.session().add(t)
        db.session().commit()
  
    return redirect(url_for("tasks_index"))

#Alla hahmotelma uudesta metodista

@app.route("/tasks/", methods=["POST"])
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
