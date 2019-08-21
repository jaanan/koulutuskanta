from application import db
from application.models import Base, material2task

from sqlalchemy.sql import text

class Material(Base):

    name = db.Column(db.String(144), nullable=False)
    
    material2task = db.relationship("Task", secondary = material2task,
                               backref=db.backref('materials', lazy = 'dynamic'))

    def __init__(self, name):
        self.name = name
