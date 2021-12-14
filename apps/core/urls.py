from django.urls import path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/women'), name='frontpage'),
    path('women/', views.women, name='women'),
    path('men/', views.men, name='men'),
    #path('', views.index, name='frontpage'),
]