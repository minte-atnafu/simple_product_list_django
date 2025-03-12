from django import template

register = template.Library()

@register.filter
def rangefilter(value):
    return range(value)
