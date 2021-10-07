from django.contrib import admin
from django.urls import path

from . import views

app_name = 'donor'

urlpatterns = [
    #path('', views.hero, name='greetings'),
    path('', views.home, name="home"),
    path('home/<uuid:sponsor>/', views.home, name="home"),
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
    path('survey/attitude/prioity_prompt/<int:ans>', views. prioity_prompt, name="prioity_prompt"),
    path('donor/badge/<int:donor_id>', views.donor_badge, name="donor_badge"),
    path('donor/stories/', views.story_list, name="story_list"),
    path('donor/consent/quiz/', views.consent_after_quiz, name="consent_after_quiz"),
    path('donor/consent/story/', views.consent_after_story, name="consent_after_story"),
    path('donor/consent/reward/', views.consent_after_reward, name="consent_after_reward"),
    path('donor/reward/', views.reward, name="reward"),


]
