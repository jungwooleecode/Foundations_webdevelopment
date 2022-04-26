from operator import methodcaller
from flask import Blueprint, render_template, request, current_app
from app import booking
from .models import Workshop, Userinfo

blueprint = Blueprint('booking', __name__)

@blueprint.route('/book/<int:id>')
def book(id):
    workshop = Workshop.query.filter_by(id=id).first_or_404()
    return render_template('booking/book.htm', workshop=workshop)

@blueprint.get('/bookingcomplete')
def get_bookingcomplete():
    return render_template('booking/bookingComplete.html')

@blueprint.post('/bookingcomplete')
def post_bookingcomplete():
    return render_template('booking/bookingComplete.html')


@blueprint.route('/classinfo/<int:id>')
def classinfo(id):
    workshop = Workshop.query.filter_by(id=id).first_or_404()
    return render_template('booking/classInfo.htm',workshop=workshop)

@blueprint.route('/workshops')
def workshops():
    page_number = request.args.get('page', 1, type=int)
    workshops_pagination=Workshop.query.paginate(page_number, current_app.config['WORKSHOPS_PER_PAGE'])
    return render_template('booking/workshops.htm', workshops_pagination=workshops_pagination)