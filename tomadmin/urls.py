"""tomadmin URL Configuration

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
from django.contrib import admin
from django.urls import path
from sitetomadmin import views #получаем данные из views.py где у нас функции с указанием пути к страницам

# для + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) в конце
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # страница с админкой tomadmin.ru/admin была уже по умолчанию
    path('admin/', admin.site.urls),

    #домашняя страница (понадобится как минимум при выходе пользователя из профиля)
    path('', views.home, name='home'), #дописали для открытия домашней страницы, пустое в '' как раз для открытия домашней страницы без доп адресов tomadmin.ru

    # создали страницу входа в личный кабинет и далее в views.py нужно задать функцию
    path('signup/', views.signupuser, name='signupuser'),

    # создадим страницу входа пользователя
    path('login/', views.loginuser, name='loginuser'),

    # создадим страницу выхода пользователя
    path('logout/', views.logoutuser, name='logoutuser'),

    # страница для оставления заявок в форму
    path('help/', views.helpuser, name='helpuser'),

    # страница отображения истории заявок из БД
    path('hist/', views.historder, name='historder'),

# !!!!ДОБАВИЛИ + static для работы с собственными css и др файлами
# https://docs.djangoproject.com/en/3.1/howto/static-files/
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
