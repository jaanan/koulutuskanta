from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CourseForm(FlaskForm):
    name = StringField("Kurssin nimi", [validators.Length(min=8)])
    
    class Meta:
        csrf = False

              
