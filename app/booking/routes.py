from flask import Blueprint, render_template
from app import booking
from .models import Dance,Level
import datetime

blueprint = Blueprint('booking', __name__)

@blueprint.route('/book')
def book():
    return render_template('booking/book.htm')




@blueprint.route('/bookingcomplete/')
def bookingcomplete():
    return render_template('booking/bookingComplete.html')




@blueprint.route('/classinfo/<int:number>')
def classinfo(number):
    id=number//10+1
    dance=Dance.query.filter_by(id=id).first_or_404()

    time=number%10

    if time==1:
        strftime='5:30 - 6:50 PM'
    elif time==2:
        strftime='7:30 - 8:50 PM'
    elif time==3:
        strftime='9:30 - 10:50 PM'

    return render_template('booking/classInfo.htm', dance=dance, time=time, strftime=strftime)

@blueprint.route('/schedule')
def schedule():
    x = datetime.datetime.now()
    year= x.year
    month= x.strftime("%b")
    day= x.day

    all_dances=Dance.query.all()
    return render_template('booking/schedule.htm', dances=all_dances, year=year, month=month, day=day)