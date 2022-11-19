from flask import Flask

from src.app import app_blueprint


def create_app(test_config=None):
    """App factory method to share application across tests and production
    :return: configured flask application
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = 'ClFWayxSrDQCs95V2vDH'
    from src.index.views import index_blueprint
    app.register_blueprint(app_blueprint)
    app.register_blueprint(index_blueprint)

    return app
