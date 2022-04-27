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
        current_app.logger.info(f'Error in login: {error}')
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
        current_app.logger.info(f'Error in register: {error}')
        return render_template('auth/register.html', error=error)

@blueprint.get('/mypage/<int:id>')
def get_mypage(id):
    user= User.query.filter_by(id=id).first_or_404()
    return render_template('auth/mypage.html', user=user)

@blueprint.post('/mypage/<int:id>')
def post_mypage(id):
    try:
        user= User.query.filter_by(id=id).first_or_404()

        if request.form.get('email'):
            if User.query.filter_by(email=request.form.get('email')).first():
                raise Exception('This email already exists.')
            else:
                user.email=request.form.get('email')
        if request.form.get('password'):
            user.password=request.form.get('password')
        if request.form.get('name'):
            user.name=request.form.get('name')
             
        user.save()
        return render_template('auth/mypage.html', user=user)

    except Exception as error_message:
        error = error_message or 'An error occurred'
        current_app.logger.info(f'Error in mypage: {error}')
        return render_template('auth/mypage.html', user=user, error=error)


@blueprint.route('/delete/<int:id>')
def delete(id):
    user= User.query.filter_by(id=id).first_or_404()
    user.delete()
    return redirect(url_for('standard_page.index'))
