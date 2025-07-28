from django.urls import path
from . import views

from django.urls import path
from .views import home, about_me, memories, gallery, thank_you

urlpatterns = [
    path('', home, name='home'),
    path('about/', about_me, name='about_me'),
    path('memories/', memories, name='memories'),
    path('gallery/', gallery, name='gallery'),
    path('thank-you/', thank_you, name='thank_you'),
]

