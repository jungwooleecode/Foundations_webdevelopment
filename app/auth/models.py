from app.extensions.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email=db.Column(db.String(40), unique=True)
    password=db.Column(db.String(20), unique=True)