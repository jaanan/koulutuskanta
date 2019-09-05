from application import db
from application.models import Base, kurssilainen
from flask_security import current_user, login_required, RoleMixin, Security, \
    SQLAlchemyUserDatastore, UserMixin, utils

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    role = db.Column(db.Boolean(), nullable=False)

    courseusers = db.relationship('Course', secondary=kurssilainen, backref=db.backref('kurssilaiset', lazy = 'dynamic'))
  
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.role = False

    def get_id(self):
        return self.id
  
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def required_roles(*roles):
        def wrapper(f):
            @wraps(f)
            def wrapped(*args, **kwargs):
                if is_accessible() not in roles:
                    flash('Authentication error, please check your details and try again','error')
                    return redirect(url_for('index'))
                return f(*args, **kwargs)
            return wrapped
        return wrapper

    def is_accessible():

        if not (current_user.role == True): 
            return 'not admin'

        return 'admin'    


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
        #stmt = text('SELECT Account.name AS Työntekijä, Course.name AS Kurssi FROM Account, Course, kurssilainen'
        #                ' WHERE Course.id = kurssilainen."course.id"' 
        #                    ' AND Account.id = kurssilainen."account.id"')
        
        stmt = text(' SELECT kurssilainen."account.id" COUNT(*) FROM kurssilainen, Course '
                    ' WHERE Course.id = kurssilainen."course.id"'
                    ' GROUP BY Couse.name'

        result = db.engine.execute(stmt)
        ids = []
        for row in result:
            ids.append({"id":row[0], "Course.name":row[1]})
            
        return ids
    
    @staticmethod
    def find_materials_and_users():
        stmt = text('SELECT Course.name AS kurssi, COUNT(*) AS materiaaleja FROM Course, kurssimateriaali'
                     ' WHERE Course.id = kurssimateriaali."course.id"'
                     ' GROUP BY Course.name')
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"Työntekijä":row[0], "Materiaali":row[1]})

        return response
   
    @staticmethod
    def find_materiaalit_and_users():
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
        stmt = text('SELECT Account.name AS Työntekijä, Course.name AS Kurssi, Material.name AS Materiaali FROM Account'
                     ' LEFT JOIN kurssilainen ON kurssilainen."account.id" = Account.id'
                     ' LEFT JOIN Course ON kurssilainen."course.id" = Course.id'
                     ' LEFT JOIN kurssimateriaali ON kurssilainen."course.id" = kurssimateriaali."course.id"'
                     ' LEFT JOIN Material ON kurssimateriaali."material.id" = Material.id'
                     ' WHERE Material.name IS NOT NULL')
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"Työntekijä":row[0], "Kurssi":row[1], "Materiaali":row[2]})

        return response
    
    @staticmethod
    def find_all_my_courses():
        id = current_user.id
        stmt = text('SELECT Course.name AS Kurssi FROM Course '
                     'LEFT JOIN kurssilainen ON kurssilainen."course.id" = Course.id '
                     'WHERE kurssilainen."account.id" = {} '.format(id))
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"Kurssi":row[0]})

        return response               

