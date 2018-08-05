from django.db import models
from django.utils.timezone import now

class Zaer(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=1000, blank=True)
    mobile = models.CharField(max_length=16, blank=True)
    birth_date = models.DateField(blank=True, db_index=True)
    in_datetime = models.DateTimeField(default=now, blank=True, db_index=True)
    out_datetime = models.DateTimeField(blank=True, db_index=True, null=True)
    gender = models.CharField(max_length=1, blank=True, default='m')
    image = models.ImageField(upload_to='images/', blank=True)
