
from django.urls import path
from .views import coupon,orders_list
urlpatterns = [

    path('c/',coupon,name='coupon'),
    path('',orders_list,name='orders_list'),

]
