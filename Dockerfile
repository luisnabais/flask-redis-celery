FROM python:3.6.1-alpine
MAINTAINER Luís Nabais "mail@luisnabais.com"

COPY ./code/ /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
