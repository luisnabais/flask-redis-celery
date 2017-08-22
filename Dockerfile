FROM python:3.6.2-alpine3.6
MAINTAINER Luís Nabais "mail@luisnabais.com"

COPY ./code/ /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
