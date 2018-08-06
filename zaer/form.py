from django import forms
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from .models import Zaer
from django.utils.translation import gettext_lazy as _



class ZaerForm(forms.ModelForm):
    class Meta:
        model = Zaer
        fields = ('first_name', 'last_name', 'age', 'gender', 'image', 'address', 'mobile')

    # def __init__(self, *args, **kwargs):
    #     super(ZaerForm, self).__init__(*args, **kwargs)
    #
    #     # you can added a "class" to this field for user your datepicker!
    #     # self.fields['date'].widget.attrs.update({'class': 'jalali_date-date'})
    #
    #     self.fields['birth_date'] = SplitJalaliDateTimeField(
    #         widget=AdminJalaliDateWidget # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
    #     )
