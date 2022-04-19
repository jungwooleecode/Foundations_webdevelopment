from flask import Blueprint, render_template
from app import standard_page

blueprint = Blueprint('standard_page', __name__)

@blueprint.route('/')
def index():
    return render_template('standard_page/index.html')

@blueprint.route('/about')
def about():
    return render_template('standard_page/about.htm')