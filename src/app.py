import os
import sys

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix

db = SQLAlchemy()
cors = CORS()

sys.path.append("/usr/src/app/src")  # without this tests don't run properly
from apis import api  # this needs to be after db, circular import issues


def create_app(script_info=None):

    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)  # To fix Swagger for HTTPS

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)
    app.config["MAX_CONTENT_LENGTH"] = (
        1024 * 1024
    )  # Only 1MB files (kind of a security for the uploads)

    db.init_app(app)
    cors.init_app(app, resources={r"*": {"origins": "*"}})
    api.init_app(app)

    # shell context for flask cli

    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
