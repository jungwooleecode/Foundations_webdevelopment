from app.extensions.database import db
from app.auth.models import User

def test_user_update(client):
    # updates cookie's properties
    user = User(id=8, name='Aviv', email='avia@gmail.com', password='hihihih')
    db.session.add(user)
    db.session.commit()

    user.name = 'Avia'
    user.save()

    updated_user = User.query.filter_by(id=8).first()
    assert updated_user.name == 'Avia'