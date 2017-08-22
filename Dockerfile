FROM python:3.6.2-alpine3.6
MAINTAINER Luís Nabais "mail@luisnabais.com"

COPY ./code/ /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
