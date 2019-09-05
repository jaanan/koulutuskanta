from flask import render_template
from application import app
from application.auth.models import User
#from application.tasks.models import Task
from application.materials.models import Material
from application.courses.models import Course
from flask_login import login_required, current_user
from flask import flash
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

    if not (current_user.role == True): 
        return 'not admin'

    return 'admin'  

@app.route("/")
@login_required
@required_roles('admin')
def index():
    return render_template("index.html", all_users=User.find_users(), course_students=User.student_to_course(), 
                           student_materials=User.find_materials_and_users(), find_everything=User.find_materials_courses_users())
