from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
from django.urls import reverse
from django.utils import timezone
import random


def random_order_generator():
    number=random.randint(0,10000)
    return f'Order{number}'



class Order(models.Model):
    name=models.CharField(default=random_order_generator,max_length=10)
    total_amount=models.IntegerField(default=5000)
    coupon=models.ForeignKey('Coupon',on_delete=models.SET_NULL,blank=True,null=True)


    def __str__(self):
        return self.name


    def get_total_amount(self):
        return int(self.total_amount)

    def get_discount_amount(self):
        amount=0
        if self.coupon:
            amount=( int(self.coupon.discount) / 100 ) * int(self.get_total_amount())
        return int(amount)

    def get_final_amount(self):
        amount=int(self.get_total_amount()) - self.get_discount_amount()
        return amount

    def get_absolute_url(self):
        return reverse('order_detail_coupon',kwargs={'id':self.id})

    def get_remove_coupon_url(self):
        return reverse('remove_coupon',kwargs={'id':self.id})


def random_discount_generator():
    number=random.randint(0,95)
    return number

def random_discount_code_generator():
    list=['CODE','FRIDAY','EASY','PICKME','FIRST']
    number=random.randint(0,len(list)-1)
    return list[number]

class Coupon(models.Model):
    code=models.CharField(max_length=25,default=random_discount_code_generator,help_text='CODE50',unique=True)
    # code=models.CharField(max_length=25,default=str(random_discount_code_generator)+str(random_discount_generator),help_text='CODE50',unique=True)
    valid_from=models.DateTimeField(default=timezone.now())
    valid_to=models.DateTimeField(blank=True,null=True)
    discount=models.IntegerField(default=random_discount_generator,validators=[MinValueValidator(0),
                                             MaxValueValidator(100)])
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.code

