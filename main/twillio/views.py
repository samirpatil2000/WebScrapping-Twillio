from django.shortcuts import render,redirect
import os
from twilio.rest import Client
from django.contrib import messages

import random
from .forms import OTPVerificationForm

def generate_opt():
    n=random.randrange(1000,9999)
    return n

# otp=1234
otp=generate_opt()


# Create your views here.
def sms(request):
    mobile_number='+919730614299'

    # message='Network error'

    account_sid = 'ACfa4a3581136b69dbedf0da3879c1c7f4'
    auth_token = '75e9bd081a5c946514f16cc884ff1f2f'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=f"Hii Samir Patil You OTP is {otp}",
        from_='+14439798610',
        to=mobile_number
    )

    form=OTPVerificationForm()
    if request.POST:
        form = OTPVerificationForm(request.POST or None)

        if form.is_valid():
            otp_input=form.cleaned_data['otp_input']
            if otp_input==otp:
                messages.info(request,'Successfully Verify')
                return redirect('scrapper_home')
            else:
                messages.warning(request,'Your Otp Is Wrong')



    context={
        'message':message,
        'mobile_number':mobile_number,
        'form':form
    }

    return render(request,'scrapper/sms.html',context)