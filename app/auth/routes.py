from flask import Blueprint, render_template, request, redirect, url_for, current_app
from app import auth
from .models import User
from .services.create_user import create_user
from werkzeug.security import generate_password_hash, check_password_hash

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
        user = User.query.filter_by(email=request.form.get('email')).first()

        if not user:
            raise Exception('This accound does not exist.')
        elif not check_password_hash(user.password, request.form.get('password')):
            raise Exception('The password is not correct.')
    
        return redirect(url_for('index.standard_page'))
    
    except Exception as error_message:
        error = error_message or 'An error occurred.'
        return render_template('auth/login.html', error=error)

@blueprint.route('/mailbox')
def mailbox():
    return render_template('auth/mailbox.html')

@blueprint.get('/register')
def get_register():
    return render_template('auth/register.html')

@blueprint.post('/register')
def post_register():
    try:
        if request.form.get('password') != request.form.get('password_confirmation'):
            raise Exception('The password confirmation must match.')
        elif User.query.filter_by(email=request.form.get('email')).first():
            raise Exception('This email already exists.')
        elif not all([ request.form.get('name'), request.form.get('email'), request.form.get('password')]):
            raise Exception('Please fill out all the fields.')

        create_user(request.form, generate_password_hash)
        return redirect(url_for('index.standard_page'))

    except Exception as error_message:
        error = error_message or 'An error occurred'
        current_app.logger.info(f'Error creating an order: {error}')
        return render_template('auth/register.html', error=error)

@blueprint.route('/mypage/<int:id>')
def mypage(id):
    user= User.query.filter_by(id=id).first_or_404()
    return render_template('auth/mypage.html', user=user)

@blueprint.route('/reset')
def reset():
    return render_template('auth/reset.html')