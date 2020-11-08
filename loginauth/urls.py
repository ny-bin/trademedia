from django.urls import path
from loginauth import views

app_name ='loginauth'

urlpatterns =[
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
      