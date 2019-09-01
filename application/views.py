from flask import render_template
from application import app
from application.auth.models import User
from application.tasks.models import Task
from application.materials.models import Material
from application.courses.models import Course
from application.roles.models import Role
from flask_login import login_required, current_user

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
    
    m = User.query.filter(User.id==1)
    
    if not (current_user == m): 
        return 'admin'

    #res = roles_users.query.filter(roles_users.id==current_user.id).first()
    #stmt = text('SELECT Account.name FROM Account'
                    #' LEFT JOIN roles_users ON role_users."Account.id" = Role.id'
                    #' LEFT JOIN Account ON role_users."account.id" = Account.id'
                    #' WHERE current_user.id = Account.id')
                    
    #res = db.engine.execute(stmt)
    
    #stmt = text('SELECT role.name FROM Role'
                    #' LEFT JOIN roles_users ON role_users."role.id" = Role.id'
                    #' LEFT JOIN Account ON role_users."account.id" = Account.id'
                    #' WHERE current_user.id = Account.id')
                    
    #result.name = db.engine.execute(stmt)

    #response = []
    #for row in res:
        #response.append({"id":row[0]})

    return 'not admin'

@app.route("/")
@login_required
def index():
    return render_template("index.html", all_users=User.find_users(), course_students=User.studentto_course(), 
                           student_materials=User.find_materials_and_users(), find_everything=User.find_materials_courses_users(),
                           g_user_role=required_roles('admin'))
