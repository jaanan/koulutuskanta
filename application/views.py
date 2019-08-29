from flask import render_template
from application import app
from application.auth.models import User
from application.tasks.models import Task
from application.materials.models import Material
from application.courses.models import Course
from flask_login import login_required, current_user

@app.route("/")
@login_required
def index():
    return render_template("index.html", all_users=User.find_users(), all_materials=Material.find_materials(), course_students=User.studentto_course())
