import os

from flask import Flask

from app.config import Config
from app.routes import init_routes


def create_app():
    app = Flask(__name__)
    app.secret_key = Config.SECRET_KEY

    # Load configuration
    app.config.from_object("app.config.Config")

    # Initialize routes
    init_routes(app)

    return app
