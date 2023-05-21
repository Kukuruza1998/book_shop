from django.db import models

# Create your models here.

class Autor(models.Model):
    autor_name = models.CharField(
        verbose_name = 'Autor name',
        max_length = 50
    )
    autor_description = models.TextField(
        verbose_name = 'Autor description',
        null = True,
        blank = True
    )

    def __str__(self) -> str:
        return self.autor_name
    

class Series(models.Model):
    series_name = models.CharField(
        verbose_name = 'Series',
        max_length = 100
    )
    series_description = models.TextField(
        verbose_name = "Count book's series",
        null = True,
        blank = True
    )

    def __str__(self) -> str:
        return self.series_name


class Genre(models.Model):
    genre_name = models.CharField(
        verbose_name = 'Genre',
        max_length = 50
    )
    genre_description = models.TextField(
        verbose_name = 'Genre description',
        null = True,
        blank = True
    )

    def __str__(self) -> str:
        return self.genre_name


class Publishing_House(models.Model):
    publishing_house_name = models.CharField(
        verbose_name = 'Publishing house name',
        max_length = 50
    )
    publishing_house_description = models.TextField(
        verbose_name = 'Publishing house description',
        null = True,
        blank = True
    )

    def __str__(self) -> str:
        return self.publishing_house_name
    

class Book(models.Model):
    book_name = models.CharField(
        verbose_name = 'Book name',
        max_length = 50
    )
    book_image = models.ImageField(
        upload_to = 'book',
        blank = True
    )
    book_price = models.DecimalField(
        max_digits = 6,
        decimal_places = 2,
        default = 0
    )
    autor = models.ForeignKey(
        Autor,
        on_delete = models.PROTECT,
        verbose_name = 'autor'
    )
    series = models.ForeignKey(
        Series,
        on_delete = models.PROTECT,
        verbose_name = 'series'
    )
    genre = models.ForeignKey(
        Genre,
        on_delete = models.PROTECT,
        verbose_name = 'genre'
    )
    year_publishing = models.DateField(
        verbose_name = 'Year publishing book',
        max_length = 50
    )
    
    def __str__(self) -> str:
        return self.book_name