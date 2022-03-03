from django.db import models


class Image(models.Model):
    path = models.CharField(max_length=300, unique=True)
    predictions = models.TextField()
