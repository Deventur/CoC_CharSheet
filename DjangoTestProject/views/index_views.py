from django.shortcuts import render
from apps.index.forms import UserForm


def index(request):
    host = request.META["HTTP_HOST"]  # получаем адрес сервера
    user_agent = request.META["HTTP_USER_AGENT"]  # получаем данные бразера
    path = request.path  # получаем запрошенный путь

    data = {"host": host, "user_agent": user_agent, "path": path}

    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        return render(request, 'index/index.html', {"data": data, "name": name, "age": age})
    else:
        return render(request, 'index/userForm.html', {"form": UserForm, "data": data})




