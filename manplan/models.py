from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200, blank=False)
    unNum = models.CharField(max_length=200, blank=True)
    designation = models.CharField(max_length=200, blank=False)
    ftm = models.CharField(max_length=3, blank=True)
    shift = models.CharField(max_length=1, blank=True)
    address = models.CharField(max_length=200, blank=True)
    idnum = models.CharField(max_length=200, blank=True)
    cell = models.CharField(max_length=200, blank=True)
    homenum = models.CharField(max_length=200, blank=True)
    dob = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class Schedule(models.Model):
    date = models.DateTimeField()
    position = models.CharField(max_length=5, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date}"