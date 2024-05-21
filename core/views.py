from django.shortcuts import render
from .models import GeneralSetting, ImageSetting,Skills,Experience
# Create your views here.


def index(request):
    site_title = GeneralSetting.objects.get(name="site_title").paramater
    profile = ImageSetting.objects.get(name="profile").file
    skills = Skills.objects.all()
    experience = Experience.objects.all()
    context = {
        "site_title":site_title,
        "profile":profile,
        "skills":skills,
        "experiences":experience,
    }
    return render(request, "index.html",context)
def about_us(request):
    return render(request, "about-us.html")
def services(request):
    return render(request, "services.html")
def portfolio(request):
    return render(request, "portfolio.html")
def elements(request):
    return render(request, "elements.html")


