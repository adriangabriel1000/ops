from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    initals = models.CharField(max_length=10, blank=True)
    unique = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    idnum = models.CharField(max_length=200, blank=True)
    cell = models.CharField(max_length=200, blank=True)
    homenum = models.CharField(max_length=200, blank=True)
    dob = models.DateTimeField(null=True, blank=True)
    designation = models.CharField(max_length=200, blank=True)
    image = models.ImageField(default='profilepic.jpg', upload_to='profile_pictures', blank=True)

    def __str__(self):
        return self.user.username
