from django.db import models

# Create your models here.
class Game(models.Model):
    CHOICES = [(True, 'Yes'), (False, 'No')]
    name = models.CharField(max_length=100, default='None')
    guessed_algorethm = models.CharField(max_length=100, default='Not enough to guess')
    
    ml = models.BooleanField(choices=CHOICES, default=False)
    dt = models.BooleanField(choices=CHOICES, default=False)
    rf = models.BooleanField(choices=CHOICES, default=False)
    svm = models.BooleanField(choices=CHOICES, default=False)
    linear = models.BooleanField(choices=CHOICES, default=False)
    logistic = models.BooleanField(choices=CHOICES, default=False)
    rein = models.BooleanField(choices=CHOICES, default=False)
    knn = models.BooleanField(choices=CHOICES, default=False)

    dl = models.BooleanField(choices=CHOICES, default=False)
    rnn = models.BooleanField(choices=CHOICES, default=False)
    lstm = models.BooleanField(choices=CHOICES, default=False)
    trans = models.BooleanField(choices=CHOICES, default=False)
    gan = models.BooleanField(choices=CHOICES, default=False)
    cnn = models.BooleanField(choices=CHOICES, default=False)
    
    def __str__(self):
        return self.name