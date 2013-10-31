import logging
from datetime import datetime

from django.utils.timezone import make_aware, get_default_timezone
from django.conf import settings as django_settings


import jsonpickle

from .settings import DEFAULT_APP_ID

LogRecord = None


class BaseFormatter(logging.Formatter):

    DEFAULT_PROPERTIES = logging.LogRecord('', '', '', '', '', '', '', '').__dict__.keys()

    def _get_extra(self, record):
        """Standard record decorated with extra contextual information."""
        extra = {}
        contextual_extra = set(record.__dict__).difference(set(self.DEFAULT_PROPERTIES))

        try:
            contextual_extra.remove('message')
            contextual_extra.remove('asctime')
        except KeyError:
            pass

        for key in contextual_extra:
            extra[key] = getattr(record, key)
        return extra

    def _get_data(self, record):
        timestamp = datetime.fromtimestamp(record.created)
        if django_settings.USE_TZ:
            timestamp = make_aware(timestamp, get_default_timezone())

        return dict(
            loggerName=record.name, level=record.levelno, timestamp=timestamp,
            message=record.getMessage(), fileName=record.pathname, lineNumber=record.lineno,
            thread=record.thread, app_id=getattr(record, 'app_id', DEFAULT_APP_ID),
            request_id=record.request_id
        )


class ModelFormatter(BaseFormatter):

    def format(self, record):
        # Lazy models imports.
        global LogRecord
        if LogRecord is None:
            from .models import LogRecord

        # Basic record data.
        log_record = LogRecord(**self._get_data(record))

        # Exception data if available.
        if record.exc_info is not None:
            log_record.exception_message = str(record.exc_info[1])
            log_record.exception_traceback = self.formatException(record.exc_info)
        # Extra data.
        log_record.extra = self._get_extra(record)
        return log_record


class GearmanFormatter(BaseFormatter):

    def format(self, record):
        # Basic record data.
        record_dict = self._get_data(record)
        
        # Exception data if available.
        if record.exc_info is not None:
            record_dict['exception_message'] = str(record.exc_info[1])
            record_dict['exception_traceback'] = self.formatException(record.exc_info)
        # Extra data.
        record_dict['extra'] = self._get_extra(record)
        record_dict['timestamp'] = record_dict['timestamp'].isoformat()

        return jsonpickle.encode(record_dict)