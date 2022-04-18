from flask import Flask, render_template
from . import standard_page

def create_app():
    app= Flask(__name__)

    register_blueprints(app)
    return app

def register_blueprints(app: Flask):
    app.register_blueprint(standard_page.routes.blueprint)
    app.register_blueprint(booking.routes.blueprint)
    app.register_blueprint(auth.routes.blueprint)



