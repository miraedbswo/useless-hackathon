from flask import Flask

from config import config


def register_extension(_app: Flask):
    from app import extension
    extension.swag.init_app(_app)
    extension.swag.template = _app.config['SWAGGER_TEMPLATE']
    extension.cors.init_app(_app)
    extension.db.connect(**_app.config['MONGODB_SETTINGS'])


def register_blueprint(_app: Flask):
    from app.view import survey_blueprint
    _app.register_blueprint(survey_blueprint)


def create_app(config_name: str) -> Flask:
    _app = Flask(__name__)
    _app.config.from_object(config[config_name])

    register_extension(_app)
    register_blueprint(_app)

    return _app
