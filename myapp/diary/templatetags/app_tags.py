from django import template
from django.utils import timezone
from ..models import Diary

register = template.Library()


@register.inclusion_tag('templates/includes/month_links.html')
def render_month_links():
    return {
        'dates': Diary.objects.published().dates('created_date', 'month', order='DESC'),
    }
