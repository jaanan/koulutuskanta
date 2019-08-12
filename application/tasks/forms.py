from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField

class TaskForm(FlaskForm):
    name = StringField("Koulutuksen nimi")
    done = BooleanField("Done")
 
    class Meta:
        csrf = False

# tähän vähän kommenttia testiksi
