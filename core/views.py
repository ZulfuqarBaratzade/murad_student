from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")
def about_us(request):
    return render(request, "about-us.html")
def services(request):
    return render(request, "services.html")
def portfolio(request):
    return render(request, "portfolio.html")
def elements(request):
    return render(request, "elements.html")
