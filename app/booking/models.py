
from app.extensions.database import db, CRUDMixin
from datetime import datetime


class Workshop(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    name = db.Column(db.String(20))
    teacher = db.Column(db.String(50))
    price = db.Column(db.Numeric(20, 2))
    fixed_spots = db.Column(db.Integer)
    available_spots = db.Column(db.Integer)
    userinfos = db.relationship('Userinfo', backref='workshop', lazy=True)
    picture_url = db.Column(db.String(260))

class Userinfo(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    workshop_id= db.Column(db.Integer, db.ForeignKey('workshop.id'))