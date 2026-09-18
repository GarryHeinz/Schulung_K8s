import os
from unittest.mock import patch

import pytest

from app import create_app
from app.routes import CARTS


@pytest.fixture(autouse=True)
def mock_env_vars():
    """Set up test environment variables."""
    with patch.dict(
        os.environ,
        {
            "FLASK_SECRET_KEY": "test-secret-key",
            "HOST": "0.0.0.0",
            "PORT": "8080",
        },
    ):
        yield


@pytest.fixture(autouse=True)
def reset_cart_state():
    """Ensure each test starts with a clean cart store."""

    CARTS.clear()
    yield
    CARTS.clear()


@pytest.fixture
def app():
    """Create and configure a test Flask application instance."""
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
            "SECRET_KEY": "test-secret-key",
            "SERVER_NAME": "test.local",  # Required for url_for to work in tests
        }
    )

    # Push an application context
    ctx = app.app_context()
    ctx.push()
    yield app
    ctx.pop()


@pytest.fixture
def client(app):
    """Create a test client for the app."""
    return app.test_client()
