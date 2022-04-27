from app.auth.models import User

def create_user(form_data):

    user=User(
        name=form_data.get('name'),
        email=form_data.get('email'),
        password=form_data.get('password')
    )

    user.save()