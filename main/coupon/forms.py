from django import forms
from .models import Coupon


# this is not use full
"""class CouponForm(forms.ModelForm):
    class Meta:
        model=Coupon
        fields=['code','valid_from','valid_to','discount','is_active']"""


class CouponForm(forms.Form):
    coupon=forms.CharField(required=False)
