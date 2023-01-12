from django.urls import path

from .views import contact, home

urlpatterns = [
    path('', home),
    path('contact/', contact),
]
