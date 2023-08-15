from django import template
from datetime import timedelta

register = template.Library()

@register.filter(name='hours_and_minutes')
def hours_and_minutes(value):
    total_minutes = value.total_seconds() // 60
    hours = int(total_minutes // 60)
    minutes = int(total_minutes % 60)
    return f'{hours}h {minutes}m'
