from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class UniteForm(FlaskForm):
    task = StringField("Koulutuksen nimi", [validators.Length(min=8)])
    material = StringField("Materiaalin nimi", [validators.Length(min=8)])

    class Meta:
        csrf = False
