from . import db

class User(db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    expert = db.Column(db.Boolean)
    admin = db.Column(db.Boolean)
    
    
    
    def __repr__(self):
        return f'User {self.username}'