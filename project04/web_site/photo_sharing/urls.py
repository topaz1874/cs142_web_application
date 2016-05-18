from django.conf.urls import  url
from . import views

# app_name = photo_sharing

urlpatterns = [

    url(r'^$', views.listview,name='index'),
    url(r'^(?P<user_slug>[-\w]+)/$', views.userdetailview,name='userdetailview'),
    url(r'upload/(?P<user_slug>[-\w]+)/$', views.uploadview, name='uploadview'),
    url(r'edit/(?P<user_slug>[-\w]+)/$',views.editview, name='editview'),
    url(r'comment/(?P<photo_id>[0-9]+)/$', views.commentview, name='commentview'),
    ]