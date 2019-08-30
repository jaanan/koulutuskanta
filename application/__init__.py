from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
from flask import current_user, login_required, RoleMixin, Security, \
    SQLAlchemyUserDatastore, UserMixin, utils

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"    
    app.config["SQLALCHEMY_ECHO"] = True

  
db = SQLAlchemy(app)

from application import views

from application.roles import models
from application.roles import views

from application.tasks import models
from application.tasks import views

from application.auth import models
from application.auth import views

from application.materials import models
from application.materials import views

from application.courses import models
from application.courses import views

from application.kurssimateriaalitaulu import views
from application.kurssilaistaulu import views


# login
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# lisätään edelliseen sulkuun, mikäli saadaan toimimaan, needs_tasks=User.find_users_with_no_tasks()

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


try: 
    db.create_all()
    user_datastore.find_or_create_role(name='admin', description='Administrator')
    user_datastore.find_or_create_role(name='end-user', description='End user')
except:
    pass
