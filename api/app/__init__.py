from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

api = Flask(__name__)
api.config.from_object(Config)
db = SQLAlchemy(api)
migrate = Migrate(api, db)
login = LoginManager(api)

from app import routes, models
