from app.booking.models import Workshop, Userinfo
from datetime import datetime

def test_booking_renders_workshops(client):
  
  new_workshop = Workshop(id=8, date= datetime.fromisoformat('2022-08-05T16:30:00'), name= 'K-pop choreography', teacher='Alex', price= 18.99, fixed_spots= 30, available_spots= 30, picture_url='https://tmilly.com/wp-content/uploads/2018/03/Thumbnail-Tims-YouTube-1200x675.jpg', video_url='https://www.youtube.com/embed/dZsTdOd0eaU?autoplay=1&mute=1')
  new_workshop.save()

  response = client.get('/workshops')
  
  assert b'K-pop choreography' in response.data

def test_get_bookingcomplete_renders(client):
  
  response = client.get('/bookingcomplete/1')
  assert b'Thank you for booking our class!' in response.data

def test_post_bookingcomplete_creates_userinfo(client):
  
  response = client.post('/bookingcomplete/2', data={
    'name':'Jung Woo Lee',
    'workshop_id': 2
  })

  assert Userinfo.query.first() is not None