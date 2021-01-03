import uuid
from django.utils import timezone
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    """Management command for push data to influxdb"""

    def handle(self, *args, **options):
        if settings.WORKFLOW_MANAGER_URL is not None:
            task_id = uuid.uuid4().hex
            print(f"pushing {task_id} networks to workflow_manager when {timezone.now()}")
            # Todo
            print(f"pushed {task_id} networks to workflow_manager when {timezone.now()}")
