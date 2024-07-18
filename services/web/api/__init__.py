from flask import Flask
from .config import env
from .swagger import SWAGGER_URL, swagger_ui_blueprint


def create_app(config_class=env):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from .v1 import bp as api_v1

    app.register_blueprint(api_v1, url_prefix="/v1")
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    return app
