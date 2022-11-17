celery -A Test beat -l INFO

celery -A Test worker -l info




# celery -A Test.celery worker --pool=solo -l info
# celery -A Test.celery worker  -l info




# $ celery -A Test beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler