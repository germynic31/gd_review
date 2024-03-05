from django.urls import path

from . import views


app_name = 'users'


urlpatterns = [
    path('', views.UsersView.as_view(), name='user_list'),
    path('<str:username>/', views.ProfileView.as_view(), name='profile'),
]
