from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.middleware import PrefixMiddleware
from config import Config

application = Flask(__name__)
bootstrap = Bootstrap5(application)
# Database
application.config.from_object(Config)
db = SQLAlchemy(application)
migrate = Migrate(application, db)

# For vocareum
application.wsgi_app = PrefixMiddleware(application.wsgi_app, voc=True)

from app import routes, models

