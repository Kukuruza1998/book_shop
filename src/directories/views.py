from django.shortcuts import render
from random import randint
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from pathlib import Path

from . import models
from PIL import Image

#Autor
class AutorsView(generic.ListView):
    model = models.Autor
    template_name = "book-shop/autor/autors.html"

class DeleteAutorsView(generic.DeleteView):
    model = models.Autor
    template_name = "book-shop/autor/delete_autors.html"
    success_url = "/directories/success"

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
    success_url = "/directories/success"



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
    success_url = "/directories/success"



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
    success_url = "/directories/success"



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

    def get_success_url(self) -> str:
        resizer(self.object.book_image)
        return super().get_success_url()

class BookDeleteView(generic.DeleteView):
    model = models.Book
    template_name = 'book-shop/book/delete_books.html'
    success_url = "/directories/success"

def resizer(image):
    extention = image.file.name.split('.')[-1]
    BASE_DIR = Path(image.file.name).resolve().parent
    file_name = Path(image.file.name).resolve().name.split('.')
    for m_basewidth in [250, 40]:
      im = Image.open(image.file.name)
      wpercent = (m_basewidth / float(im.size[0]))
      hsize = int(float(im.size[1]) * float(wpercent))
      im.thumbnail((m_basewidth, hsize), Image.Resampling.LANCZOS)
      im.save(str(BASE_DIR / "".join(file_name[:-1])) + f'_{m_basewidth}.' + extention)



def success_page(request):
    return render(
        request,
        template_name='book-shop/success.html'
    )