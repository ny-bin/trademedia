from django.urls import path

from . import views

app_name = "media"
 
urlpatterns = [
    path('', views.index, name='list'),
    # path('/<int:user_id>/list', views.index, name='index'),
    # path('/<string:user_id>/<int:content_id>', views.index, name='index'),
    # path('', views.index, name='index'),

]
