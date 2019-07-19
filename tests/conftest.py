import os
import sys

import pytest
from marketplace import create_app
from marketplace import db

sys.path.append(os.path.join(os.path.dirname(__file__), 'helpers'))

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
        'DATABASE': 'marketplace_test',
    })

    yield app

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
