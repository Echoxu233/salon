from django.urls import path
from . import views

app_name = 'haircut'
urlpatterns = [
    path('', views.home_page, name='home_page'),
]

from django.shortcuts import render

def home_page(request):

    if request.method == "GET":
            return render(request, 'blog/home_page.html')

    if request.method == "POST":
            return render(request, 'blog/home_page.html')
