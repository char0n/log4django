from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.core.cache import cache

from ...models import LogRecord, App
from ...settings import PAGE_SIZE
from ...decorators import authenticate
from .. import _filter_records


class LogRecordList(TemplateView):
    template_name = 'log4django/bootstrap/logrecord/list.html'
    http_method_names = ('get',)

    @method_decorator(authenticate())
    def get(self, request, *args, **kwargs):
        logrecord_qs = _filter_records(request)
        paginator = Paginator(logrecord_qs, PAGE_SIZE)
        page = request.GET.get('page', None)
        try:
            records = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            records = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            records = paginator.page(paginator.num_pages)
        # Getting filtering values.
        apps = App.objects.all()
        try:
            loggers = self.get_loggers_names()
        except NotImplementedError:
            loggers = LogRecord.objects.order_by('loggerName').values('loggerName')
            loggers = set([r['loggerName'] for r in loggers])
            loggers = [{'loggerName': ln} for ln in loggers]
        levels = LogRecord.LEVEL
        return self.render_to_response(dict(
            records=records, apps=apps, loggers=loggers, levels=levels,
            filter_levels=[int(l) for l in request.GET.getlist('level')]
        ))

    @staticmethod
    def get_loggers_names():
        cache_key = 'log4django_loggers_names'
        loggers = cache.get(cache_key)
        if not loggers:
            loggers = list(
                LogRecord.objects.distinct('loggerName').order_by('loggerName').values('loggerName')
            )
            cache.set(cache_key, loggers)
        return loggers



class LogRecordDetail(TemplateView):
    template_name = 'log4django/bootstrap/logrecord/detail.html'
    http_method_names = ('get',)

    @method_decorator(authenticate())
    def get(self, request, logrecord_id=None):
        record = get_object_or_404(LogRecord, pk=logrecord_id)

        related = None
        if record.request_id:
            related = LogRecord.objects.filter(
                Q(request_id=record.request_id)
                & ~Q(pk=record.pk)
            )

        return self.render_to_response(dict(
            record=record, related=related
        ))
