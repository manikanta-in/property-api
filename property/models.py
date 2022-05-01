from django.db import models


class Property(models.Model):
    location = models.CharField(max_length=100, blank=False, default='')
    latittude = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False, default=0)
    longitude = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False, default=0)
    extent_in = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False, default=0)
    road_size = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False, default=0)
    village_locality = models.CharField(max_length=100, blank=False, default=0)
    mandal = models.CharField(max_length=100, blank=False, default=0)
    offer_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False, default=0)
    near_market_value = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False, default=0)
    distance_from_orr = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False, default=0)
    name_of_owner = models.CharField(max_length=100, blank=False, default=0)
    contact_details = models.CharField(max_length=1000, blank=False, default=0)
    approch_road = models.CharField(max_length=30, blank=False, default=0)
