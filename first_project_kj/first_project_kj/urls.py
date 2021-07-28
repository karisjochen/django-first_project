"""first_project_kj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url, include
from first_app_kj import views as first_app_views
# from tapp_kj import views as tapp_views

urlpatterns = [
    url(r'^$',first_app_views.print_text,name='print_text'), # this is the display for the website landing page
    url(r'^help/', include('tapp_kj.urls')),
    url(r'^users/', include('users_app.urls'), name='display_users'),
    url(r'^userform/', include('users_app.urls2'),name='user_view'),
    url(r'^first_app_kj/',include('first_app_kj.urls')),
    path('admin/', admin.site.urls),
]
