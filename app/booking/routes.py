from flask import Blueprint, render_template, request, current_app
from app import booking
from .models import Workshop, Userinfo
from .services.create_userinfo import create_userinfo
from flask_login import login_required

blueprint = Blueprint('booking', __name__)

@blueprint.get('/book/<int:id>')
@login_required
def get_book(id):
    workshop = Workshop.query.filter_by(id=id).first_or_404()
    return render_template('booking/book.htm', workshop=workshop)

@blueprint.post('/book/<int:id>')
def post_book(id):
    try:
        workshop = Workshop.query.filter_by(id=id).first_or_404()
        if not all([ request.form.get('name'), request.form.get('payment')]):
            raise Exception('Please fill out all the fields.')
        
        create_userinfo(request.form, id)

        workshop.available_spots=workshop.available_spots-1
        workshop.save()
        
        payment_method=request.form['payment']
        return render_template('booking/bookingComplete.html', payment_method=payment_method)

    except Exception as error_message:
        error = error_message or 'An error occurred'
        current_app.logger.info(f'Error in booking: {error}')
        return render_template('booking/book.htm', workshop=workshop, error=error)

@blueprint.route('/bookingcomplete')
def bookingcomplete():
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