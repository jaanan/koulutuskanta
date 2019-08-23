from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class TaskForm(FlaskForm):
    name = StringField("Koulutuksen nimi", [validators.Length(min=8)])
    done = BooleanField("Suoritettu")
 
    class Meta:
        csrf = False
        
# class UniteForm(FlaskForm):
#    koulutus = StringField("Koulutuksen nimi", [validators.Length(min=8)])
#    material = StringField("Materiaalin nimi", [validators.Length(min=8)])

#    class Meta:
#        csrf = False
