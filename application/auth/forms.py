from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False

class RegistrationForm(FlaskForm):
    name = StringField("Nimi")
    username = StringField("Käyttäjänimi")
    password = PasswordField("Salasana")

class RolesForm(FlaskForm):
    name = StringField("Työntekijän nimi")
    
    class Meta:
        csrf = False

class NameChangeForm(FlaskForm):
    name = StringField("Anna uusi nimi")
    
    class Meta:
        csrf = False

class U_nameChangeForm(FlaskForm):
    username = StringField("Anna uusi käyttäjänimi")
    
    class Meta:
        csrf = False 

class PasswordChangeForm(FlaskForm):
    password = StringField("Anna uusi salasana")
    
    class Meta:
        csrf = False         