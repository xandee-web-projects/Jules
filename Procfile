heroku config:set DISABLE_COLLECTSTATIC=1
release: python manage.py migrate
web: gunicorn jfs.wsgi --log-file=-