from django.db import models

# Create your models here.
class Note(models.Model):
    Subject = models.CharField(max_length=100, blank=True)
    Lesson = models.CharField(max_length=200, blank=True)
    Note1 = models.CharField(max_length=500, blank=True)
    Note2 = models.CharField(max_length=500, blank=True)
    Note3 = models.CharField(max_length=500, blank=True)
    Note4 = models.CharField(max_length=500, blank=True)
    Note5 = models.CharField(max_length=500, blank=True)
    
    def __str__(self):
        return self.Lesson