"""
URL configuration for monthly_challenges_proj project.

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('challenge/', include("challenges_app.urls"))
]
