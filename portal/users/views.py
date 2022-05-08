from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from .forms import LoginForm, RegistrationForm

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from .models import CustomUser
import string
from django.contrib.auth.models import Group
from courses.models import Course

from django.core.mail import send_mail
from portal import settings

from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('users.can_add_new_user')
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            chars = string.ascii_lowercase + string.digits
            password = CustomUser.objects.make_random_password(length=8, allowed_chars=chars)
            user.set_password(password)

            group = Group.objects.get(pk=request.POST['group'])
            user.group = group

            course = Course.objects.get(pk=request.POST['course'])
            user.course = course

            group.user_set_add(user)

            message_to_user = f'''Salom {user.first_name} {user.last_name}
Siz portalga kirish huquqiga ega bo'ldingiz.

Login: {user.username}
Parol: {password}

Birinchi avtorizatsiyadan so'ng parolni almashtirishini maslahat beramiz.
'''
            mail = send_mail(
                subject="Ta'lim portaliga dostup",
                message=message_to_user,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=True
            )

            if mail:
                messages.success(request, 'Akaunt yaratilib xat jonatildi')
            else:
                messages.error(request, 'Xatni yuborishda xatolik')

            print(message_to_user)
            return redirect('lessons_list')

    else:
        form = RegistrationForm()
        context = {
            'title': 'Akkanut ochish',
            'form': form,
        }
    return render(request, 'users/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Salom {user.username}! Siz avtorizatsiyadan o'tdingiz.")
            next_page = request.POST.get('next', 'lessons_list')
            return redirect(next_page)
    else:
        form = LoginForm()

    context = {
        'title': "Akountga kirish",
        'form': form,
    }
    return render(request, 'users/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'users/profile.html', {'title': 'Sining profilingiz'})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Parol muvaffaqiyatli o\'zgartirildi')
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)

    context = {
        'title': "Parolni o'zgartirish",
        'form': form
    }
    return render(request, 'users/change_password.html', context)




















