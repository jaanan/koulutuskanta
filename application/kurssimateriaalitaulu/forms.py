from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class UnionForm(FlaskForm):
    course = StringField("Kurssin nimi", [validators.Length(min=8)])
    material = StringField("Materiaalin nimi", [validators.Length(min=8)])

    class Meta:
        csrf = False

            #koitetaan päivittää heroku ajan tasalle
