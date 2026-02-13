from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


# Create your views here.

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


def monthly_challenge(request,month):
  try:
    challenge_text = monthly_challenges[month]
    return HttpResponse(challenge_text)
  except:
    return HttpResponseNotFound("month does not exist");

def monthly_challenge_by_number(request,month):
  print("monthly_challenge_by_number is called")
  months = list(monthly_challenges.keys())

  if (month > len(months)):
     return HttpResponseNotFound("Invalid month");

  monthToRedirect = months[month - 1];
  return HttpResponseRedirect("/challenges/" + monthToRedirect);

