from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class TaskForm(FlaskForm):
    name = StringField("Koulutuksen nimi", [validators.Length(min=8)])
    done = BooleanField("Done")
 
    class Meta:
        csrf = False

# tähän vähän kommenttia testiksi
