from django.shortcuts import render
from django.db.models import Q
from directories.models import Book

def search(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(
            Q(book_name__icontains=query) |
            Q(autor__autor_name__icontains=query) |
            Q(genre__genre_name__icontains=query)
        )
    else:
        books = Book.objects.all()
    context = {
        'books': books,
        'query': query,
    }
    return render(request, 'search.html', context)