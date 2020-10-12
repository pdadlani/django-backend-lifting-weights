from django.db import models

# Create your models here.
class Lifting(models.Model):
  username = models.CharField(max_length=100)
  email = models.EmailField(max_length=100, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)