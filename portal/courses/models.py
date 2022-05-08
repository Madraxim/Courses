from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.
from django.urls import reverse
from .utils import *


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name='Nomi', unique=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Courses(pk={self.pk}, title={self.title})"

    def get_absolute_url(self):
        return reverse('lessons_list_by_course', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Kurs'
        verbose_name_plural = 'Kurslar'


class Lesson(models.Model):

    number = models.PositiveIntegerField(verbose_name='Nomer', help_text='Dars nomerini korsating')
    title = models.CharField(verbose_name='Tema', max_length=255)
    description = models.TextField(verbose_name='Tavsifi')
    script = models.TextField(verbose_name='Script', blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Kurs')

    video = models.FileField(upload_to=save_video, verbose_name='Video',
                             validators=[FileExtensionValidator(allowed_extensions=['mp4'])])

    materials = models.FileField(upload_to=save_materials, verbose_name='Materiallar', blank=True,
                                 validators=[FileExtensionValidator(allowed_extensions=['zip'])])

    homework = models.FileField(upload_to=save_homework, verbose_name='Uy ishi', blank=True,
                                validators=[FileExtensionValidator(allowed_extensions=['zip'])])

    additional_materials = models.FileField(upload_to=save_additional_materials, verbose_name='Qoshimcha material', blank=True,
                                            validators=[FileExtensionValidator(allowed_extensions=['zip'])])


    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yuklangan vaqti')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Ozgartirilgan vaqti')
    is_published = models.BooleanField(default=True, verbose_name='Yuklash')

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return f"Lesson(pk={self.pk}, course='{self.course}', number={self.number})"

    def get_absolute_url(self):
        return reverse('lesson_detail', kwargs={'course_id': self.course.pk, 'pk': self.pk})

    def get_update_url(self):
        return reverse('lesson_update', kwargs={'course_id': self.course.pk, 'pk': self.pk})

    def get_delete_url(self):
        return reverse('lesson_delete', kwargs={'course_id': self.course.pk, 'pk': self.pk})

    def get_comment_url(self):
        return reverse('comment_list', kwargs={'lesson_id': self.pk})

    class Meta:
        verbose_name = 'Dars'
        verbose_name_plural = 'Darslar'
        ordering = ['-created_at']
        unique_together = ('number', 'course')
        permissions = [
            ('can_view_all_lessons', 'Barcha darslarni korish'),
            ('can_view_lessons_by_course', 'Faqat kursni korish'),
            ('can_add_lesson', 'Dars qoshish'),
            ('can_update_lesson', 'Darsni ozgartirish'),
            ('can_delete_lesson', 'Darsni ochirish'),
        ]



from django.contrib.auth.models import User
class Comment(models.Model):

    text = models.TextField(verbose_name='Kommentariya')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Dars')
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, verbose_name='Avtor')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Vaqti')

    def __str__(self):
        return f"{self.pk} - {self.created_at}"

    class Meta:
        verbose_name = 'Komentariya'
        verbose_name_plural = 'Komentariyalar'
        ordering = ['-created_at']