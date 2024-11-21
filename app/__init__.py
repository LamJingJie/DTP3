from flask import Flask
from app.middleware import PrefixMiddleware
from flask_bootstrap import Bootstrap5

application = Flask(__name__)
bootstrap = Bootstrap5(application)


application.wsgi_app = PrefixMiddleware(application.wsgi_app, voc=True)

from app import routes

