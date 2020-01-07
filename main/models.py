from django.db import models

# Create your models here.

class short_url(models.Model):
    short_url = models.CharField(max_length = 20)
    long_url = models.CharField(max_length = 100, unique=True)

    def __str__(self):
        return self.short_url