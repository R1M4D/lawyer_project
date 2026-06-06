from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes import register_routes
from extension import db

from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from models import Order


def create_app():
    app = Flask(__name__, template_folder="templates")


    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lawyer_site.db'
    db.init_app(app)

    bcrypt = Bcrypt()

    register_routes(app, db, bcrypt)

    from models import Order

    migrate = Migrate(app, db)

    return app