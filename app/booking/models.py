
from app.extensions.database import db, CRUDMixin
from datetime import datetime


class Workshop(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    name = db.Column(db.String(20))
    teacher = db.Column(db.String(50))
    level = db.Column(db.String(20))
    price = db.Column(db.Numeric(20, 2))
    fixed_spots = db.Column(db.Integer)
    spot_id = db.Column(db.Integer, db.ForeignKey('spot.id'))
    userinfos = db.relationship('Userinfo', backref='workshop', lazy=True)
    

class Spot(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    available_spots = db.Column(db.Integer)
    workshop = db.relationship('Workshop', backref='spot', uselist=False, lazy=True)

class Userinfo(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    workshop_id= db.Column(db.Integer, db.ForeignKey('workshop.id'))