from django import forms
from .models import Lesson, Comment


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = [
            'number',
            'title',
            'description',
            'script',
            'course',
            'video',
            'materials',
            'homework',
            'additional_materials',
            'is_published',
        ]

        widgets = {
            'number': forms.NumberInput(attrs={
                'class': 'lesson__number',
                'placeholder': '№',
            }),
            'title': forms.TextInput(attrs={
                'class': 'lesson__title',
                'placeholder': 'Nomi',
            }),
            'description': forms.Textarea(attrs={
                'class': 'lesson__description',
                'placeholder': 'Matni'
            }),
            'script': forms.Textarea(attrs={
                'class': 'lesson_script',
                'placeholder': 'Script'
            }),
            'course': forms.Select(attrs={
                'class': 'lesson_course',
            }),
        }



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'text'
        ]

        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-comment__text',
                'placeholder': 'Sining komentariyangiz...'
            })
        }