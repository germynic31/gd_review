from django.urls import path

from . import views


app_name = 'levels'


urlpatterns = [
    path('', views.LevelView.as_view(), name='level_list'),
]
