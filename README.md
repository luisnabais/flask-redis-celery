# Flask-Redis-Celery

#### **Description**
Skeleton Flask app for Redis and Celery use.

#### **Code**
Code tested with Python 3.6.2.

This app is prepared to be used both in Docker containers and manually in your system, with or without a virtual environment. Feel free to use it on any way you like.
Just make sure that:
- REDIS_URL points to correct host in code/config.py (change it to localhost if using locally, or point 'redis' to 127.0.0.1 (or other host) in your hosts file)

#### **Run**
##### Using Docker
docker run -d -ti --name myapp -p 5000:5000 flask-redis-celery

##### Using Docker Compose
docker-compose up -d (don't use -d if you want to run the app in foregound, attached to console)

##### Using Docker Swarm
docker service create --name myapp -p 5000:5000 flask-redis-celery

##### Manually
- if starting manually:
    - make sure all requirements in requirements.txt are installed, with the command 'pip install -r requirements.txt'
    - execute python app.py
