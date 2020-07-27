import os

from celery import Celery
from flask import Flask
from source.conf import celery_config


def make_celery(app):
    celery = Celery()
    celery.config_from_object(celery_config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


app = Flask(__name__)

app.config["CELERY_BROKER_URL"] = os.environ.get("CELERY_BROKER_URL")
app.config["CELERY_RESULT_URL"] = os.environ.get("CELERY_RESULT_URL")

celery = make_celery(app)
