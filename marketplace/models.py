import bcrypt

from sqlalchemy.ext.hybrid import hybrid_property

from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    _password = db.Column('password', db.String(100))

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext):
        salt = bcrypt.gensalt(rounds=12)
        self._password = bcrypt.hashpw(plaintext.encode(), salt).decode()

class Listing(db.Model):
    __tablename__ = 'listings'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    description = db.Column(db.Text())