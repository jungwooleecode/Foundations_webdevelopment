from app.extensions.database import db
from app.auth.models import User

def test_user_update(client):
    
    user = User(id=8, name='Aviv', email='avia@gmail.com', password='hihihih')
    db.session.add(user)
    db.session.commit()

    user.name = 'Avia'
    user.save()

    updated_user = User.query.filter_by(id=8).first()
    assert updated_user.name == 'Avia'

def test_user_delete(client):
   
    user = User(id=9, name='Maher', email='maher@gmail.com', password='makemake')
    db.session.add(user)
    db.session.commit()

    user.delete()

    deleted_user = User.query.filter_by(id=9).first()
    assert deleted_user is None