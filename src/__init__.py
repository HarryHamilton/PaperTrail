import atexit
import os
import logging
from flask import Flask, render_template, make_response, send_from_directory, request, send_file
from src.app import app_blueprint

def create_app(test_config=None):
    """App factory method to share application across tests and production
    :return: configured flask application
    """
    app = Flask(__name__, instance_relative_config=True)
    from src.index.views import index_blueprint
    app.register_blueprint(app_blueprint)
    app.register_blueprint(index_blueprint)

    return app