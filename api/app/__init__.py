from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()


def create_app(config_class=Config):
    api = Flask(__name__)
    api.config.from_object(config_class)

    db.init_app(api)
    migrate.init_app(api)
    login.init_app(api)

    from app.auth import bp as auth_bp
    api.register_blueprint(auth_bp)

    return api
