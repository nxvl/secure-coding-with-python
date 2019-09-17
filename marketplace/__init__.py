import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect


db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='postgresql:///marketplace',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        WTF_CSRF_SECRET_KEY='CSRF_SUP3R_S3CUR3_K3Y',
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import models
    db.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db)

    from . import listings, users, api
    app.register_blueprint(listings.bp)
    app.register_blueprint(users.bp)
    app.register_blueprint(api.bp)

    return app
