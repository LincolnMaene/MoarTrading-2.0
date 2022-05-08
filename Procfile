web: gunicorn less_talking_more_trading.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate