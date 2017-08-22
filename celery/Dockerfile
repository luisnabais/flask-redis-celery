FROM python:3.6.2-alpine3.6
MAINTAINER Luís Nabais "mail@luisnabais.com"

ENV REDIS_HOST redis
ENV REDIS_PORT 6379
ENV REDIS_PWD ln_pwd_123

COPY ./code/ /app
WORKDIR /app
RUN pip install -r requirements.txt

RUN sed -i 's/REDIS_HOST/'"${REDIS_HOST}"'/' /app/config.py
RUN sed -i 's/REDIS_PORT/'"${REDIS_PORT}"'/' /app/config.py
RUN sed -i 's/REDIS_PWD/'"${REDIS_PWD}"'/' /app/config.py

CMD ["celery", "worker", "-A", "app.celery", "--loglevel=info"]
