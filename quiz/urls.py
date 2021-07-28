from django.contrib import admin
from django.urls import path

from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.quiz_list, name="quiz_list"),
    path('<int:id>/', views.quiz, name="quiz"),
    path('<int:id>/data', views.quiz_data, name="quiz_data"),
]
