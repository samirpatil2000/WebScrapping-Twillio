from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests
from .models import News
# Create your views here.

def homeView(request):
    object=News.objects.all()
    return render(request,'scrapper/home.html',{'objects':object})

def scrap_website(request):
    src = requests.get('http://coreyms.com').text

    soup = BeautifulSoup(src, 'lxml')
    articles = soup.find_all('article')
    i = 0

    for article in articles:
        title = article.header.h2.a.text
        time = article.header.p.time.text

        content_class = article.find('div', class_='entry-content')
        content = content_class.p.text

        try:

            video_link = content_class.span.iframe['src']
            """ Now you have to take only id of that yt video """
            video_id = video_link.split('/')[
                4]  # because split function will return list and our id is at 4th position and the link is separated by " / "
            id = video_id.split('?')[0]
            yt_link = f'https://youtube.com/watch?v={id}'

        except Exception as e:
            yt_link = None

        i += 1

        data=News.objects.create(title=title,link=yt_link,content=content)
        data.save()


        print(i, ']  ', title, "  -  ", " {", time, "} ", "\n", content, "\n", yt_link)
    return redirect('home')
