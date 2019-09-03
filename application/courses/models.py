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
        
    def get_id(self):
        return id        

    @staticmethod
    def courseto_material():
        stmt = text('SELECT Course.name AS Kurssi, Material.name AS Materiaali FROM Course, Material, kurssimateriaali'
                        ' WHERE Course.id = kurssimateriaali."course_id"' 
                            ' AND Material.id = kurssimateriaali."material_id"')
        
        result = db.engine.execute(stmt)
        ids = []
        for row in result:
            ids.append({"Kurssi":row[0],"Materiaali":row[1]})
            
        return ids
        