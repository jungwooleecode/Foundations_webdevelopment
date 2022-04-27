from app.auth.models import User

def create_user(form_data, generate_password_hash):

    user=User(
        name=form_data.get('name'),
        email=form_data.get('email'),
        password=generate_password_hash(form_data.get('password'))
    )

    user.save()