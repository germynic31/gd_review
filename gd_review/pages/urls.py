from django.urls import path

from . import views


app_name = 'pages'


urlpatterns = [
    path('levels/', views.levels, name='levels'),   # TODO: перенести в новое приложение
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('users/', views.users, name='users'),
]
