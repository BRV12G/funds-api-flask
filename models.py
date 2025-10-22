from . import db
from sqlalchemy.sql import func

class Users(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.string(100), nullable=False)
    lastName = db.Column(db.string(200), nullable=False)
    password = db.Column(db.string(250), nullable=False)
    email = db.Column(db.string(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())


    def __repr__(self): #output in python shell or logs , the __repr__ function.
        return f'<User {self.firstNamee} {self.id}>'


class 

