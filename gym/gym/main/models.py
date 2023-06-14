from django.db import models

# Create your models here.
class Part(models.Model):
    part_name = models.CharField(max_length=50)

class Exercise(models.Model):
    title = models.CharField(max_length=50)
    part = models.ForeignKey(Part, on_delete=models.PROTECT, related_name='exercise')
