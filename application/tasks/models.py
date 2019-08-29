from application import db
from application.models import Base, koulutusmateriaali

from sqlalchemy.sql import text

class Task(Base):

    name = db.Column(db.String(144), nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    #Relationships
    #taskmaterials = db.relationship('Material', secondary=koulutusmateriaali, backref=db.backref('koulutusmateriaalit', lazy = 'dynamic'))

    def __init__(self, name):
        self.name = name
        self.done = False
        
    def get_id(name):
        return id        
        
    @staticmethod
    def find_tasks():
        stmt = text("SELECT Task.name FROM Task"
                        " GROUP BY Task.name;")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0]})

        return response 

    @staticmethod
    def connect_account():
        stmt = text("SELECT Account.name AS Työntekijä, Task.name AS Koulutus  FROM Task, Account"
                        " WHERE Account.id = Task.account_id"
                        " ORDER BY Account.name;")
        
        result = db.engine.execute(stmt)
        ids = []
        for row in result:
            ids.append({"Työntekijä":row[0],"Koulutus":row[1]})
           
        return ids
    
    #@staticmethod
    #def connect_taskmaterial():
        #stmt = text("SELECT Account.name AS Työntekijä, Task.name AS Koulutus, Material.name AS Materiaali FROM Account, Task, Material, koulutusmateriaali"
                        #" WHERE Task.id = koulutusmateriaali.'task.id'"
                            #" AND Material.id = koulutusmateriaali.'material.id'"
                            #" AND Account.id = Task.account_id"
                        #" ORDER BY Account.name;")
        
        #result = db.engine.execute(stmt)
        #ids = []
        #for row in result:
            #ids.append({"Työntekijä":row[0],"Koulutus":row[1],"Materiaali":row[2]})
           
        #return ids
