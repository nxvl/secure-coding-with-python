import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='postgresql:///marketplace',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import models
    db.init_app(app)
    migrate.init_app(app, db)

    from . import listings
    app.register_blueprint(listings.bp)

    return app