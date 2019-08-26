from application import db
from application.models import Base, material2task

from sqlalchemy.sql import text

class Task(Base):

    name = db.Column(db.String(144), nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    #Relationships
    taskmaterials = db.relationship('Material', secondary=material2task, backref=db.backref('koulutusmateriaalit', lazy = 'dynamic'))

    def __init__(self, name):
        self.name = name
        self.done = False
        
    def get_id(name):
        return self.id        
        
    @staticmethod
    def find_tasks():
        stmt = text("SELECT Task.id, Task.name FROM Task")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response        
