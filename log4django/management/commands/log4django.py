import json

from django.db import transaction
from django.conf import settings

from django_gearman_commands import GearmanWorkerBaseCommand

from ...settings import GERMAN_TASK_NAME, COMMAND_EXCEPTION_CALLBACK
from ...pipeline.process_bundle_data import persist_record
from ...utils import import_string


exception_callback = import_string(COMMAND_EXCEPTION_CALLBACK)


class Command(GearmanWorkerBaseCommand):
    db = settings.DATABASE_ALIAS_LOGGING

    @property
    def task_name(self):
        return GERMAN_TASK_NAME

    def exiting(self):
        try:
            if transaction.is_dirty(using=self.db):
                try:
                    transaction.commit(using=self.db)
                except:
                    transaction.rollback(using=self.db)
        finally:
            transaction.leave_transaction_management(using=self.db)

    def do_job(self, job_data):
        transaction.enter_transaction_management(using=self.db)
        try:
            payload = json.loads(job_data)
            return persist_record(payload)
        except Exception as ex:
            exception_callback(ex, gearman_worker=self.gearman_worker)
        finally:
            self.exiting()

        return False

