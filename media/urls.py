from django.urls import path

from . import views

app_name = "media"
 
urlpatterns = [
    path('', views.index, name='list'),
    path('profile', views.profile, name='profile'),
    path('createview',views.PostView.as_view(),name = 'createview'),
    path('usercontents', views.ContentsListByUser.as_view(), name='usercontents'),
    path('<int:pk>/detail', views.ContentDetail.as_view(), name='detail'),
]
