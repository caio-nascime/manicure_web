from flask import Flask
from app.config import configs

from app.routes import health_checks



def create_app(config = "desenvolvimento"):

    app = Flask(__name__)

    classe_config = configs[config]
    app.config.from_object(classe_config)

    app.register_blueprint(health_checks.health_checks_bp)

    return app



    