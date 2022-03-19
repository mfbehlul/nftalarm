from django.db import models

# Create your models here.

class Collection(models.Model):
    name=models.CharField(max_length=128)

class Attribute(models.Model):
    name=models.CharField(max_length=128)
    collection=models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='attributes')
    
