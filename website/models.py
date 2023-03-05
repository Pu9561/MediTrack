from . import db
from flask_login import UserMixin

class Medications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prescrip = db.Column(db.String(150))
    pillperserve = db.Column(db.Integer)
    numperbottle = db.Column(db.Integer)
    dateyear = db.Column(db.String(4))
    datemonth = db.Column(db.String(2))
    dateday = db.Column(db.String(2))
    frequency = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    birthdate = db.Column(db.String(10))
    gender = db.Column(db.String(10))
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    medicine = db.relationship('Medications')
