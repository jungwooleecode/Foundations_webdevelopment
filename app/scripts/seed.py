from app.app import create_app
from app.auth.models import User
from app.booking.models import Dance, Level
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

dances_data={
    1 : {
        'first': 'Monica', 'second':'Monica', 'third':'Honey J', 'level_id':1
    },
    2 : {
        'first': 'Aiki', 'second':'Aiki', 'third':'Monica', 'level_id':2
    },
    3 : {
        'first': 'Monica', 'second':'Monica', 'third':'Honey J', 'level_id':3
    },
    4 : {
        'first': 'Aiki', 'second':'Aiki', 'third':'Monica', 'level_id':4
    },
    5 : {
        'first': 'Honey J', 'second':'Monica', 'third':'Aiki', 'level_id':5
    },
    6 : {
        'first': 'Honey J', 'second':'Monica', 'third':'Aiki', 'level_id':6
    },
    7 : {
        'first': 'Monica', 'second':'Monica', 'third':'Honey J', 'level_id':1
    },
    8 : {
        'first': 'Aiki', 'second':'Aiki', 'third':'Monica', 'level_id':2
    }
}

for id, dance in dances_data.items():
    new_dance = Dance(id=id, first=dance['first'], second=dance['second'], third=dance['third'], level_id=dance['level_id'])
    db.session.add(new_dance)

db.session.commit()

levels_data={
    1 : {
        'first': 'Beginner', 'second':'Advanced', 'third':'Master'
    },
    2 : {
        'first': 'Beginner', 'second':'Master', 'third':'Advanced'
    },
    3 : {
        'first': 'Master', 'second':'Advanced', 'third':'Beginner'
    },
    4 : {
        'first': 'Advanced', 'second':'Beginner', 'third':'Master'
    },
    5 : {
        'first': 'Master', 'second':'Beginner', 'third':'Advanced'
    },
    6 : {
        'first': 'Advanced', 'second':'Master', 'third':'Beginner'
    }
}

for id, level in levels_data.items():
    new_level = Level(id=id, first=level['first'], second=level['second'], third=level['third'])
    db.session.add(new_level)

db.session.commit() 
