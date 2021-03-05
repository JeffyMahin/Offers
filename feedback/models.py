from django.utils import timezone

from django.db import models
from offer.models import OfferDetail


class Feedback(models.Model):
    feedback = models.BooleanField(null=True, default=None)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    offer_id = models.ForeignKey(OfferDetail, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.feedback)
