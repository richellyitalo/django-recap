from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Rich'
    })


def contact(request):
    return render(request, 'recipes/contact.html', context={
        'name': 'Jão da silva de sousa'
    })
