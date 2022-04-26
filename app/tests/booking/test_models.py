from app.extensions.database import db
from app.booking.models import Userinfo, Workshop
from datetime import datetime

def test_workshop_update(client):
  
  workshop = Workshop(id=8, date= datetime.fromisoformat('2022-08-10T14:30:00'), name= 'Commercial choreography', teacher='Jade', price= 15.99, fixed_spots= 30, available_spots= 30, picture_url='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/lia-1498857451.jpg', video_url='https://www.youtube.com/embed/WnSyWk9sjY0?autoplay=1&mute=1')
  db.session.add(workshop)
  db.session.commit()

  workshop.name = 'Commercial choreography'
  workshop.save()

  updated_workshop = Workshop.query.filter_by(id=8).first()
  assert updated_workshop.name == 'Commercial choreography'

def test_userinfo_update(client):
  
  userinfo = Userinfo(id=57, name= 'Dana', workshop_id= 0)
  db.session.add(userinfo)
  db.session.commit()

  userinfo.name = 'Dana'
  userinfo.save()

  updated_userinfo = Userinfo.query.filter_by(id=57).first()
  assert updated_userinfo.name == 'Dana'

def test_workshop_delete(client):
  
  workshop = Workshop(id=8, date= datetime.fromisoformat('2022-08-10T14:30:00'), name= 'Commercial choreography', teacher='Jade', price= 15.99, fixed_spots= 30, available_spots= 30, picture_url='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/lia-1498857451.jpg', video_url='https://www.youtube.com/embed/WnSyWk9sjY0?autoplay=1&mute=1')
  db.session.add(workshop)
  db.session.commit()

  workshop.delete()

  deleted_workshop = Workshop.query.filter_by(id=8).first()
  assert deleted_workshop is None

def test_userinfo_delete(client):
  
  userinfo = Userinfo(id=57, name= 'Dana', workshop_id= 0)
  db.session.add(userinfo)
  db.session.commit()

  userinfo.delete()

  deleted_userinfo = Userinfo.query.filter_by(id=57).first()
  assert deleted_userinfo is None