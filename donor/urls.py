from django.contrib import admin
from django.urls import path

from . import views

app_name = 'donor'

urlpatterns = [
    path('', views.home, name="home"),
    path('enrollment/', views.enrollment, name="enrollment"),
    path('survey/knowledge/', views.donor_knowledge, name="survey_knowledge"),
    path('survey/attitude/', views.donor_attitude, name="survey_attitude"),

]
