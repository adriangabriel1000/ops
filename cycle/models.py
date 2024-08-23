from django.db import models

# Create your models here.

class Shift(models.Model):
    shift = models.CharField(max_length=3)
    def __str__(self):
        return self.shift


class Cycle(models.Model):
    shift = models.ForeignKey(Shift, null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateTimeField()
    cycle = models.CharField(max_length=3, blank=True)
    
    def __str__(self):
        return f"{self.date}"
    


