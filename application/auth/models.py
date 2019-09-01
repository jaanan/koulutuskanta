from application import db
from application.models import Base, kurssilainen, roles_users
from flask_security import current_user, login_required, RoleMixin, Security, \
    SQLAlchemyUserDatastore, UserMixin, utils

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    tasks = db.relationship("Task", backref='account', lazy=True)
    courseusers = db.relationship('Course', secondary=kurssilainen, backref=db.backref('kurssilaiset', lazy = 'dynamic'))
    
    roles = db.relationship(
        'Role',
        secondary=roles_users,
        backref=db.backref('users', lazy='dynamic')
    )
  
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id
  
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

      
    @staticmethod
    def find_users_with_no_tasks():
        stmt = text("SELECT Account.id, Account.name FROM Account"
                     " LEFT JOIN Task ON Task.account_id = Account.id"
                     " WHERE (Task.done IS null OR Task.done = 1)"
                     " GROUP BY Account.id"
                     " HAVING COUNT(Task.id) = 0")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response

    @staticmethod
    def find_users():
        stmt = text("SELECT Account.id, Account.name FROM Account")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response
    
    
    @staticmethod
    def studentto_course():
        stmt = text("SELECT Account.name AS Työntekijä, Course.name AS Kurssi FROM Account, Course, kurssilainen"
                        " WHERE Course.id = kurssilainen.'course.id'"
                            " AND Account.id = kurssilainen.'account.id'")
        
        result = db.engine.execute(stmt)
        ids = []
        for row in result:
            ids.append({"Työntekijä":row[0], "Kurssi":row[1]})
            
        return ids
    
    
    @staticmethod
    def find_materials_and_users():
        stmt = text('SELECT Account.name AS Työntekijä, Material.name AS Materiaali FROM Account'
                     ' LEFT JOIN kurssilainen ON kurssilainen."account.id" = Account.id'
                     ' LEFT JOIN kurssimateriaali ON kurssilainen."course.id" = kurssimateriaali."course.id"'
                     ' LEFT JOIN Material ON kurssimateriaali."material.id" = Material.id'
                     ' WHERE Material.name IS NOT NULL')
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"Työntekijä":row[0], "Materiaali":row[1]})

        return response
    
        @staticmethod
        def find_materials_courses_users():
        stmt = text('SELECT Account.name AS Työntekijä, Course.name AS Kurssi Material.name AS Materiaali FROM Account'
                     ' LEFT JOIN kurssilainen ON kurssilainen."account.id" = Account.id'
                     ' LEFT JOIN Course ON kurssilainen."course.id" = Course.id'
                     ' LEFT JOIN kurssimateriaali ON kurssilainen."course.id" = kurssimateriaali."course.id"'
                     ' LEFT JOIN Material ON kurssimateriaali."material.id" = Material.id'
                     ' WHERE Material.name IS NOT NULL')
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"Työntekijä":row[0], "Kurssi":row[1]}, "Materiaali":row[2]})

        return response

