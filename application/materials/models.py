from application import db
from application.models import Base

from sqlalchemy.sql import text

class Material(Base):

    name = db.Column(db.String(144), nullable=False)
    t = 1
    task_id = db.Column(db.Integer, db.ForeignKey(t), nullable=False)

    def __init__(self, name):
        self.name = name
