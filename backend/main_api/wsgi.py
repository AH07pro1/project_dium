"""
WSGI config for main_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from apscheduler.schedulers.background import BackgroundScheduler
from main_api.cron import my_cron_job

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_api.settings')

application = get_wsgi_application()

scheduler = BackgroundScheduler()
scheduler.add_job(my_cron_job, 'cron', hour=14, minute=29)
scheduler.start()


