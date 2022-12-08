FROM python:3.10
WORKDIR /
COPY ./.env.prod /.env
COPY ./.flaskenv /.flaskenv
COPY ./requirements.txt /requirements.txt
COPY ./app /app
EXPOSE 5000
RUN pip --no-cache-dir install -r /requirements.txt
CMD ["/bin/sh","-c", "gunicorn -w 4 -b=0.0.0.0:5000 app.wsgi:app"]
