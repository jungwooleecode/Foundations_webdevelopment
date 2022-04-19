from flask import Flask
from . import standard_page, booking, auth
from app.extensions.database import db

def create_app():
    app= Flask(__name__)

    register_extensions(app)
    register_blueprints(app)

    return app

def register_blueprints(app: Flask):
    app.register_blueprint(standard_page.routes.blueprint)
    app.register_blueprint(booking.routes.blueprint)
    app.register_blueprint(auth.routes.blueprint)

def register_extensions(app: Flask):
    db.init_app(app)