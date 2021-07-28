from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from first_app_kj import views

urlpatterns = [
    url(r'^$',views.print_text,name='print_text')
]