from django.db import models
class countdown(models.Model):
    time=models.CharField(max_length=20,null=True, blank=True)
