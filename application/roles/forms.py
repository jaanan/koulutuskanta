from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
class RoleForm(FlaskForm):
    name = StringField("Käyttäjänimi")
    role = StringField("Rooli")
  
    class Meta:
        csrf = False
