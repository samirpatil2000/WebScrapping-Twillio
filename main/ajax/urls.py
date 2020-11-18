
from django.urls import path
from .views import ajax_home
urlpatterns = [
    #BUY GOING THIS URL YOU WILL RECIVE SMS
    path('',ajax_home,name='ajax_home'),

]
