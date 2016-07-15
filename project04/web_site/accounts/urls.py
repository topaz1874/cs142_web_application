from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'register/$', views.register, name='register'),
    url(r'login/$', views.auth_login, name='login'),
    url(r'logout/$', views.auth_logout, name='logout'),

    ]