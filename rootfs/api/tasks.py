# Create your tasks here
import time
import uuid
import logging
from datetime import timedelta
from typing import List, Dict
from django.core import signals
from django.utils.timezone import now
from celery import shared_task
from api.models.resource import Resource

logger = logging.getLogger(__name__)


@shared_task
def retrieve_resource(resource):
    task_id = uuid.uuid4().hex
    signals.request_started.send(sender=task_id)
    try:
        if not resource.retrieve():
            t = time.time() - resource.created.timestamp()
            if t < 3600:
                retrieve_resource.apply_async(
                    args=(resource, ),
                    eta=now() + timedelta(seconds=30))
            elif t < 3600 * 12:
                retrieve_resource.apply_async(
                    args=(resource, ),
                    eta=now() + timedelta(seconds=1800))
            else:
                resource.detach_resource()
    except Resource.DoesNotExist:
        logger.info("retrieve task not found resource: {}".format(resource.id))  # noqa
    finally:
        signals.request_finished.send(sender=task_id)


@shared_task
def measure_config(*config: List[Dict[str, str]]):
    """
    [
        {
            "user": "test",
            "type": "task",
            "namespace":  "test",
            "cpu": "1",
            "memory": "2G",
            "timestamp": 1609231998.9103732
        }
    ]
    """
    task_id = uuid.uuid4().hex
    signals.request_started.send(sender=task_id)
    try:
        pass
    except Exception as e:
        logger.info("write influxdb point fail: {}".format(e))
    finally:
        signals.request_finished.send(sender=task_id)


@shared_task
def measure_volumes(*volumes: List[Dict[str, str]]):
    """
    [
        {
            "user": "test",
            "name": "disk",
            "namespace": "test",
            "size": "100G",
            "timestamp": "1609231998.9103732"
        }
    ]
    """
    task_id = uuid.uuid4().hex
    signals.request_started.send(sender=task_id)
    try:
        pass
    except Exception as e:
        logger.info("write influxdb point fail: {}".format(e))
    finally:
        signals.request_finished.send(sender=task_id)


@shared_task
def measure_networks(*networks: List[Dict[str, str]]):
    """
    [
        {
            "user": "test",
            "type": "web",
            "namespace":  "test",
            "rx_bytes": "10000",
            "tx_bytes": "200000",
            "timestamp": "1609231998.9103732"
        }
    ]
    """
    task_id = uuid.uuid4().hex
    signals.request_started.send(sender=task_id)
    try:
        pass
    except Exception as e:
        logger.info("write influxdb point fail: {}".format(e))
    finally:
        signals.request_finished.send(sender=task_id)


@shared_task
def measure_resources(*resources: List[Dict[str, str]]):
    """
    workflow_manager_url + measurements/resources
    [
        {
            "user": "test1",
            "name": "redis",
            "plan": "redis:small",
            "namespace": "test",
            "timestamp": "1609231998.9103732"
        }
    ]
    """
    task_id = uuid.uuid4().hex
    signals.request_started.send(sender=task_id)
    try:
        pass
    except Exception as e:
        logger.info("write influxdb point fail: {}".format(e))
    finally:
        signals.request_finished.send(sender=task_id)
