from application import db
from application.models import Base, kurssimateriaali

from sqlalchemy.sql import text

class Course(Base):

    name = db.Column(db.String(144), nullable=False)

    #Relationships
    coursematerials = db.relationship('Material', secondary=kurssimateriaali, backref=db.backref('kurssimateriaalit', lazy = 'dynamic'))

    def __init__(self, name):
        self.name = name
        self.done = False
        
    def get_id(name):
        return id        
