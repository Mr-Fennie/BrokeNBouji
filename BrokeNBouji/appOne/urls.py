from django.conf.urls import url
from appOne import views

app_name = 'appOne'

urlpatterns = [
    url(r'^$', views.users, name='users'),
    url(r'^appOne/$', views.stuff, name='stuff'),
]
