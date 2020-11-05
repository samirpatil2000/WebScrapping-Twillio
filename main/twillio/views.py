from django.shortcuts import render
import os
from twilio.rest import Client

# Create your views here.
def sms(request):

    account_sid = 'ACfa4a3581136b69dbedf0da3879c1c7f4'
    auth_token = '75e9bd081a5c946514f16cc884ff1f2f'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Hii Samir Patil You Win Nothing",
        from_='+14439798610',
        to='+919730614299'
    )
    context={
        'message':message,
    }

    return render(request,'scrapper/sms.html',context)