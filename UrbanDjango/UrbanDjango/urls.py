"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from task2.views import task2_func_view, ViewByClass
from task4.views import task3_func_view
from task4.views import task3_shop_view
from task4.views import skate_list
from task4.views import task3_description_view
from task5.views import sign_up_by_html, sign_up_by_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func_view/', task2_func_view),
    path('class_view/', ViewByClass.as_view()),
    path('func3_view/', task3_func_view),
    path('func3_view/scates', skate_list, name='skate_list'),
    path('scates_shop_view/', task3_shop_view),
    path('skate_list/', skate_list),
    path('description_view/', task3_description_view),
    path('platform4/', task3_func_view),
    path('platform4/scates', skate_list),
    path('platform4/cart', task3_description_view),
    path('', sign_up_by_html),
    path('django_sign_up/', sign_up_by_django)


]
