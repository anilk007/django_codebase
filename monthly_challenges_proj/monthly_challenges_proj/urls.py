"""
URL configuration for monthly_challenges_proj project.

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # you can dynamically change below path here
    # automatically it will be change every where
    path('challenge/', include("challenges_app.urls"))
]
