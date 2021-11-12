#!/usr/bin/env python3

from django.shortcuts import render

# Create your views here.

from newsapi import NewsApiClient

import environ

# initialise environment variables

env = environ.Env()

environ.Env.read_env()

API_KEY = env('API_KEY')

def Index(request):
    newsapi = NewsApiClient(API_KEY)
    topheadlines = newsapi.get_top_headlines(sources='al-jazeera-english')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])


    mylist = zip(news, desc, img)


    return render(request, 'index.html', context={"mylist":mylist})



def bbc(request):
    newsapi = NewsApiClient(API_KEY)
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])


    mylist = zip(news, desc, img)


    return render(request, 'bbc.html', context={"mylist":mylist})
