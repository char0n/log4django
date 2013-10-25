from django.db.models import Q

from ..models import LogRecord


def _filter_records(request):
    getvars = request.GET
    logrecord_qs = LogRecord.objects.all().select_related('app')
    # Filtering by get params.
    if getvars.get('q'):
        q = getvars.get('q')
        logrecord_qs = logrecord_qs.filter(
            Q(app__name__icontains=q)
            | Q(message__icontains=q)
            | Q(fileName__icontains=q)
            | Q(loggerName__icontains=q)
            | Q(exception_message__icontains=q)
            | Q(request_id__icontains=q)
            | Q(_extra__icontains=q)
        )
    if getvars.get('app'):
        logrecord_qs = logrecord_qs.filter(app_id=getvars.get('app'))
    if getvars.get('logger'):
        logrecord_qs = logrecord_qs.filter(loggerName=getvars.get('logger'))
    if getvars.getlist('level'):
        logrecord_qs = logrecord_qs.filter(level__in=getvars.getlist('level'))
    if getvars.get('from'):
        logrecord_qs = logrecord_qs.filter(timestamp__gte=getvars.get('from'))
    if getvars.get('to'):
        logrecord_qs = logrecord_qs.filter(timestamp__lte=getvars.get('to'))
    return logrecord_qs