from django.db import models

# Create your models here.

class Shift(models.Model):
    shift = models.CharField(max_length=3)
    def __str__(self):
        return self.shift

class Cycle(models.Model):
    date = models.DateTimeField()
    aShift = models.CharField(max_length=1, blank=True)
    bShift = models.CharField(max_length=1, blank=True)
    cShift = models.CharField(max_length=1, blank=True)
    dShift = models.CharField(max_length=1, blank=True)
    eShift = models.CharField(max_length=1, blank=True)
    fShift = models.CharField(max_length=1, blank=True)
    team1 = models.CharField(max_length=1, blank=True)
    team2 = models.CharField(max_length=1, blank=True)
    team3 = models.CharField(max_length=1, blank=True)
    team4 = models.CharField(max_length=1, blank=True)
    
    def __str__(self):
        return f"{self.date}"
    


