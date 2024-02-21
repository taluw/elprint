from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    context = {
        'title': 'Home - Главная',
        'content': 'Главная страница E&L Print'
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': "Красивый текст про Лену и Леонида"
    }

    return render(request, 'main/about.html', context)    

def contact(request):
    context = {
        'title': 'Home - Контакты',
        'content': 'Контакты',
        'text_on_page': "Ну контакты тудыть сюдыть"
    }

    return render(request, 'main/contact.html', context)    

def shipay(request):
    context = {
        'title': 'Home - Доставка и оплата',
        'content': 'Доставка и оплата',
        'text_on_page': "Такси заказывали"
    }

    return render(request, 'main/shipay.html', context)    