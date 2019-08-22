from flask import render_template
from application import app
from application.auth.models import User
from application.tasks.models import Task
from application.materials.models import Material

@app.route("/")
def index():
    return render_template("index.html", needs_tasks=User.find_users_with_no_tasks(), all_users=User.find_users(), 
                           all_tasks=Task.find_tasks(), all_materials=Material.find_materials())
