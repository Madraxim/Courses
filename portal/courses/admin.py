from django.contrib import admin
from .models import Course, Lesson, Comment
from modeltranslation.admin import TranslationAdmin

# Register your models here.

class LessonAdmin(admin.ModelAdmin):
    list_display = ('course', 'number', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('number', 'title')
    list_editable = ('is_published',)


admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Comment)