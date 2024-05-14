from django.urls import path
from .views import index,about_us,services,portfolio,elements



urlpatterns=[
    path("",index,name="index"),
    path("about-us/",about_us,name="about-us"),
    path("services/",services,name="services"),
    path("portfolio/",portfolio,name="portfolio"),
    path("elements/",elements,name="elements"),
]




