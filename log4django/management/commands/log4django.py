import json

from django.utils.dateparse import parse_datetime
from django.db import transaction
from django.conf import settings

from django_gearman_commands import GearmanWorkerBaseCommand

from ...settings import GERMAN_TASK_NAME
from ...models import LogRecord
from ...pipeline.process_bundle_data import persist_record


class Command(GearmanWorkerBaseCommand):

    @property
    def task_name(self):
        return GERMAN_TASK_NAME

    def do_job(self, job_data):
        try:
            payload = json.loads(job_data)
            return persist_record(payload)
        except Exception, ex:
            print ex
        finally:
            transaction.commit(using=settings.DATABASE_ALIAS_LOGGING)
        return True