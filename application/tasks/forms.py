from flask_wtf import FlaskForm
from wtforms import StringField

class TaskForm(FlaskForm):
    name = StringField("Task name")
 
    class Meta:
        csrf = False

// tähän vähän kommenttia testiksi
