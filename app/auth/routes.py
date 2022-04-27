from flask import Blueprint, render_template, request, redirect, url_for, current_app
from app import auth
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user

blueprint = Blueprint('auth', __name__)

@blueprint.get('/login')
def get_login():
    return render_template('auth/login.html')

@blueprint.post('/login')
def post_login():
    try:
        user = User.query.filter_by(email=request.form.get('email')).first()

        if not user:
            raise Exception('This account does not exist.')
        elif not check_password_hash(user.password, request.form.get('password')):
            raise Exception('The password is not correct.')

        login_user(user)
        return redirect(url_for('standard_page.index'))
    
    except Exception as error_message:
        error = error_message or 'An error occurred.'
        return render_template('auth/login.html', error=error)

@blueprint.get('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.get_login'))

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

        user=User(
        name=request.form.get('name'),
        email=request.form.get('email'),
        password=generate_password_hash(request.form.get('password'))
        )

        user.save()
        
        user = User.query.filter_by(email=request.form.get('email')).first()
        login_user(user)
        return redirect(url_for('standard_page.index'))

    except Exception as error_message:
        error = error_message or 'An error occurred'
        current_app.logger.info(f'Error creating an order: {error}')
        return render_template('auth/register.html', error=error)

@blueprint.route('/mypage/<int:id>')
@login_required
def mypage(id):
    user= User.query.filter_by(id=id).first_or_404()
    return render_template('auth/mypage.html', user=user)
