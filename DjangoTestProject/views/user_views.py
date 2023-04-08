from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.index.forms_users import UserRegisterForm, UserUpdateForm
from apps.investigator.models import Investigative


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        investigators = Investigative.objects.filter(player=request.user.id)
        print(investigators)

    context = {
        'u_form': u_form,
        'investigators': investigators
    }

    return render(request, 'users/profile.html', context)
