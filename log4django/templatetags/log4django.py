import json

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.utils.text import normalize_newlines

from ..models import LogRecord
from ..settings import EXTRA_DATA_INDENT, PAGINATOR_RANGE


register = template.Library()


@register.simple_tag
def level_css_class(level):
    return {
        LogRecord.LEVEL.NOTSET: 'label-default',
        LogRecord.LEVEL.DEBUG: 'label-success',
        LogRecord.LEVEL.INFO: 'label-info',
        LogRecord.LEVEL.WARNING: 'label-warning',
        LogRecord.LEVEL.ERROR: 'label-primary',
        LogRecord.LEVEL.CRITICAL: 'label-danger'
    }[int(level)]


@register.simple_tag
def extra_data(record):
    return json.dumps(record.extra, indent=EXTRA_DATA_INDENT)


@register.inclusion_tag('log4django/bootstrap/templatetags/pagination.html', takes_context=True)
def pagination(context, page):
    if PAGINATOR_RANGE > page.paginator.num_pages:
        range_length = page.paginator.num_pages
    else:
        range_length = PAGINATOR_RANGE
    range_length -= 1
    range_min = max(page.number - (range_length / 2), 1)
    range_max = min(page.number + (range_length / 2), page.paginator.num_pages)
    range_diff = range_max - range_min
    if range_diff < range_length:
        shift = range_length - range_diff
        if range_min - shift > 0:
            range_min -= shift
        else:
            range_max += shift
    page_range = range(range_min, range_max + 1)
    getvars = context['request'].GET.copy()
    getvars.pop('page', None)
    return dict(
        page=page, page_range=page_range, getvars=getvars
    )

@register.filter
@stringfilter
def remove_newlines(text):
    normalized_text = normalize_newlines(text)
    return mark_safe(normalized_text.replace('\n', ' '))
remove_newlines.is_safe = True
