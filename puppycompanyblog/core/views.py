# core/views.py
from flask import render_template, request, Blueprint

core = Blueprint('core', __name__)

@core.route('/')
def index():
    # More come
    return render_template('index.html'), 200

@core.route('/info')
def info():

    return render_template('info.html'), 200
