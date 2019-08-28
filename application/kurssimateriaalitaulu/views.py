from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from wtforms import BooleanField, StringField, validators
from flask_login import login_required, current_user
from application.models import Base, kurssimateriaali


from application import app, db
from application.materials.models import Material
from application.courses.models import Course
from application.kurssimateriaalitaulu.forms import UnionForm

from sqlalchemy.sql import text

@app.route("/kurssimateriaalitaulu", methods=["GET"])
@login_required
def kurssimateriaalitaulu_index():
    return render_template("kurssimateriaalitaulu/kurssimateriaalitauluform.html", form = UnionForm())

@app.route("/kurssimateriaalitaulu", methods=["GET", "POST"])
@login_required
def union_create():
    form = UnionForm(request.form)
    
    if not form.validate():
       return render_template("courses/new.html", form = form)    


    kurssi = Course.query.filter(Course.name==form.course.data).first()
    
    materiaali = Material.query.filter(Material.name==form.material.data).first() 
    
    if not(kurssi.name in materiaali.kurssimateriaalit):
    
        kurssi.coursematerials.append(materiaali)
        db.session.commit()       
  
    return redirect(url_for("courses_index"))
