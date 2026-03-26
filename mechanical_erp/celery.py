import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mechanical_erp.settings')

app = Celery('mechanical_erp')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Periodic task schedule
app.conf.beat_schedule = {
    'check-low-stock-daily': {
        'task': 'inventory.tasks.check_low_stock',
        'schedule': crontab(hour=9, minute=0),  # Run daily at 9 AM
    },
}
