from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView
from django.contrib import messages

from .models import Course, Lesson, Comment
from .forms import LessonForm, CommentForm

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin



# Create your views here.

class LessonsList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    paginate_by = 3
    model = Lesson
    context_object_name = 'lessons'
    extra_context = {
        'title': 'Barcha darslar',
        'nav_title': 'Kurslar',
    }
    permission_required = 'courses.can_view_all_lessons'

    def get_queryset(self):
        return Lesson.objects.filter(is_published=True)

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('login')
        else:
            return redirect('lessons_list_by_course', self.request.user.course.pk)


class LessonsListByCourse(LessonsList):

    # allow_empty = False
    permission_required = 'courses.can_view_lessons_by_course'

    def get(self, *args, **kwargs):
        if not self.request.user.is_superuser and self.kwargs['pk'] != self.request.user.course.pk:
            return redirect('lessons_list_by_course', self.request.user.course.pk)
        return super(LessonsListByCourse, self).get(*args, **kwargs)



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        course = Course.objects.get(pk=self.kwargs['pk'])
        context['title'] = f"Kurs bo'yicha darslar '{course}'"
        return context

    def get_queryset(self):
        return Lesson.objects.filter(course_id=self.kwargs['pk'], is_published=True)

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Http404:
            if self.request.user.is_superuser:
                return redirect('lessons_list')
            else:
                return redirect('lessons_list_by_course', self.request.course.pk)


class LessonDetail(LoginRequiredMixin, DetailView):
    model = Lesson
    context_object_name = 'lesson'


    def get(self, *args, **kwargs):
        if not self.request.user.is_superuser and self.kwargs['course_id'] != self.request.user.course.pk:
            return redirect('lesson_detail', course_id=self.request.user.course.pk, pk=self.kwargs['pk'])
        return super(LessonDetail, self).get(*args, **kwargs)


    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Http404:
            if self.request.user.is_superuser:
                return redirect('lessons_list')
            else:
                return redirect('lessons_list_by_course', self.kwargs['course_id'])

    def get_queryset(self):
        return Lesson.objects.filter(
            pk=self.kwargs['pk'],
            course_id=self.kwargs['course_id'],
            is_published=True
        )

    def get_context_data(self, **kwargs):
        context = super(LessonDetail, self).get_context_data()
        lesson  = Lesson.objects.filter(
            pk=self.kwargs['pk'],
            course_id=self.kwargs['course_id'],
            is_published=True
        )[0]
        context['title'] = f"Dars {lesson.number} - Kurs {lesson.course}"
        context['nav_title'] = 'Darslar'
        context['files'] = []
        files = [
            ('video', 'Video'),
            ('homework', 'Uy ishi'),
            ('materials', 'Materiallar'),
            ('additional_materials', "Qo'shimcha material")
        ]
        for attr, title in files:
            file = getattr(lesson, attr)
            if file:
                context['files'].append({
                    'url': file.url,
                    'text': title
                })
        return context







class NewLesson(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = LessonForm
    template_name = 'courses/lesson_form.html'
    extra_context = {
        'title': "Dars qo'shish"
    }

    permission_required = 'courses.can_add_lesson'

    def handle_no_permission(self):
        return redirect('lessons_list_by_course', self.request.user.course.pk)



class LessonUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'courses/lesson_form.html'
    extra_context = {
        'title': 'Darsni yangilash',
    }

    permission_required = 'courses.can_update_lesson'


class LessonDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Lesson
    context_object_name = 'lesson'
    extra_context = {
        'title': "Darsni o'chirish"
    }

    permission_required = 'courses.can_delete_lesson'

    def get_success_url(self):
        return reverse('lessons_list_by_course', kwargs={'pk': self.kwargs['course_id']})


class SearchResultsViev(LessonsList):

    def get_queryset(self):
        search_item = self.request.GET.get('q')
        lessons = Lesson.objects.filter(
            Q(title__icontains=search_item) |
            Q(description__icontains=search_item) |
            Q(script__icontains=search_item),
            is_published=True
        )
        return lessons


@login_required()
def comment_list(request, lesson_id):
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.author_id = request.user.pk
            comment.lesson_id = lesson_id
            comment.save()
            messages.success(request, 'Komentariya qoshildi!')
    else:

        form = CommentForm()

        comments = Comment.objects.filter(lesson_id=lesson_id)
        lesson = Lesson.objects.get(pk=lesson_id)

        paginator = Paginator(comments, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'form': form,
            'lesson': lesson,
            'page_obj': page_obj,
            'title': 'Komentariyalar'
        }
        return render(request, 'courses/comment_list.html', context)


@login_required()
def comment_delete(request, pk, page, lesson_id):
    try:
        comment = Comment.objects.get(pk=pk)
        if request.user == comment.author or request.user.superuser:
            comment.delete()
            messages.success(request, f"Komentariya {comment.text[:20]} o'chirildi")
            return redirect(f'/comments/{lesson_id}/?page={page}')
    except Exception as e:
        print(e, e.__class__.__name__, 'redirect')
        messages.error(request, "So'ralgan komentariya mavjud emas")

        return redirect('lessons_list')
