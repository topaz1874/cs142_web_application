from django.conf.urls import  url
from . import views

# app_name = photo_sharing

urlpatterns = [
    url(r'^$', views.userlistview,name='userindex'),
    url(r'photo_index/$',views.photolistview.as_view(), name='photoindex'),
    url(r'user/(?P<user_slug>[-\w]+)/$', views.userdetailview,name='userdetail'),
    url(r'photo/(?P<pk>[0-9]+)/$', views.photodetailview.as_view(), name='photodetail'),
    url(r'photo/upload/(?P<user_slug>[-\w]+)/$', views.photouploadview, name='photoupload'),
    url(r'photo/delete/(?P<user_slug>[-\w]+)/$',views.photodeleteview, name='photodelete'),
    url(r'comment/(?P<pk>[0-9]+)/$', views.CommentCreate.as_view(), name='commentcreate'),
    url(r'comment/delete/(?P<pk>[0-9]+)/$', views.CommentDelete.as_view(), name='commentdelete'),
    url(r'comment/edit/(?P<pk>[0-9]+)/$', views.CommentUpdate.as_view(), name='commentedit'),
    url(r'comment/thread/(?P<pk>[-\d]+)/$', views.CommentThread.as_view(), name='commentthread'),
    ]