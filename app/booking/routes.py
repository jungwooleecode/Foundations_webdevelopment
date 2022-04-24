from flask import Blueprint, render_template
from app import booking
from .models import Workshop, Userinfo

blueprint = Blueprint('booking', __name__)

@blueprint.route('/book')
def book():
    return render_template('booking/book.htm')


@blueprint.route('/bookingcomplete')
def bookingcomplete():
    return render_template('booking/bookingComplete.html')


@blueprint.route('/classinfo')
def classinfo():
    return render_template('booking/classInfo.htm')

@blueprint.route('/workshops')
def workshops():
    
    return render_template('booking/workshops.htm')