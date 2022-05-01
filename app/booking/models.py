from app.extensions.database import db, CRUDMixin

class Workshop(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(120))
    name = db.Column(db.String(120))
    teacher = db.Column(db.String(150))
    price = db.Column(db.Numeric(100, 2))
    fixed_spots = db.Column(db.Integer)
    available_spots = db.Column(db.Integer)
    picture_url = db.Column(db.String(300))
    video_url= db.Column(db.String(300))
    userinfos = db.relationship('Userinfo', backref='workshop', lazy=True)

    def update_spots(self):
        self.available_spots -= 1
        self.save()

class Userinfo(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    workshop_id= db.Column(db.Integer, db.ForeignKey('workshop.id'))
