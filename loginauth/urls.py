from django.urls import path

from loginauth import views

app_name = "loginauth"
 
urlpatterns = [
    path('', views.index, name='list'),

]