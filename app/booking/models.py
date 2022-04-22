from app.extensions.database import db


class Dance(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    first:db.Column(db.String(20))
    second:db.Column(db.String(20))
    third:db.Column(db.String(20))
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'))

class Level(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    first:db.Column(db.String(10))
    second:db.Column(db.String(10))
    third:db.Column(db.String(10))
    dance = db.relationship('Dance', backref='level', uselist=False, lazy=True)