# -*- coding: utf-8 -*-
import logging
import sys

from flask import Flask
from flask_cors import CORS

from source import models
from source.API.publication import publication_blueprint
from source.conf.extensions import bcrypt, jwt_security, db, migrate

app = Flask(__name__)


def create_app(config_object="source.conf.settings.DevelopmentConfig"):
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_shellcontext(app)
    configure_logger(app)

    @app.route('/')
    def healthcheck():
        return "CMS microservice"

    return app


def register_extensions(app):
    bcrypt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    jwt_security.init_app(app)

    return None


def register_blueprints(app):
    app.register_blueprint(publication_blueprint)

    return None


def register_shellcontext(app):
    def shell_context():
        return {
            "db": db,
            "Publication": models.publication.Publication
        }

    app.shell_context_processor(shell_context)


def configure_logger(app):
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)
