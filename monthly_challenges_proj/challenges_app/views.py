from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "january challenge",
    "february": "february challenge",
    "march": "march challenge",
    "april": "april challenge",
    "may": "may challenge",
    "june": "june challenge",
    "july": "july challenge",
    "august": "august challenge",
    "september": "september challenge",
    "october": "october challenge",
    "november": "november challenge",
    "december": "december challenge"
}


def getChallenge(request, month):
  return  HttpResponse(monthly_challenges[month]);



def getChallengeByNunber(request, month):
  months = list(monthly_challenges.keys())
  redirect_month = months[month - 1]

  redirect_path = reverse("monthly_challenge_url", args=[redirect_month])

  return HttpResponseRedirect(redirect_path);