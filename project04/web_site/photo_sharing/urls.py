from django.conf.urls import  url
from . import views

# app_name = photo_sharing

urlpatterns = [
    url(r'^$', views.userlistview,name='userindex'),
    url(r'photo_index/$',views.photolistview.as_view(), name='photoindex'),
    url(r'user/(?P<user_slug>[-\w]+)/$', views.userdetailview,name='userdetail'),
    url(r'photo/upload/(?P<user_slug>[-\w]+)/$', views.photouploadview, name='photoupload'),
    url(r'photo/delete/(?P<user_slug>[-\w]+)/$',views.photodeleteview, name='photodelete'),
    url(r'comment/(?P<photo_id>[0-9]+)/$', views.commentcreateview, name='commentcreate'),
    ]