from application import db
from application.models import Base, roles_users
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_security import current_user, login_required, RoleMixin, Security, \
    SQLAlchemyUserDatastore, UserMixin, utils
from functools import wraps
from flask import flash

from wtforms.fields import PasswordField

class Role(Base, RoleMixin):

    # Our Role has three fields, ID, name and description
    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=False)

    # __str__ is required by Flask-Admin, so we can have human-readable values for the Role when editing a User.
    # If we were using Python 2.7, this would be __unicode__ instead.
    def __str__(self):
        return self.name

    # __hash__ is required to avoid the exception TypeError: unhashable type: 'Role' when saving a User
    def __hash__(self):
        return hash(self.name)
    
    def required_roles(*roles):
        def wrapper(f):
            @wraps(f)
            def wrapped(*args, **kwargs):
                if is_accessible() not in roles:
                    flash('Authentication error, please check your details and try again','error')
                    return redirect(url_for('index'))
                return f(*args, **kwargs)
            return wrapped
        return wrapper

    def is_accessible():

        m = flask_security.current_user.id

        if not (m.role == True): 
            return 'admin'

        return 'not admin'
