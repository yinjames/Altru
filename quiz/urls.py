from django.contrib import admin
from django.urls import path

from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.quiz_list, name="quiz_list"),
    path('<int:id>/', views.quiz, name="quiz"),
    path('educate-donor/', views.educate_donor, name="educate_donor"),
    path('<int:id>/data', views.quiz_data, name="quiz_data"),
    path('<int:quiz_id>/<int:score>/', views.add_score, name="add_score"),
]
