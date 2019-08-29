from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from wtforms import BooleanField, StringField, validators
from flask_login import login_required, current_user
from application.models import Base, kurssilainen


from application import app, db
from application.courses.models import Course
from application.auth.models import User
from application.kurssilaistaulu.forms import StudentForm

from sqlalchemy.sql import text

@app.route("/kurssilaistaulu", methods=["GET"])
@login_required
def kurssilaistaulu_index():
    return render_template("kurssilaistaulu/kurssilaistauluform.html", form = StudentForm(), course_students=User.studentto_course())

@app.route("/kurssilaistaulu", methods=["GET", "POST"])
@login_required
def student_create():
    form = StudentForm(request.form)
    
    if not form.validate():
       return render_template("auth/new.html", form = form)    


    opiskelija = User.query.filter(User.name==form.user.data).first()
    
    kurssi = Course.query.filter(Course.name==form.course.data).first() 
    
    if not(opiskelija.name in kurssi.kurssilaiset):

        opiskelija.courseusers.append(kurssi)
        db.session.commit()       
  
    return redirect(url_for("index"))
