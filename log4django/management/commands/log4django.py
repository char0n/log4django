import json

from django.db import transaction
from django.conf import settings

from django_gearman_commands import GearmanWorkerBaseCommand

from ...settings import GERMAN_TASK_NAME
from ...pipeline.process_bundle_data import persist_record


class Command(GearmanWorkerBaseCommand):

    @property
    def task_name(self):
        return GERMAN_TASK_NAME

    @transaction.commit_on_success(using=settings.DATABASE_ALIAS_LOGGING)
    def do_job(self, job_data):
        try:
            payload = json.loads(job_data)
            return persist_record(payload)
        except Exception, ex:
            print ex
        return False