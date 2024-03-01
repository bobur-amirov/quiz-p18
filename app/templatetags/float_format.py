from django import template

register = template.Library()

@register.filter
def float_format(value, precision=2):
    return round(value, precision)