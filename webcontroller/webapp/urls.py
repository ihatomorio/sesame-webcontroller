from django.urls import path

from . import views

urlpatterns = [
    path('', views.sesame_list, name='sesame_list'),
    path('sesame/new/', views.sesame_new, name='sesame_new')
]
