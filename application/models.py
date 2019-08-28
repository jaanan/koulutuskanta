from application import db

class Base(db.Model):

    __abstract__ = True
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

koulutusmateriaali = db.Table('koulutusmateriaali',
                          db.Column('task.id', db.Integer, db.ForeignKey('task.id')),
                          db.Column('material.id', db.Integer, db.ForeignKey('material.id')),
                          db.PrimaryKeyConstraint('task.id', 'material.id'))
