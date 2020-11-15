from django.urls import path

from . import views

app_name = "media"
 
urlpatterns = [
    path('', views.index, name='list'),
    path('profile/', views.profile, name='profile'),
    path('createview',views.PostView.as_view(),name = 'createview')
    # path('/<string:user_id>/<int:content_id>', views.index, name='index'),
    # path('', views.index, name='index'),
]
