from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'chat_app/home.html')


def room(request, room):
    return render(request, 'chat_app/room.html')


def checkview(request):
    pass