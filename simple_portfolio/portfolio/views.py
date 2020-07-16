from django.views.generic import TemplateView, ListView

from .models import Project

class Index(TemplateView):
    template_name = 'portfolio/index.html'
    
class Projects(ListView):
    template_name = 'portfolio/projects.html'
    model = Project
    context_object_name = 'projects'
    
class CV(TemplateView):
    template_name = 'portfolio/cv.html'