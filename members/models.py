from django.db import models

# Create your models here.

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

class baru(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  title = models.CharField(max_length=100)
  content = models.TextField()
  pub_date = models.DateTimeField('date published')
