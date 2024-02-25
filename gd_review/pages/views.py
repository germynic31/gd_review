from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def levels(request):
    return render(request, 'pages/levels.html')


def users(request):
    return render(request, 'pages/users.html')
