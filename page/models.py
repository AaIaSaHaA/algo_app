from django.db import models

# Create your models here.
class Teacher_Info(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Phonenumber=models.CharField(max_length=100)

    def __str__(self):
        return self.Name
