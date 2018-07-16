from django import template

register = template.Library()


@register.filter(name='find_mean')
def find_mean(value):
    return round(sum(value) / float(len(value)), 2) if value else 0.0


@register.filter(name='find_max')
def find_max(value):
    return round(max(value), 2) if value else 0.0


@register.filter(name='find_min')
def find_min(value):
    return round(min(value), 2)  if value else 0.0
