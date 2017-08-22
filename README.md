# Flask-Redis-Celery

#### **Description**
Basic Flask app structure for integration with Redis and Celery.

Flask-Redis-Celery is divided in 3 microservices:
- Flask is a Python Web Framework. Is the base webapp. (http://flask.pocoo.org)
- Celery is an background asynchronous task service. (http://www.celeryproject.org)
- Redis is in-memory data structure store, which can be used as a database, cache and message broker. Default Redis installation (password-protected)

This app is prepared to be used both in Docker containers and manually in your system, with or without a virtual environment. Feel free to use it on any way you like.
Just make sure that:
- REDIS variables point to correct host/port/pass in code/config.py

Code tested with Python 3.6.2.


#### **Run**
##### Using Docker
```
$ docker network create mynet
$ docker run -d -ti --name redis -v redis-data:/data -p 6379:6379 --network mynet redis:4.0.1-alpine redis-server --requirepass 'ln_pwd_123'
$ docker run -d -ti --name myapp_celery -e REDIS_HOST=redis -e REDIS_PORT=6379 -e REDIS_PWD=ln_pwd_123 --network mynet luisnabais/celery-redis
$ docker run -d -ti --name myapp_flask -e REDIS_HOST=redis -e REDIS_PORT=6379 -e REDIS_PWD=ln_pwd_123 --network mynet -p 5000:5000 luisnabais/flask-redis
```

##### Using Docker Compose
```
$ docker-compose up -d -e REDIS_HOST=redis -e REDIS_PORT=6379 -e REDIS_PWD=ln_pwd_123
```

##### Using Docker Swarm
```
$ docker network create --driver overlay mynet
$ docker service create --name redis --network mynet redis redis-server --requirepass 'ln_pwd_123'
$ docker service create --name myapp_celery -e REDIS_HOST=redis -e REDIS_PORT=6379 -e REDIS_PWD=ln_pwd_123 --network mynet luisnabais/celery-redis
$ docker service create --name myapp_flask -e REDIS_HOST=redis -e REDIS_PORT=6379 -e REDIS_PWD=ln_pwd_123 --network mynet -p 5000:5000 luisnabais/flask-redis
```

##### Manually
Make sure all Python requirements in requirements.txt are installed.
If you use pip, you can do that with the command 'pip install -r requirements.txt'.

Start Redis.
Start Celery: execute 'celery worker -A app.celery --loglevel=info'
Start Flask: execute 'python app.py'
