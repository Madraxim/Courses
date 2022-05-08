from modeltranslation.translator import register, TranslationOptions
from .models import Course, Lesson

@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title', 'description')