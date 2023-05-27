from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'web_content/home.html')


def categories(request):
    return render(request, 'web_content/categories.html')


def favorites(request):
    return render(request, 'web_content/favorites.html')


def about(request):
    return render(request, 'web_content/about.html')


def subscriptions(request):
    return render(request, 'web_content/subscriptions.html')
