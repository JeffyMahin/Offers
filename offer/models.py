from django.db import models
from django.utils import timezone

from shop.models import ShopDetail


class OfferDetail(models.Model):
    name = models.CharField(max_length=155)
    product = models.CharField(max_length=155)
    image = models.ImageField(upload_to='uploads/')
    offer_percentage = models.FloatField(null=True, blank=True, default=0)
    detail = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(null=True, blank=True, default=0)
    shop_id = models.ForeignKey(ShopDetail, on_delete=models.CASCADE, default=None)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return str(self.name)
