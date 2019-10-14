from django.shortcuts import render
# from .articles import Post


def index(request):
    return render(request, 'index_simulations.html', {})
# Create your views here.
