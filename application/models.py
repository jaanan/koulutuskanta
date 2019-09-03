from application import db

class Base(db.Model):

    __abstract__ = True
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())


kurssimateriaali = db.Table('kurssimateriaali',
                          db.Column('course_id', db.Integer, db.ForeignKey('course.id')),
                          db.Column('material_id', db.Integer, db.ForeignKey('material.id')),
                          db.PrimaryKeyConstraint('course_id', 'material_id'))

kurssilainen = db.Table('kurssilainen',
                          db.Column('account_id', db.Integer, db.ForeignKey('account.id')),
                          db.Column('course_id', db.Integer, db.ForeignKey('course.id')),
                          db.PrimaryKeyConstraint('account_id', 'course_id'))
roles_users = db.Table('roles_users',
                          db.Column('account_id', db.Integer, db.ForeignKey('account.id')),
                          db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
                          db.PrimaryKeyConstraint('account_id', 'role_id'))

