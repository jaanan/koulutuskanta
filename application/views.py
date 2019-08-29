from flask import render_template
from application import app
from application.auth.models import User
from application.tasks.models import Task
from application.materials.models import Material
from application.courses.models import Course

@app.route("/")
def index():
    return render_template("index.html", all_users=User.find_users(), all_materials=Material.find_materials())
