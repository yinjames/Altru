from django.contrib import admin
from django.urls import path

from . import views

app_name = 'donor'

urlpatterns = [
    path('', views.home, name="home"),
    path('<uuid:sponsor>/', views.home, name="home"),
    path('stats/donor/', views.donor_stats, name="donor_stats"),
    path('champions/stats/', views.champion_stats, name="champion_stats"),
    path('enrollment/', views.enrollment, name="enrollment"),
    path('profile/', views.profile_home, name="profile"),
    path('profile/stats/', views.profile_stats, name="profile_stats"),
    path('profile/teamstats/', views.profile_team_stats, name="profile_team_stats"),
    path('profile/team/create', views.create_team, name="create_team"),
    path('profile/team/<int:team_id>/join', views.join_team, name="join_team"),
    path('survey/knowledge/', views.donor_knowledge, name="survey_knowledge"),
    path('survey/attitude/', views.donor_attitude, name="survey_attitude"),

]
