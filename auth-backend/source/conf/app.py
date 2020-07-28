# -*- coding: utf-8 -*-
import logging
import subprocess
import sys

from flask import Flask
from flask_cors import CORS
from source import models
from source.API.auth import auth_blueprint
from source.API.bot import bot_blueprint
from source.API.user import user_blueprint
from source.conf.extensions import bcrypt, db, jwt_security, migrate

app = Flask(__name__)


def create_app(config_object="source.conf.settings.DevelopmentConfig"):
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_shellcontext(app)
    configure_logger(app)

    # Creates a fucking infinite loop
    # OF COURSE
    # TODO: stop being an idiot
    # migrate_db()

    @app.route("/")
    def healthcheck():
        return "Auth microservice"

    return app


def migrate_db():
    subprocess.run(["flask", "db", "upgrade"])


def register_extensions(app):
    bcrypt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    jwt_security.init_app(app)

    return None


def register_blueprints(app):
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(bot_blueprint)
    return None


def register_shellcontext(app):
    # Add models here
    def shell_context():
        return {"db": db, "User": models.user.User}

    app.shell_context_processor(shell_context)


def configure_logger(app):
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)
