from django.contrib import admin
from django.urls import path,include
from .views import contact_us
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',contact_us,name='contact'),
]
