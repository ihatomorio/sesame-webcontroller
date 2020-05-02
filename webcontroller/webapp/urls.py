from django.urls import path

from . import views

urlpatterns = [
    path('', views.sesame_list, name='sesame_list'),
]
