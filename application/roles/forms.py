from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
class RoleForm(FlaskForm):
    name = StringField("Nimi")
    role = StringField("Rooli")
  
    class Meta:
        csrf = False
