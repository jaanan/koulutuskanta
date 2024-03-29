from application import db

class Base(db.Model):

    __abstract__ = True
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())


kurssimateriaali = db.Table('kurssimateriaali',
                          db.Column('course.id', db.Integer, db.ForeignKey('course.id')),
                          db.Column('material.id', db.Integer, db.ForeignKey('material.id')),
                          db.PrimaryKeyConstraint('course.id', 'material.id'))

kurssilainen = db.Table('kurssilainen',
                          db.Column('account.id', db.Integer, db.ForeignKey('account.id')),
                          db.Column('course.id', db.Integer, db.ForeignKey('course.id')),
                          db.PrimaryKeyConstraint('account.id', 'course.id'))

