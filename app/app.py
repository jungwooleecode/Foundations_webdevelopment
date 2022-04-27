from flask import Flask
from app import standard_page, booking, auth
from app.extensions.database import db, migrate
from app.extensions.authentication import login_manager

login_manager.login_view = 'auth.get_login'

def create_app():
    app= Flask(__name__)
    app.config.from_object('config')

    register_extensions(app)
    register_blueprints(app)

    return app

def register_blueprints(app: Flask):
    app.register_blueprint(standard_page.routes.blueprint)
    app.register_blueprint(booking.routes.blueprint)
    app.register_blueprint(auth.routes.blueprint)

def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)