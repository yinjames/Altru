from django.contrib import admin
from django.urls import path

from . import views

app_name = 'donor'

urlpatterns = [
    path('', views.home, name="home"),
    path('<uuid:sponsor>/', views.home, name="home"),
    path('stats/donor/', views.donor_stats, name="donor_stats"),
    path('stats/team/', views.team_stats, name="team_stats"),
    path('enrollment/', views.enrollment, name="enrollment"),
    path('profile/', views.profile, name="profile"),
    path('profile/team/create', views.create_team, name="create_team"),
    path('survey/knowledge/', views.donor_knowledge, name="survey_knowledge"),
    path('survey/attitude/', views.donor_attitude, name="survey_attitude"),

]
