from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'title':'Главная страница',
        
    }

    return render(request, 'main/index.html', data)

def about(request):
    data = {
        'title':'О нас',
        
    }

    return render(request, 'main/about.html', data)

def journeys(request):
    data = {
            'title':'Путишествия',
        }
    return render(request, 'main/journeys.html', data)

def games(request):
    return render(request, 'main/games.html')

def entertainments(request):
    return render(request, 'main/entertainments.html')


