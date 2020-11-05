from django.db import models

# Create your models here.

from django.db import models
# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200 , default='No Title')
    link = models.CharField(max_length=2083 , default='No Link',blank=True,null=True)
    content=models.TextField(default='This is the content' )
    def __str__(self):
        return self.title