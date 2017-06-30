from app import app
from . import tasks
from flask_redis import FlaskRedis

redis_store = FlaskRedis(app)

@app.route('/')
def hello_world():
    redis_store.set('hello-world-msg', 'Hello from Flask-Redis-Celery')
    view_count = redis_store.incr('hello-world-view-count')

    msg = redis_store.get('hello-world-msg').decode("utf-8")

    return msg + '.<br /><br />This page has been seen ' + str(view_count) + ' times.'

@app.route('/save_counter')
def counter_save():
    tasks.counter_save.delay()

    return 'Sent an async request to Celery, to order Redis to SAVE data to disk.'

@app.route('/reset_counter')
def counter_reset():
    tasks.counter_reset.delay()

    return 'Sent an async request to Celery, to order Redis to RESET data to disk.'

