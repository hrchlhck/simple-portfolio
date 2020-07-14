from django.urls import path, include

from .views import Index, Projects

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Index.as_view()),
    path('projects/', Projects.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)