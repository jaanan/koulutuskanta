from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.materials.models import Material
from application.materials.forms import MaterialForm

@app.route("/material", methods=["GET"])
def material_index():
    return render_template("material/list.html", materials = Material.query.all())

@app.route("/materials/new/")
@login_required
def materials_form():
    return render_template("materials/new.html", form = MaterialForm())

@app.route("/materials/", methods=["POST"])
@login_required
def materials_create():
    form = MaterialForm(request.form)
    
    if not form.validate():
        return render_template("materials/new.html", form = form)    

    t = Material(form.name.data)
    
#lisätään aina kaikki materiaalit task eli koulutus id:llä 1:seen, kunnes keskitään, miten tämä toimii    
  
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("materials_index"))
