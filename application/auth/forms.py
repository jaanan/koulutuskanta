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

    #koitetaan päivittää heroku ajan tasalle
