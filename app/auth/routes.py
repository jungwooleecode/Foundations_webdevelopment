from flask import Blueprint, render_template, request, current_app
from app import auth
from .models import User
from .services.create_user import create_user

blueprint = Blueprint('auth', __name__)

@blueprint.route('/forgot')
def forgot():
    return render_template('auth/forgot.html')

@blueprint.get('/login')
def get_login():
    return render_template('auth/login.html')

@blueprint.post('/login')
def post_login():
    try:
        if not all([ request.form.get('name'), request.form.get('email'), request.form.get('password')]):
            raise Exception('Please fill out all the fields.')

        create_user(request.form)
        return render_template('auth/login.html')
    except Exception as error_message:
        error = error_message or 'An error occurred'
        current_app.logger.info(f'Error creating an order: {error}')
        return render_template('auth/register.html', error=error)

@blueprint.route('/mailbox')
def mailbox():
    return render_template('auth/mailbox.html')

@blueprint.route('/register')
def register():
    return render_template('auth/register.html')

@blueprint.route('/mypage/<int:id>')
def mypage(id):
    user= User.query.filter_by(id=id).first_or_404()
    return render_template('auth/mypage.html', user=user)

@blueprint.route('/reset')
def reset():
    return render_template('auth/reset.html')