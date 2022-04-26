from app.app import create_app
from app.auth.models import User
from app.booking.models import Userinfo, Workshop
from app.extensions.database import db
from datetime import datetime

app = create_app()
app.app_context().push()

users_data={
    1000 : {
        'name': 'James', 'email':'james@gmail.com', 'password':'asdfghj'
    },
    1001 : {
        'name': 'Anna', 'email':'anna@gmail.com', 'password':'qwertyu'
    },
    1002 : {
        'name': 'Monica', 'email':'monica@gmail.com', 'password':'zxcvbnm'
    },
    1003 : {
        'name': 'Tom', 'email':'tom@gmail.com', 'password':'lkjhgfd'
    },
    1004 : {
        'name': 'Josh', 'email':'josh@gmail.com', 'password':'poiuytr'
    },
    1005 : {
        'name': 'Noam', 'email':'noam@gmail.com', 'password':'mnbvcxz'
    },
    1006 : {
        'name': 'Alex', 'email':'alex@gmail.com', 'password':'hellofriend'
    }
}

for id, user in users_data.items():
    new_user = User(id=id, name=user['name'], email=user['email'], password=user['password'])
    db.session.add(new_user)

db.session.commit()

workshops_data= {
    0 : {
        'date': datetime.fromisoformat('2022-05-20T14:30:00'), 'name': 'Hip-hop choreography', 'teacher':'Honey J', 'price': 15.99, 'fixed_spots': 30, 'available_spots': 30, 'picture_url':'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/lia-1498857451.jpg', 'video_url':'https://www.youtube.com/embed/WnSyWk9sjY0?autoplay=1&mute=1'
    },
    1 : {
        'date': datetime.fromisoformat('2022-05-24T15:30:00'), 'name': 'Commercial choreography', 'teacher':'Monica', 'price': 19.99, 'fixed_spots': 30, 'available_spots': 30, 'picture_url':'https://www.1millionoutfits.com/wp-content/uploads/2015/05/7-mina-myoung-choreography-1million-dance-studio-clothes.jpg', 'video_url':'https://www.youtube.com/embed/8mMGGFGYgYA?autoplay=1&mute=1'
    },
    2 : {
        'date': datetime.fromisoformat('2022-06-03T16:00:00'), 'name': 'Poppin choreography', 'teacher':'Noze', 'price': 10.99, 'fixed_spots': 30, 'available_spots': 30, 'picture_url':'https://i.ytimg.com/vi/eGrvoHIobNc/maxresdefault.jpg', 'video_url':'https://www.youtube.com/embed/r-waF2SXNbI?autoplay=1&mute=1'
    },
    3 : {
        'date': datetime.fromisoformat('2022-06-23T17:30:00'), 'name': 'choreography', 'teacher':'Lia Kim', 'price': 13.99, 'fixed_spots': 30, 'available_spots': 30, 'picture_url':'https://www.1millionoutfits.com/wp-content/uploads/2015/05/7-mina-myoung-choreography-1million-dance-studio-clothes.jpg', 'video_url':'https://www.youtube.com/embed/a53aJIuQ1ck?autoplay=1&mute=1'
    },
    4 : {
        'date': datetime.fromisoformat('2022-06-30T13:30:00'), 'name': 'Modern dance', 'teacher':'Lee Jung', 'price': 14.99, 'fixed_spots': 30, 'available_spots': 30, 'picture_url':'../static/images/workshop.png', 'video_url':'https://www.youtube.com/embed/dZsTdOd0eaU?autoplay=1&mute=1'
    },
    5 : {
        'date': datetime.fromisoformat('2022-07-05T14:30:00'), 'name': 'Heels choreography', 'teacher':'Aiki', 'price': 13.99, 'fixed_spots': 30, 'available_spots': 30, 'picture_url':'https://tmilly.com/wp-content/uploads/2018/03/Thumbnail-Tims-YouTube-1200x675.jpg', 'video_url':'https://www.youtube.com/embed/WnSyWk9sjY0?autoplay=1&mute=1'
    },
    6 : {
        'date': datetime.fromisoformat('2022-07-20T15:00:00'), 'name': 'K-pop choreography', 'teacher':'Rian', 'price': 18.99, 'fixed_spots': 30, 'available_spots': 30, 'picture_url':'https://i.ytimg.com/vi/LVzEm9vO-hM/maxresdefault.jpg', 'video_url':'https://www.youtube.com/embed/8mMGGFGYgYA?autoplay=1&mute=1'
    },
    7 : {
        'date': datetime.fromisoformat('2022-08-01T16:30:00'), 'name': 'K-pop choreography', 'teacher':'Alex', 'price': 18.99, 'fixed_spots': 30, 'available_spots': 30, 'picture_url':'https://tmilly.com/wp-content/uploads/2018/03/Thumbnail-Tims-YouTube-1200x675.jpg', 'video_url':'https://www.youtube.com/embed/dZsTdOd0eaU?autoplay=1&mute=1'
    }
}

for id, workshop in workshops_data.items():
    new_workshop = Workshop(id=id, date=workshop['date'], name=workshop['name'], teacher=workshop['teacher'], price=workshop['price'], fixed_spots=workshop['fixed_spots'], available_spots=workshop['available_spots'], picture_url=workshop['picture_url'], video_url=workshop['video_url'])
    db.session.add(new_workshop)

db.session.commit()

userinfos_data={
    50 : {
        'name': 'Alex', 'workshop_id': 0
    },
    51 : {
        'name': 'Noam', 'workshop_id': 0
    },
    52 : {
        'name': 'Josh', 'workshop_id': 0
    },
    53 : {
        'name': 'Tom', 'workshop_id': 1
    },
    54 : {
        'name': 'Monica', 'workshop_id': 1
    },
    55 : {
        'name': 'Anna', 'workshop_id': 2
    },
    56 : {
        'name': 'James', 'workshop_id': 2
    }
}

for id, userinfo in userinfos_data.items():
    new_userinfo = Userinfo(id=id, name=userinfo['name'], workshop_id=userinfo['workshop_id'] )
    db.session.add(new_userinfo)

db.session.commit()