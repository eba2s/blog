from django.db import models

# Create your models here.

class posts(models.Model):
    author = models.CharField(max_length= 30)
    title = models.CharField(max_length= 100)
    continut = models.TextField()
    timestamp = models.DateTimeField(auto_now= False)


class AboutMe(models.Model):
    titleMe = models.CharField(max_length=20)
    contentMe = models.TextField()
    dateMe = models.DateField(auto_created=True)

