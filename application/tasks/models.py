from application import db
from application.models import Base, material2task

from sqlalchemy.sql import text

class Task(Base):

    name = db.Column(db.String(144), nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    #Relationships
    material2task = db.relationship("Material", secondary = material2task,
                               backref=db.backref('tasks', lazy = 'joined'))

    def __init__(self, name):
        self.name = name
        self.done = False
