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
        'date': datetime.fromisoformat('2022-05-20'), 'name': 'Hip-hop choreography', 'teacher':'Honey J', 'price': 15.99, 'fixed_spots': 30, 'available_spots': 30
    },
    1 : {
        'date': datetime.fromisoformat('2022-05-24'), 'name': 'Commercial choreography', 'teacher':'Monica', 'price': 19.99, 'fixed_spots': 30, 'available_spots': 30
    },
    2 : {
        'date': datetime.fromisoformat('2022-06-03'), 'name': 'Poppin choreography', 'teacher':'Noze', 'price': 10.99, 'fixed_spots': 30, 'available_spots': 30
    },
    3 : {
        'date': datetime.fromisoformat('2022-06-23'), 'name': 'choreography', 'teacher':'Lia Kim', 'price': 13.99, 'fixed_spots': 30, 'available_spots': 30
    },
    4 : {
        'date': datetime.fromisoformat('2022-06-30'), 'name': 'Modern dance', 'teacher':'Lee Jung', 'price': 14.99, 'fixed_spots': 30, 'available_spots': 30
    },
    5 : {
        'date': datetime.fromisoformat('2022-07-05'), 'name': 'Heels choreography', 'teacher':'Aiki', 'price': 13.99, 'fixed_spots': 30, 'available_spots': 30
    },
    6 : {
        'date': datetime.fromisoformat('2022-07-20'), 'name': 'K-pop choreography', 'teacher':'Rian', 'price': 18.99, 'fixed_spots': 30, 'available_spots': 30
    },
    7 : {
        'date': datetime.fromisoformat('2022-08-01'), 'name': 'K-pop choreography', 'teacher':'Alex', 'price': 18.99, 'fixed_spots': 30, 'available_spots': 30
    }
}

for id, workshop in workshops_data.items():
    new_workshop = Workshop(id=id, date=workshop['date'], name=workshop['name'], teacher=workshop['teacher'], price=workshop['price'], fixed_spots=workshop['fixed_spots'], available_spots=workshop['available_spots'])
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
