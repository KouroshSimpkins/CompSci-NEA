from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Kourosh',
        'title': 'Initial Post',
        'content': 'First post testing',
        'date_posted': 'December 22, 2019'
    },
    {
        'author': 'John Doe',
        'title': 'Second Post',
        'content': 'Second post testing',
        'date_posted': 'December 23, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
