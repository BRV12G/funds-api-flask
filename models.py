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
    funds = db.relationship('Funds', backref='user')

)

    def __repr__(self): #output in python shell or logs , the __repr__ function.
        return f'<User {self.firstNamee} {self.id}>'


class Funds(db.Model):
    __tablename__ = "Funds"
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('Users.id'))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    # name = db.Column(db.string(100), nullable=False)

    @property #
    def serialize(self): # serialize converts the SQLAlchemy object → Python dictionary → JSON-friendly.

        return {
            'id': self.id,
            'amount': self.amount,
            'created_at': self.created_at,
        }

