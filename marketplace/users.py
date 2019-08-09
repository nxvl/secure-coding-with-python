from flask import Blueprint, request, render_template

from . import db
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