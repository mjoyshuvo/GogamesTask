from django.shortcuts import render


def home(request):
    title = 'DjangoProject'
    return render(request, 'home.html', {'title': title})
