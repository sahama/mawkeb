from django.db import models
from django.utils.timezone import now
import datetime
from django.utils.translation import gettext_lazy as _

class Zaer(models.Model):
    GENDER_CHOICES = (('m', 'مرد'),
                      ('f', 'زن'))
    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), max_length=50)
    address = models.CharField(_("address"), max_length=1000, blank=True)
    mobile = models.CharField(_("mobile"), max_length=16, blank=True)
    # birth_date = models.DateField(blank=True, db_index=True)
    age = models.IntegerField(_("age"))
    in_datetime = models.DateTimeField(_("in date"), default=now, blank=True, db_index=True)
    out_datetime = models.DateTimeField(_("out date"), blank=True, db_index=True, null=True)
    gender = models.CharField(_("gender"), choices=GENDER_CHOICES, max_length=1)
    image = models.ImageField(_("image"), upload_to='images/', blank=True, default='no_image')

    def save(self, *args, **kwargs):
        self.out_datetime = self.in_datetime + datetime.timedelta(days=3)
        super(Zaer, self).save(*args, **kwargs)

