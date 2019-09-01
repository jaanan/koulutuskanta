from application import db
from application.models import Base, roles_users
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_security import current_user, login_required, RoleMixin, Security, \
    SQLAlchemyUserDatastore, UserMixin, utils

from wtforms.fields import PasswordField

class Role(Base, RoleMixin):

    # Our Role has three fields, ID, name and description
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    # __str__ is required by Flask-Admin, so we can have human-readable values for the Role when editing a User.
    # If we were using Python 2.7, this would be __unicode__ instead.
    def __str__(self):
        return self.name

    # __hash__ is required to avoid the exception TypeError: unhashable type: 'Role' when saving a User
    def __hash__(self):
        return hash(self.name)
    
 
    @staticmethod
    def is_accessible():
        stmt = text('SELECT "role.id" FROM role_users'
                        ' WHERE current_user.id = "account.id"')
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0]})

        return response 
