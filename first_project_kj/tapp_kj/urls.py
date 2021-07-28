from django.conf.urls import url
from tapp_kj import views


urlpatterns = [
    url(r'^$',views.help,name='help'),
]