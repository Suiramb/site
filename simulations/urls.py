from django.urls import path

from . import views

app_name = 'simulations'

urlpatterns = [
    path('', views.index, name='index'),
]
