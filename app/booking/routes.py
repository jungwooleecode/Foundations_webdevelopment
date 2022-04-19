from flask import Blueprint, render_template
from app import booking

blueprint = Blueprint('booking', __name__)

@blueprint.route('/book')
def book():
    return render_template('booking/book.html')

@blueprint.route('/bookingcomplete')
def bookingcomplete():
    return render_template('booking/bookingComplete.html')

@blueprint.route('/classinfo')
def classinfo():
    return render_template('booking/classinfo.html')

@blueprint.route('/schedule')
def schedule():
    return render_template('booking/schedule.html')