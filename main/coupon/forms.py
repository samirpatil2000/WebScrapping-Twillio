from django import forms
from .models import Coupon

class CouponForm(forms.ModelForm):
    class Meta:
        model=Coupon
        fields=['code','valid_from','valid_to','discount','is_active']