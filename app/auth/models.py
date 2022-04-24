from app.extensions.database import db, CRUDMixin

class User(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email=db.Column(db.String(40))
    password=db.Column(db.String(20))