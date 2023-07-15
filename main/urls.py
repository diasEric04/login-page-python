from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),

    # user

    path('user/login/', views.user_login, name='user_login'),
    path('user/logout/', views.user_logout, name='user_logout'), # r
    path('user/register/', views.user_register, name='user_register'), 
    # path('user/update/', views.user_update, name='user_update'), # r
]