import logging

from .formatters import ModelFormatter, GearmanFormatter
from .settings import GERMAN_TASK_NAME


class ModelHandler(logging.Handler):

    def __init__(self, level=logging.NOTSET):
        super(ModelHandler, self).__init__(level)
        self.formatter = ModelFormatter()

    def emit(self, record):
        try:
            self.format(record).save()
        except Exception:
            self.handleError(record)


class GearmanHandler(logging.Handler):

    def __init__(self, level=logging.NOTSET):
        super(GearmanHandler, self).__init__(level)
        self.formatter = GearmanFormatter()

    def emit(self, record):
        from django_gearman_commands import submit_job
        try:
            submit_job(GERMAN_TASK_NAME, self.format(record))
        except Exception:
            self.handleError(record)