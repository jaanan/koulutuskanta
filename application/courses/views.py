from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.courses.models import Course
from application.courses.forms import CourseForm

from sqlalchemy.sql import text

@app.route("/course", methods=["GET"])
@login_required
def course_index():
    return render_template("courses/list.html", courses = Course.query.all())

@app.route("/courses/new/")
@login_required
def courses_form():
    return render_template("courses/new.html", form = CourseForm(), courses = Course.query.all())

@app.route("/courses/", methods=["POST"])
@login_required
def courses_create():
    form = CourseForm(request.form)
    
    if not form.validate():
        return render_template("courses/new.html", form = form)    

    t = Course(form.name.data)
    
    m = Course.query.filter(Course.name == form.name.data).count()
    
    if m > 0:
        return redirect(url_for("course_index"))
    else:
        db.session().add(t)
        db.session().commit()
  
    return redirect(url_for("course_index"))
