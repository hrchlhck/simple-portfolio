from django.urls import path, include

from .views import Index, Projects

urlpatterns = [
    path('', Index.as_view()),
    path('projects/', Projects.as_view()),
]