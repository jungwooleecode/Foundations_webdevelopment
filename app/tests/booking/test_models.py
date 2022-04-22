from app.extensions.database import db
from app.booking.models import Dance, Level

def test_dance_update(client):
  
    dance = Dance(id=9, first='Monica', second='Honey J', third='Aiki', level_id=4)
    db.session.add(dance)
    db.session.commit()

    dance.first = 'Honey J'
    dance.save()

    updated_dance = Dance.query.filter_by(id=9).first()
    assert updated_dance.first == 'Honey J'

def test_level_update(client):
  
    level = Level(id=7, first='Beginner', second='Advanced', third='Master')
    db.session.add(level)
    db.session.commit()

    level.first = 'Advanced'
    level.save()

    updated_level = Level.query.filter_by(id=7).first()
    assert updated_level.first == 'Advanced'

def test_dance_delete(client):
  
    dance = Dance(id=10, first='Monica', second='Honey J', third='Aiki', level_id=4)
    db.session.add(dance)
    db.session.commit()

    dance.delete()

    deleted_dance = Dance.query.filter_by(id=10).first()
    assert deleted_dance is None

def test_level_delete(client):
  
    level = Level(id=8, first='Beginner', second='Advanced', third='Master')
    db.session.add(level)
    db.session.commit()

    level.delete()

    deleted_level = Level.query.filter_by(id=8).first()
    assert deleted_level is None