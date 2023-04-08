"""DjangoTestProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include

from views import index_views, about_views, investigator_views, user_views, test_views
from django.contrib.auth import views as auth_views

about_patterns = [
    re_path(r'^', about_views.main),
    re_path(r'^contacts', about_views.contact),
]

urlpatterns = [
    re_path(r'^testPage', test_views.main, name='testPage'),
    path('investigator/<int:investigator_id>', investigator_views.main, name='investigator'),
    re_path(r'^index', index_views.index, name='home'),
    path('about', include(about_patterns)),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    re_path(r'^profile', user_views.profile, name='profile'),
    re_path(r'^accounts/profile', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', index_views.index, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
