
from django.urls import path
from .views import homeView,scrap_website
urlpatterns = [
    path('',homeView,name='scrapper_home'),
    path('scrapper/',scrap_website,name='scrapper'),
]
