from os          import environ
from celery      import Celery
from django.conf import settings

environ.setdefault('DJANGO_SETTINGS_MODULE', 'fampay.settings')
app = Celery("yt_app")

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.task_routes = {
    'yt_app.tasks.*': {'queue': 'poll_yt_feed'},
}

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'YT_FEED_POLLER': {
        'task': 'yt_app.tasks.fetch_data',
        'schedule': settings.REFRESH_FREQUENCY,
        'options': {
            'queue': 'poll_yt_feed',
        }
    },
}
