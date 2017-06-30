from flask import Flask
from celery import Celery

app = Flask(__name__)
app.config.from_object('config')

from flask_celery import make_celery
celery = make_celery(app)

from app import views
from app import tasks
