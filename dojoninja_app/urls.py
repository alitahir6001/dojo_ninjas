from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('create_dojo', views.createdojo),
    path('create_ninjas', views.createninjas),
]