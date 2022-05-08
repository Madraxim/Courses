from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class CustomUser(AbstractUser):

    photo = models.ImageField(upload_to='photos/', verbose_name='Rasm', blank=True, null=True)
    email = models.EmailField(unique=True, blank=False, null=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Status', blank=True, null=True)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, verbose_name='Kurs', blank=True, null=True)

    def __str__(self):
        return self.username

    @property
    def get_photo_url(self):
        if self.photo:
            url = self.photo.url
        else:
            url = 'https://www.static-contents.youth4work.com/y4w/Images/Users/5810810.png?v=20200620141353'
        return url

    class Meta:
        permissions = [
            ('can_add_user', "Yangi foydalanuuvchi qo'shish")
        ]