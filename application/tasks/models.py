from application import db
from application.models import Base

from sqlalchemy.sql import text

class Task(Base):

    name = db.Column(db.String(144), nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
#    materials = db.relationship("Material", backref='task', lazy=True)

    def __init__(self, name):
        self.name = name
        self.done = False
