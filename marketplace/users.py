from base64 import b64encode

import bcrypt
from flask import Blueprint, request, render_template, session, url_for, redirect

from . import db
from .helpers import auth
from .models import User

bp = Blueprint('users', __name__, url_prefix='/user')


@bp.route('/signup', methods=('GET', 'POST'))
def sign_up():
    if request.method == 'POST':
        user = User(
            full_name=request.form['full_name'],
            email=request.form['email'],
            password=request.form['password'],
        )
        db.session.add(user)
        db.session.commit()

        return render_template('users/signup_success.html', user=user)
    return render_template('users/signup.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    error = None
    if request.method == 'POST':
        error = "The email hasn't been registered."
        u = db.session.query(User).filter(User.email == request.form['email']).scalar()
        if u:
            error = "Invalid password."
            password = request.form['password']
            if bcrypt.checkpw(password.encode(), u.password.encode()):
                session['logged_in'] = True
                return redirect(url_for('users.welcome'))

    return render_template('users/login.html', error=error)


@bp.route('/welcome', methods=('GET',))
@auth
def welcome():
    return render_template('users/welcome.html')
