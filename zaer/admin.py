from django.contrib import admin
from .models import Zaer
from jalali_date.admin import ModelAdminJalaliMixin
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from django.forms import DateTimeField, DateField

@admin.register(Zaer)
class ZaerModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    formfield_overrides = {
        DateField: {'widget': JalaliDateField},
        # DateTimeField: {'widget': SplitJalaliDateTimeField},
    }

# admin.site.register(ZaerModelAdmin)