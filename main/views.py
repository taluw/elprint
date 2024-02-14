from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Home',
        'content': 'Main page E&L Print',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': False
    }

    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About page')