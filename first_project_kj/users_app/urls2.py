from django.conf.urls import url
from users_app import views

# urlpatterns = [
#     url(r'^$',views.display_users,name='display_users'),

# ]
urlpatterns = [
    url(r'^$',views.display_users,name='display_users'),

]