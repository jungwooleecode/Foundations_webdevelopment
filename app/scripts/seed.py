from app.app import create_app
from app.booking.models import Workshop
from app.extensions.database import db
from datetime import datetime

app = create_app()
app.app_context().push()

workshops_data= {
    1 : {
        'date': datetime.fromisoformat('2022-05-20T14:30:00'), 'name': 'Hip-hop choreography', 'teacher':'Honey J', 'price': 15.99, 'fixed_spots': 30, 'available_spots': 30, 'picture_url':'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/lia-1498857451.jpg', 'video_url':'https://www.youtube.com/embed/WnSyWk9sjY0?autoplay=1&mute=1'
    },
    2 : {
        'date': datetime.fromisoformat('2022-05-24T15:30:00'), 'name': 'Commercial choreography', 'teacher':'Monica', 'price': 19.99, 'fixed_spots': 30, 'available_spots': 30, 'picture_url':'https://www.1millionoutfits.com/wp-content/uploads/2015/05/7-mina-myoung-choreography-1million-dance-studio-clothes.jpg', 'video_url':'https://www.youtube.com/embed/8mMGGFGYgYA?autoplay=1&mute=1'
    },
    3 : {
        'date': datetime.fromisoformat('2022-06-03T16:00:00'), 'name': 'Poppin choreography', 'teacher':'Noze', 'price': 10.99, 'fixed_spots': 30, 'available_spots': 30, 'picture_url':'https://i.ytimg.com/vi/eGrvoHIobNc/maxresdefault.jpg', 'video_url':'https://www.youtube.com/embed/r-waF2SXNbI?autoplay=1&mute=1'
    },
    4 : {
        'date': datetime.fromisoformat('2022-06-23T17:30:00'), 'name': 'choreography', 'teacher':'Lia Kim', 'price': 13.99, 'fixed_spots': 30, 'available_spots': 30, 'picture_url':'https://www.1millionoutfits.com/wp-content/uploads/2015/05/7-mina-myoung-choreography-1million-dance-studio-clothes.jpg', 'video_url':'https://www.youtube.com/embed/a53aJIuQ1ck?autoplay=1&mute=1'
    },
    5 : {
        'date': datetime.fromisoformat('2022-06-30T13:30:00'), 'name': 'Modern dance', 'teacher':'Lee Jung', 'price': 14.99, 'fixed_spots': 30, 'available_spots': 30, 'picture_url':'../static/images/workshop.png', 'video_url':'https://www.youtube.com/embed/dZsTdOd0eaU?autoplay=1&mute=1'
    },
    6 : {
        'date': datetime.fromisoformat('2022-07-05T14:30:00'), 'name': 'Heels choreography', 'teacher':'Aiki', 'price': 13.99, 'fixed_spots': 30, 'available_spots': 30, 'picture_url':'https://tmilly.com/wp-content/uploads/2018/03/Thumbnail-Tims-YouTube-1200x675.jpg', 'video_url':'https://www.youtube.com/embed/WnSyWk9sjY0?autoplay=1&mute=1'
    },
    7 : {
        'date': datetime.fromisoformat('2022-07-20T15:00:00'), 'name': 'K-pop choreography', 'teacher':'Rian', 'price': 18.99, 'fixed_spots': 30, 'available_spots': 30, 'picture_url':'https://i.ytimg.com/vi/LVzEm9vO-hM/maxresdefault.jpg', 'video_url':'https://www.youtube.com/embed/8mMGGFGYgYA?autoplay=1&mute=1'
    },
    8 : {
        'date': datetime.fromisoformat('2022-08-01T16:30:00'), 'name': 'Heels choreography', 'teacher':'Alex', 'price': 18.99, 'fixed_spots': 30, 'available_spots': 30, 'picture_url':'https://tmilly.com/wp-content/uploads/2018/03/Thumbnail-Tims-YouTube-1200x675.jpg', 'video_url':'https://www.youtube.com/embed/dZsTdOd0eaU?autoplay=1&mute=1'
    },
    9 : {
        'date': datetime.fromisoformat('2022-08-10T15:00:00'), 'name': 'K-pop choreography', 'teacher':'Rian', 'price': 14.99, 'fixed_spots': 30, 'available_spots': 30, 'picture_url':'https://i.ytimg.com/vi/LVzEm9vO-hM/maxresdefault.jpg', 'video_url':'https://www.youtube.com/embed/8mMGGFGYgYA?autoplay=1&mute=1'
    },
    10 : {
        'date': datetime.fromisoformat('2022-08-20T15:00:00'), 'name': 'Heels choreography', 'teacher':'Lia Kim', 'price': 18.99, 'fixed_spots': 30, 'available_spots': 30, 'picture_url':'../static/images/workshop.png', 'video_url':'https://www.youtube.com/embed/8mMGGFGYgYA?autoplay=1&mute=1'
    },
    11 : {
        'date': datetime.fromisoformat('2022-08-23T15:00:00'), 'name': 'K-pop choreography', 'teacher':'Rian', 'price': 14.99, 'fixed_spots': 30, 'available_spots': 30, 'picture_url':'https://i.ytimg.com/vi/LVzEm9vO-hM/maxresdefault.jpg', 'video_url':'https://www.youtube.com/embed/8mMGGFGYgYA?autoplay=1&mute=1'
    },
    12 : {
        'date': datetime.fromisoformat('2022-09-01T15:00:00'), 'name': 'Poppin choreography', 'teacher':'Lia Kim', 'price': 18.99, 'fixed_spots': 30, 'available_spots': 30, 'picture_url':'../static/images/workshop.png', 'video_url':'https://www.youtube.com/embed/8mMGGFGYgYA?autoplay=1&mute=1'
    },
    13 : {
        'date': datetime.fromisoformat('2022-09-10T15:00:00'), 'name': 'Poppin choreography', 'teacher':'Rian', 'price': 14.99, 'fixed_spots': 30, 'available_spots': 30, 'picture_url':'https://i.ytimg.com/vi/LVzEm9vO-hM/maxresdefault.jpg', 'video_url':'https://www.youtube.com/embed/8mMGGFGYgYA?autoplay=1&mute=1'
    },
    14 : {
        'date': datetime.fromisoformat('2022-09-20T15:00:00'), 'name': 'K-pop choreography', 'teacher':'Lia Kim', 'price': 18.99, 'fixed_spots': 30, 'available_spots': 30, 'picture_url':'https://www.1millionoutfits.com/wp-content/uploads/2015/05/7-mina-myoung-choreography-1million-dance-studio-clothes.jpg', 'video_url':'https://www.youtube.com/embed/8mMGGFGYgYA?autoplay=1&mute=1'
    }

}

for id, workshop in workshops_data.items():
    new_workshop = Workshop(id=id, date=workshop['date'], name=workshop['name'], teacher=workshop['teacher'], price=workshop['price'], fixed_spots=workshop['fixed_spots'], available_spots=workshop['available_spots'], picture_url=workshop['picture_url'], video_url=workshop['video_url'])
    db.session.add(new_workshop)

db.session.commit()