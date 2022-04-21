from flask import Blueprint, render_template
from app import auth
from .models import User

blueprint = Blueprint('auth', __name__)

@blueprint.route('/forgot')
def forgot():
    return render_template('auth/forgot.html')

@blueprint.route('/login')
def login():
    return render_template('auth/login.html')

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