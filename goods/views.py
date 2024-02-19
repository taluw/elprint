from django.shortcuts import render
from django.template import context


def catalog(request):
    context = {
        "title": "E&L Print - Каталог",
        "goods": [
            {
                "image": "deps/images/goods/brelki/a Attack on Titan 01.jpg",
                "name": "a Attack on Titan 01",
                "description": "a Attack on Titan 01.jpg",
                "price": 150.00,
            },
            {
                "image": "deps/images/goods/brelki/a Chainsaw Man 02.jpg",
                "name": "a Chainsaw Man 02",
                "description": "a Chainsaw Man 02.jpg",
                "price": 93.00,
            },
            {
                "image": "deps/images/goods/brelki/a Frieren 05.jpg",
                "name": "a Frieren 05",
                "description": "a Frieren 05.jpg",
                "price": 670.00,
            },
            {
                "image": "deps/images/goods/brelki/a Kimetsu no Yaiba 11.jpg",
                "name": "Кухонный стол с раковиной",
                "description": "Кухонный стол для обеда с встроенной раковиной и стульями.",
                "price": 365.00,
            },
            {
                "image": "deps/images/goods/otkritki/a Attack on Titan 06.jpg",
                "name": "Кухонный стол с встройкой",
                "description": "Кухонный стол со встроенной плитой и раковиной. Много полок и вообще красивый.",
                "price": 430.00,
            },
            {
                "image": "deps/images/goods/otkritki/a Chainsaw man Aki 01.jpg",
                "name": "Угловой диван для гостинной",
                "description": "Угловой диван, раскладывается в двухспальную кровать, для гостинной и приема гостей самое то!",
                "price": 610.00,
            },
            {
                "image": "deps/images/goods/otkritki/a Ghibli 02.jpg",
                "name": "Прикроватный столик",
                "description": "Прикроватный столик с двумя выдвижными ящиками (цветок не входит в комплект).",
                "price": 55.00,
            },
            {
                "image": "deps/images/goods/otkritki/a Kimetsu no Yaiba 07.jpg",
                "name": "Диван обыкновенный",
                "description": "Диван, он же софа обыкновенная, ничего примечательного для описания.",
                "price": 190.00,
            },
            {
                "image": "deps/images/goods/plakati/Genshin 07.jpg",
                "name": "Стул офисный",
                "description": "Описание товара, про то какой он классный, но это стул, что тут сказать...",
                "price": 30.00,
            },
            {
                "image": "deps/images/goods/plakati/Genshin 54.jpg",
                "name": "Растение",
                "description": "Растение для украшения вашего интерьера подарит свежесть и безмятежность обстановке.",
                "price": 10.00,
            },
            {
                "image": "deps/images/goods/plakati/Genshin ship ТартаЛи 20.jpg",
                "name": "Цветок стилизированный",
                "description": "Дизайнерский цветок (возможно искусственный) для украшения интерьера.",
                "price": 15.00,
            },
            {
                "image": "deps/images/goods/plakati/Genshin Навия 03.jpg",
                "name": "Прикроватный столик",
                "description": "Столик, довольно странный на вид, но подходит для размещения рядом с кроватью.",
                "price": 25.00,
            },
        ],
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
