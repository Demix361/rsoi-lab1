# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /src/mysite
COPY requirements.txt /src/mysite
RUN pip install -r requirements.txt
COPY . /src/mysite

RUN python ./src/mysite/manage.py makemigrations
RUN python ./src/mysite/manage.py migrate
#RUN python ./src/mysite/manage.py test main --keepdb

CMD python ./src/mysite/manage.py runserver 0.0.0.0:$PORT