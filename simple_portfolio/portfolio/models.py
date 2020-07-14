from django.db import models

from django.conf import settings

from os.path import join

class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    url = models.URLField()
    img = models.ImageField(upload_to='project_images')
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name