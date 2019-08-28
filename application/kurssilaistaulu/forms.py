from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class StudentForm(FlaskForm):
    user = StringField("Työntekijän nimi", [validators.Length(min=8)])
    course = StringField("Kurssin nimi", [validators.Length(min=8)])

    class Meta:
        csrf = False
