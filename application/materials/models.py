from application import db
from application.models import Base, material2task

from sqlalchemy.sql import text

class Material(Base):

    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name
        
    def get_id(name):
        return self.id
        
    @staticmethod
    def find_materials():
        stmt = text("SELECT Material.id, Material.name FROM Material")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response 
