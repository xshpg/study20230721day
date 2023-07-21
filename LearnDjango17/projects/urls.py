
from django.contrib import admin
from django.urls import path
from projects.views import ProjectList,ProjectDetails

urlpatterns = [
    path('projects/',ProjectList.as_view()),
    path('projects/<int:pk>/', ProjectDetails.as_view()),
]
