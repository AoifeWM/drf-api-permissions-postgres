from django.contrib.auth import get_user_model
from django.db import models


class Island(models.Model):
    name = models.CharField(max_length=64)
    ocean = models.CharField(max_length=32)
    description = models.TextField(default="")
    size = models.TextField(default="")
    contributor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
