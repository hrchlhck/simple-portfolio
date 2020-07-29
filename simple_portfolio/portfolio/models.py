from django.db import models

from django.conf import settings

from os.path import join

class Project(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=300)
    url = models.URLField(verbose_name="URL")
    img = models.ImageField(verbose_name="Image", upload_to='project_images')
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name