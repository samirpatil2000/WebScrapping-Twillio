
from django.urls import path
from .views import sms
urlpatterns = [
    #BUY GOING THIS URL YOU WILL RECIVE SMS
    path('',sms,name='home'),

]
