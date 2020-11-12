from django.urls import path
from . import views

app_name = 'loginauth'

urlpatterns = [
    path('', views.redirect_view),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('create_user/', views.signup, name='create_user')
]
