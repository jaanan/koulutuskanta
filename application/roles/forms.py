from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
class RoleForm(FlaskForm):
    name = StringField("Nimi")
    role = StringField("Rooli")
  
    class Meta:
        csrf = False
        
class RolesForm(FlaskForm):
    name = StringField("Roolin nimi")
    name = StringField("Kuvauksen nimi")
    
    class Meta:
        csrf = False
