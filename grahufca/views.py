from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Troop


def index(request):
    context = {

    }
    return render(request, 'grahufca/index.html', context)


def info(request):
    context = {

    }
    return render(request, 'grahufca/info.html', context)


def vote(request):
    if request.POST['answer'] != "fleur":
        return render(request, 'grahufca/index.html', {
            'error_message': "Zła odpowiedź, spróbujcie ponownie.",
        })
    else:
        return render(request, 'grahufca/info.html', {

        })
