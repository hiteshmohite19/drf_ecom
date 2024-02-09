from django.urls import path, include

from .views import CategoryDetails

urlpatterns = [
    path("", CategoryDetails.as_view()),
]
