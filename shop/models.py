from django.utils import timezone
from django.db import models


class ShopDetail(models.Model):
    name = models.CharField(max_length=155)
    location = models.CharField(max_length=300)
    contact = models.CharField(max_length=25)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
