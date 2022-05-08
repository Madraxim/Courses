from django.urls import path
from .views import *

urlpatterns = [
    path('', LessonsList.as_view(), name='lessons_list'),
    path('courses/<int:pk>', LessonsListByCourse.as_view(), name='lessons_list_by_course'),
    path('lessons/<int:course_id>/<int:pk>/', LessonDetail.as_view(), name='lesson_detail'),
    path('add/', NewLesson.as_view(), name='new_lesson'),
    path('update/<int:course_id>/<int:pk>/', LessonUpdate.as_view(), name='lesson_update'),
    path('delete/<int:course_id>/<int:pk>/', LessonDelete.as_view(), name='lesson_delete'),
    path('search/', SearchResultsViev.as_view(), name='search_results'),

    path('comments/<int:lesson_id>/', comment_list, name='comment_list'),
    path('comment/<int:page>/<int:lesson_id>/<int:pk>/delete/', comment_delete, name='comment_delete'),
]