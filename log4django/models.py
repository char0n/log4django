import uuid
import logging
import json

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices


logger = logging.getLogger(__file__)


class LogRecord(models.Model):
    LEVEL = Choices(
        (logging.NOTSET, 'NOTSET', _('NOTSET')),
        (logging.DEBUG, 'DEBUG', _('DEBUG')),
        (logging.INFO, 'INFO', _('INFO')),
        (logging.WARNING, 'WARNING', _('WARNING')),
        (logging.ERROR, 'ERROR', _('ERROR')),
        (logging.CRITICAL, 'CRITICAL', _('CRITICAL'))
    )

    app = models.ForeignKey('App', related_name='records')
    loggerName = models.CharField(max_length=225)
    level = models.PositiveSmallIntegerField(choices=LEVEL, default=LEVEL.NOTSET)
    timestamp = models.DateTimeField()
    message = models.TextField()
    fileName = models.TextField()
    lineNumber = models.PositiveIntegerField(null=True)
    thread = models.CharField(max_length=225, blank=True, null=True)
    exception_message = models.TextField(blank=True, null=True)
    exception_traceback = models.TextField(blank=True, null=True)
    request_id = models.CharField(max_length=36, db_index=True, blank=True, null=True)
    _extra = models.TextField(default='{}')

    @property
    def has_extra(self):
        return self._extra != LogRecord._meta.get_field('_extra').default

    @property
    def extra(self):
        try:
            return json.loads(self._extra)
        except ValueError:
            logger.error('Error while loading JSON:\n{0}'.format(self._extra))

    @extra.setter
    def extra(self, data):
        self._extra = json.dumps(data)

    def __unicode__(self):
        return self.message

    class Meta:
        ordering = ('-id',)


class App(models.Model):
    key = models.CharField(unique=True, max_length=36, default=lambda: str(uuid.uuid4()))
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
