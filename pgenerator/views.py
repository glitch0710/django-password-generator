from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.


def home(request):
    return render(request, "pgenerator/home.html")


def password(request):

    characters = list("abcdefghijklmnopqrstuvwxyz")
    length = int(request.GET.get("length", 12))
    thepassword = ""

    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get("special"):
        characters.extend(list("!@#$%^&*_+{}|?/-"))
    if request.GET.get("numbers"):
        characters.extend(list("1234567890"))

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, "pgenerator/password.html", {"pw": thepassword})


def aboutpage(request):
    return render(request, "pgenerator/about.html")
