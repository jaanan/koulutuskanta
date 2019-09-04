from flask import render_template
from application import app
from application.auth.models import User
from application.tasks.models import Task
from application.materials.models import Material
from application.courses.models import Course
from flask_login import login_required, current_user
from application.auth.models import required_roles

@app.route("/")
@login_required
@required_roles('admin')
def index():
    return render_template("index.html", all_users=User.find_users(), course_students=User.studentto_course(), 
                           student_materials=User.find_materials_and_users(), find_everything=User.find_materials_courses_users(),
                           g_user_role=User.required_roles())
