from django.db import models
from django.utils.timezone import now
import datetime

class Zaer(models.Model):
    GENDER_CHOICES = (('m', 'مرد'),
                      ('f', 'زن'))
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=1000, blank=True)
    mobile = models.CharField(max_length=16, blank=True)
    # birth_date = models.DateField(blank=True, db_index=True)
    age = models.IntegerField(blank=True, default=0)
    in_datetime = models.DateTimeField(default=now, blank=True, db_index=True)
    out_datetime = models.DateTimeField(blank=True, db_index=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=True, default='m')
    image = models.ImageField(upload_to='images/', blank=True, default='no_image')

    def save(self, *args, **kwargs):
        self.out_datetime = self.in_datetime + datetime.timedelta(days=3)
        super(Zaer, self).save(*args, **kwargs)

