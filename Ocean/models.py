from django.db import models
from django.forms import ModelForm
from django.core.files import File
# Create your models here.

class Ocean(models.Model):
    #accession = models.CharField(max_length=200, default='NA')
    #releasedate = models.CharField(max_length=200, default='NA')
    species = models.CharField(max_length=200, default='NA')
    kingdom = models.CharField(max_length=200, default='NA')
    genus =models.CharField(max_length=200, default='NA')
    family = models.CharField(max_length=200, default='NA')
    moleculetype = models.CharField(max_length=200, default='NA')
    length = models.CharField(max_length=200, default='NA')
    nuccompleteness = models.CharField(max_length=200, default='NA')
    geolocation = models.CharField(max_length=200, default='NA')
    host = models.CharField(max_length=200, default='NA')
    biosample = models.CharField(max_length=200, default='NA')
    description = models.CharField(max_length=300, default='NA')
    
    def __str__(self):
        return self.species
