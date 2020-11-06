from django import forms

class OTPVerificationForm(forms.Form):
    otp_input=forms.IntegerField(required=True)


