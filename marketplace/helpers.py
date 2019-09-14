from flask import session, redirect, url_for

from .models import User
from . import db


def auth(func):
    def decorated_function(*args, **kwargs):
        key = session.get('key')
        if not key:
            return redirect(url_for('users.login'))

        user = db.session.query(User).filter_by(session_key=key).scalar()
        if not user:
            return redirect(url_for('users.login'))

        return func(user, *args, **kwargs)

    decorated_function.__name__ = func.__name__
    return decorated_function

