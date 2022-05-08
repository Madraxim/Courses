from django import template
from courses.models import Course
from django.db.models import Count, F

from courses.models import Course, Lesson

register = template.Library()

@register.simple_tag(name='all_courses')
def get_courses_with_lessons():
    courses = Course.objects.annotate(
        total_lessons=Count('lesson', filter=F('lesson__is_published'))
    ).filter(total_lessons__gt=0)
    return courses


@register.simple_tag()
def get_tags():
    info = [
        {
            'link': 'profile',
            'text': 'Profil',
        },
        {
            'link': 'new_lesson',
            'text': 'Dars qoshish',
        },
        {
            'link': 'register',
            'text': 'Foydalanuvchi qoshish'
        },
        {
            'link': 'logout',
            'text': 'Chiqish',
        },
    ]
    return info



@register.simple_tag()
def get_all_lessons_by_course(course_id):
    return Lesson.objects.filter(
        course_id=course_id,
        is_published=True
    ).order_by('number')