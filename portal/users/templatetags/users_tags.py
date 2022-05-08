from django import template
from django.contrib.auth.models import Group
from courses.models import Course

register = template.Library()

@register.simple_tag()
def get_data(model):
    if model == 'course':
        objects = Course.objects.all()
    else:
        objects = Group.objects.all()
    return objects