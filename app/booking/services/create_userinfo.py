from app.booking.models import Userinfo

def create_userinfo(form_data, id):
    userinfo = Userinfo(
        name=form_data.get('name'),
        workshop_id=id
    )
    userinfo.save()