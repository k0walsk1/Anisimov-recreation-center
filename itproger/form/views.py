from django.shortcuts import render
from .models import Articles
from .forms import ArticlesForm

def form_home(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма была заполнена неверно'

    form = ArticlesForm()

    data = {
        'form' : form,
        'error' : error
    }

    return render(request, 'form/form_home.html', data)
