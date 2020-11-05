
from django.urls import path
from .views import homeView,scrap_website
urlpatterns = [
    path('',homeView,name='home'),
    path('scrapper/',scrap_website,name='scrapper'),
]
