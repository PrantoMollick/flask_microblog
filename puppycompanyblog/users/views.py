# users/views.py
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from puppycompanyblog import db
from puppycompanyblog.models import User, BlogPost
from puppycompanyblog.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from puppycompanyblog.users.picture_handler import addProfilePic

users = Blueprint('users', __name__)


# registration
@users.routes('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password_hash = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for Registration')
        return redirect(url_for('users.login')), 301

    return render_template('register.html', title="Registration", form=form), 200

# Login
@users.route('/login', methods=['GET', 'POST'])
    form = LoginForm

    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash("Login Success!")

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('core.index')

            return redirect(next), 301

    return render_template('login.html', title="Login", form = form), 200







# Logout
@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('core.index')), 301


# upgrade users from
#user list of blog posts
