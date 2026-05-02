from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from .config import DevelopmentConfig

db = SQLAlchemy()


def create_app(config_object=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    CORS(app, origins=app.config.get("CORS_ORIGINS", "*"))

    from .api import register_routes

    register_routes(app)

    @app.get("/health")
    def health_check():
        return {"status": "ok"}

    return app
