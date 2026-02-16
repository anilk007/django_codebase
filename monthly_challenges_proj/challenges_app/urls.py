"""
URL configuration for monthly_challenges_proj project.

"""
from . import views
from django.urls import path

urlpatterns = [
    path('<int:month>', views.getChallengeByNunber),
    path('<str:month>', views.getChallenge, name="monthly_challenge_url")
]
