"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views import generic
from directories import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view()),
#Autor
    path('autors.html', views.AutorsView.as_view()),
    path('add_autors.html', views.AddAutorsView.as_view()),
    path('delete_autors.html/<int:pk>', views.DeleteAutorsView.as_view()),
    path('update_autors.html/<int:pk>', views.UpdateAutorsView.as_view()),
#Genre
    path('genres.html', views.GenreListView.as_view()),
    path('creategenre.html', views.GenreCreateView.as_view()),
    path('deletegenre.html/<int:pk>', views.GenreDeleteView.as_view()),
    path('updategenre.html/<int:pk>', views.GenreUpdateView.as_view()),
#Publishing house
    path('publishing_house.html', views.PublishingHouseView.as_view()),
    path('create_publishing_house.html', views.PublishingHouseCreateView.as_view()),
    path('delete_publishing_house.html/<int:pk>', views.PublishingHouseDeleteView.as_view()),
    path('update_publishing_house.html/<int:pk>', views.PublishingHouseUpdateView.as_view()),
#Series
    path('series.html', views.SeriesView.as_view()),
    path('create_series.html', views.SeriesCreateView.as_view()),
    path('delete_series.html/<int:pk>', views.SeriesDeleteView.as_view()),
    path('update_series.html/<int:pk>', views.SeriesUpdateView.as_view()),
#Books
    path('books.html', views.BookView.as_view()),
    path('create_books.html', views.BookCreateView.as_view()),
    path('delete_books.html/<int:pk>', views.BookDeleteView.as_view()),
    path('update_books.html/<int:pk>', views.BookUpdateView.as_view()),

    path('success/', views.success_page)
]
