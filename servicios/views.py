from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    return render(request, 'servicios/index.html')


def servicios(request):
    return render(request, 'servicios/services.html')


def about(request):
    return render(request, 'servicios/about.html')


def contact(request):
    return render(request, 'servicios/contact.html')

def regular(request):
    return render(request, 'servicios/regular.html')
def construction(request):
    return render(request, 'servicios/Construction.html')
def pre(request):
    return render(request, 'servicios/pre.html')
def comercial(request):
    return render(request, 'servicios/comercial.html')
def inout(request):
    return render(request, 'servicios/inout.html')