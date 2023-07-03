from django import template
from django.utils.html import format_html

register = template.Library()


@register.filter(is_safe=True)
def format_job_offer(value):
    formatted_value = f"<div class='job-offer'>{value}</div>"
    return format_html(formatted_value)
