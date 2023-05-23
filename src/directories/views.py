from django.shortcuts import render
from random import randint
from django.http import HttpResponse

from . import models

# Create your views here.

def home_page(request):
    return render(
        request, 
        template_name = "book-shop/home-page.html", 
        context={}
        ) 

def autors(request):
    autors = models.Autor.objects.all()
    return render(
        request, 
        template_name = "book-shop/autors.html", 
        context={'objects': autors}
        )

def genres(request):
    genres = models.Genre.objects.all()  
    return render(
        request, 
        template_name = "book-shop/genres.html", 
        context={'objects': genres}
        )

def publishing_house(request):
    publishing_house = models.Publishing_House.objects.all()  
    return render(
        request, 
        template_name = "book-shop/publishing_house.html", 
        context={'objects': publishing_house}
        ) 

def series(request):
    series = models.Series.objects.all()  
    return render(
        request, 
        template_name = "book-shop/series.html", 
        context={'objects': series}
        )

def books(request):
    books = models.Book.objects.all()
    return render(
        request, 
        template_name = "book-shop/books.html", 
        context={'objects': books}
        )