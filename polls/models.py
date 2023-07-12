from django.db import models

# Create your models here.

class Guest(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    grade = models.IntegerField()
    email = models.EmailField()
    
