from flask import render_template, redirect, request, url_for
from app import application


@application.route('/')
@application.route('/home/')
def home():
    prefix_voc = application.wsgi_app.prefix[:-1]
    return render_template('/home.html', title='Home', prefix=prefix_voc)
