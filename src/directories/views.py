from django.shortcuts import render
from random import randint
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic

from . import models

#Autor
class AutorsView(generic.ListView):
    model = models.Autor
    template_name = "book-shop/autor/autors.html"

class DeleteAutorsView(generic.DeleteView):
    model = models.Autor
    template_name = "book-shop/autor/delete_autors.html"
    success_url = '/success'

class AddAutorsView(generic.CreateView):
    model = models.Autor
    fields = [
        'autor_name', 'autor_description'
    ]
    template_name = "book-shop/autor/add_autors.html" 
        
class UpdateAutorsView(generic.UpdateView):
    model = models.Autor
    fields = [
        'autor_name', 'autor_description'
    ]
    template_name = "book-shop/autor/update_autors.html"



#Genre
class GenreListView(generic.ListView):
    model = models.Genre
    template_name = 'book-shop/genre/genres.html'

class GenreCreateView(generic.CreateView):
    model = models.Genre
    fields = [
        'genre_name', 'genre_description'
    ]
    template_name = 'book-shop/genre/creategenre.html'

class GenreUpdateView(generic.UpdateView):
    model = models.Genre
    fields = [
        'genre_name', 'genre_description'
    ]
    template_name = 'book-shop/genre/updategenre.html'

class GenreDeleteView(generic.DeleteView):
    model = models.Genre
    template_name = 'book-shop/genre/deletegenre.html'
    success_url = '/success'



#Publishing House
class PublishingHouseView(generic.ListView):
    model = models.Publishing_House
    template_name = 'book-shop/publishing_house/publishing_house.html'

class PublishingHouseCreateView(generic.CreateView):
    model = models.Publishing_House
    fields = [
        'publishing_house_name', 'publishing_house_description'
    ]
    template_name = 'book-shop/publishing_house/create_publishing_house.html'

class PublishingHouseUpdateView(generic.UpdateView):
    model = models.Publishing_House
    fields = [
        'publishing_house_name', 'publishing_house_description'
    ]
    template_name = 'book-shop/publishing_house/update_publishing_house.html'

class PublishingHouseDeleteView(generic.DeleteView):
    model = models.Publishing_House
    template_name = 'book-shop/publishing_house/delete_publishing_house.html'
    success_url = '/success'



#Series
class SeriesView(generic.ListView):
    model = models.Series
    template_name = 'book-shop/series/series.html'

class SeriesCreateView(generic.CreateView):
    model = models.Series
    fields = [
        'series_name', 'series_description'
    ]
    template_name = 'book-shop/series/create_series.html'

class SeriesUpdateView(generic.UpdateView):
    model = models.Series
    fields = [
        'series_name', 'series_description'
    ]
    template_name = 'book-shop/series/update_series.html'

class SeriesDeleteView(generic.DeleteView):
    model = models.Series
    template_name = 'book-shop/series/delete_series.html'
    success_url = '/success'



#Books
class BookView(generic.ListView):
    model = models.Book
    template_name = 'book-shop/book/books.html'

class BookCreateView(generic.CreateView):
    model = models.Book
    fields = [
        'book_name', 'book_image', 'book_price', 'autor', 'series',
          'genre', 'year_publishing', 'page', 'binding', 'format_book',
            'ISBN', 'weight', 'age_restrictions', 'publishing_house', 
              'counter_book', 'active', 'rating'
    ]
    template_name = 'book-shop/book/create_books.html'

class BookUpdateView(generic.UpdateView):
    model = models.Book
    fields = [
        'book_name', 'book_image', 'book_price', 'autor', 'series',
          'genre', 'year_publishing', 'page', 'binding', 'format_book',
            'ISBN', 'weight', 'age_restrictions', 'publishing_house', 
              'counter_book', 'active', 'rating'
    ]
    template_name = 'book-shop/book/update_books.html'

class BookDeleteView(generic.DeleteView):
    model = models.Book
    template_name = 'book-shop/book/delete_books.html'
    success_url = '/success'



def success_page(request):
    return render(
        request,
        template_name='book-shop/success.html'
    )