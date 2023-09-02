from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def mediapath(value):
    return f"{settings.MEDIA_URL}{value}"
