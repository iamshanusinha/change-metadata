from flask import Flask
from config import Config
from .metadata_views import metadata_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register the blueprint
    app.register_blueprint(metadata_blueprint)

    return app