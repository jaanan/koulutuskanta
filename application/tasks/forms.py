from flask_wtf import FlaskForm
from wtforms import StringField

class TaskForm(FlaskForm):
    name = StringField("Koulutuksen nimi")
 
    class Meta:
        csrf = False

# tähän vähän kommenttia testiksi
