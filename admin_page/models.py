from email.policy import default
from django.db import models
from datetime import date

# Create your models here.


class Blog(models.Model):
    heading = models.CharField(max_length=120)
    desc = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to="uploads/blogs/")
    date = models.DateField(default=date.today)

class Message(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=70)
    message = models.TextField()
    contact = models.CharField(max_length=150)
    time = models.DateTimeField(auto_now_add=True)

class Random(models.Model):
    photo = models.ImageField(upload_to="uploads/random/")