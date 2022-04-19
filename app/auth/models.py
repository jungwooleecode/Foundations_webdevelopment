from app.extensions.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(40), unique=True)
    password=db.Column(db.String(20), unique=True)