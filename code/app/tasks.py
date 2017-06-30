from celery import Celery
from app import app
from app import celery
from flask_redis import FlaskRedis

redis_store = FlaskRedis(app)

@celery.task()
def counter_save():
    result = redis_store.save()
    return "Redis output: " + str(result)

@celery.task()
def counter_reset():
    result_reset = redis_store.set('hello-world-view-count', 0)
    result_save = redis_store.save()
    return "Redis output: " + str(result_reset)

