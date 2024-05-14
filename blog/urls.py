from django.urls import path
from .views import blog,single_blog

urlpatterns=[
    path("",blog,name="blog"),
    path("single-blog/",single_blog,name="single_blog")
]


