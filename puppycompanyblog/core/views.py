# core/views.py
from flask import render_template, request, Blueprint
from puppycompanyblog.models import BlogPost

core = Blueprint('core', __name__)

@core.route('/')
def index():
    # More come
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
    print(blog_posts.__dict__)
    return render_template('index.html', blog_posts=blog_posts), 200

@core.route('/info')
def info():

    return render_template('info.html'), 200
