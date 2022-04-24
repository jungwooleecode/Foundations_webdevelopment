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


@blueprint.route('/classinfo/<int:id>')
def classinfo(id):
    workshop = Workshop.query.filter_by(id=id).first_or_404()
    return render_template('booking/classInfo.htm',workshop=workshop)

@blueprint.route('/workshops')
def workshops():
    all_workshops=Workshop.query.all()
    return render_template('booking/workshops.htm', workshops=all_workshops)