from django.urls import path

from . import views

urlpatterns = [
    path('', views.quiz_view, name='quiz_view'),

    path('<str:slug>', views.quiz_list, name='quiz_list'),
    
]