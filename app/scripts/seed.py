from app.app import create_app
from app.auth.models import User
from app.booking.models import Userinfo, Spot, Workshop
from app.extensions.database import db

app = create_app()
app.app_context().push()

users_data={
    1 : {
        'name': 'James', 'email':'james@gmail.com', 'password':'asdfghj'
    },
    2 : {
        'name': 'Anna', 'email':'anna@gmail.com', 'password':'qwertyu'
    },
    3 : {
        'name': 'Monica', 'email':'monica@gmail.com', 'password':'zxcvbnm'
    },
    4 : {
        'name': 'Tom', 'email':'tom@gmail.com', 'password':'lkjhgfd'
    },
    5 : {
        'name': 'Josh', 'email':'josh@gmail.com', 'password':'poiuytr'
    },
    6 : {
        'name': 'Noam', 'email':'noam@gmail.com', 'password':'mnbvcxz'
    },
    7 : {
        'name': 'Alex', 'email':'alex@gmail.com', 'password':'hellofriend'
    }
}

for id, user in users_data.items():
    new_user = User(id=id, name=user['name'], email=user['email'], password=user['password'])
    db.session.add(new_user)

db.session.commit()


