from . import db

class User(db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    expert = db.Column(db.Boolean)
    admin = db.Column(db.Boolean)
    questions_asked = db.relationship('questions_asked_by_id',backref = 'asker',lazy="dynamic")
    answers_requested = db.relationship('answers_requested',backref = 'expert',lazy="dynamic")
    
    
    
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.Text) 
    answer = db.Column(db.Text)
    asked_by_id = db.Column(db.Integer, db.ForeignKey('user.id')),
    expert_id = db.Column(db.Integer, db.ForeignKey('user.id')),
    
    
    def __repr__(self):
        return f'User {self.username}'