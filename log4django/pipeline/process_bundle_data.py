import json
import copy

from django.utils.dateparse import parse_datetime

from django_gearman_commands import submit_job

from ..models import LogRecord
from ..settings import GERMAN_TASK_NAME


def persist_record_async(data):
    submit_job(GERMAN_TASK_NAME, json.dumps(data))
    return True


def persist_record(data):
    data = copy.copy(data)
    data['timestamp'] = parse_datetime(data['timestamp'])
    LogRecord(**data).save()
    return True
