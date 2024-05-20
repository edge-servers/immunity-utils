from celery import shared_task

from ..tasks import ImmunityCeleryTask
from .models import ImmunityVersion


@shared_task(base=ImmunityCeleryTask)
def send_usage_metrics(category='Heartbeat'):
    ImmunityVersion.send_usage_metrics(category)
