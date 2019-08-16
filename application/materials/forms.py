from flask_wtf import FlaskForm
from wtforms import StringField, validators

class MaterialForm(FlaskForm):
    name = StringField("Materiaalin nimi", [validators.Length(min=8)])
