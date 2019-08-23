from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class TaskForm(FlaskForm):
    name = StringField("Koulutuksen nimi", [validators.Length(min=8)])
    done = BooleanField("Suoritettu")
 
    class Meta:
        csrf = False
        
# class UniteForm(FlaskForm):
#    name = StringField("Koulutuksen nimi", [validators.Length(min=8)])
#    name = StringField("Materiaalin nimi", [validators.Length(min=8)])
        
#    s = Student()
#    c = Class()
#    c.students.append(s)
#    db.session.add(c)
#    db.session.commit()

#    class Meta:
#        csrf = False
