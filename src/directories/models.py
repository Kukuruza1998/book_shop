from django.db import models
from django.urls import reverse_lazy

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
    
    def get_absolute_url(self):
        return reverse_lazy('directories:success-page')
    #return reverse_lazy('directories:success-page'), kwargs={"pk": self.pk}
    

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
    
    def get_absolute_url(self):
        return reverse_lazy('directories:success-page')


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
    
    def get_absolute_url(self):
        return reverse_lazy('directories:success-page')
    

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
    
    def get_absolute_url(self):
        return reverse_lazy('directories:success-page')


class Book(models.Model):
    book_name = models.CharField(
        verbose_name = 'Book name',
        max_length = 50
    )
    book_image = models.ImageField(
        blank = True,
        default = "/book/book-default.jpg",
        upload_to = "book/%Y/%m/%d/"
    )
    book_price = models.DecimalField(
        max_digits = 6,
        decimal_places = 2,
        default = 0.01
    )
    autor = models.ForeignKey(
        Autor,
        on_delete = models.CASCADE,
        verbose_name = 'autor'
    )
    series = models.ForeignKey(
        Series,
        on_delete = models.PROTECT,
        verbose_name = 'series'
    )
    genre = models.ForeignKey(
        Genre,
        on_delete = models.CASCADE,
        verbose_name = 'genre'
    )
    year_publishing = models.DateField(
        verbose_name = 'Year publishing book',
        max_length = 50
    )
    page = models.DecimalField(
        max_digits = 6,
        decimal_places = 0,
        default = 0
    )
    BINDING = (
        ('Solid', 'solid'),
        ('Soft', 'soft'),
        ('Absent', 'absent'),
    )

    binding = models.CharField(
        verbose_name = 'Binding book',
        max_length = 6,
        choices = BINDING
    )
        
    FORMAT = (
        ('84x108/64', '84x108/64'),
        ('75x90/32', '75x90/32'),
        ('60x90/16', '60x90/16'),
        ('70x108/16', '70x108/16'),
        ('60x90/8', '60x90/8'),
        ('84x108/8', '84x108/8'),
    )

    format_book = models.CharField(
        verbose_name = 'Book format',
        max_length = 12,
        choices = FORMAT
    )
    ISBN = models.CharField(
        verbose_name = 'ISBN',
        max_length = 25
    )

    weight = models.DecimalField(
        verbose_name = 'Book weight(gramme)',
        max_digits = 6,
        decimal_places = 1,
        default = 0
    )
    age_restrictions = models.DecimalField(
        verbose_name = 'Age restrictions',
        max_digits = 3,
        decimal_places = 0,
        default = 0
    )
    publishing_house = models.ForeignKey(
        Publishing_House,
        on_delete = models.PROTECT,
        verbose_name = 'Publishing house'
    )
    counter_book = models.DecimalField(
        verbose_name = 'Count of books available',
        max_digits = 7,
        decimal_places = 0,
        default = 0
    )
    ACTIVE = (
        ('Y', 'active'),
        ('N', 'inactive'),
    )

    active = models.CharField(
        verbose_name = 'Book active',
        max_length = 4,
        choices = ACTIVE
    )
    rating = models.DecimalField(
        verbose_name = 'Rating',
        max_digits = 2,
        decimal_places = 1,
        default = 0
    )
    def __str__(self) -> str:
        return self.book_name
    
    def get_absolute_url(self):
        return reverse_lazy('directories:success-page')
    
    def book_picture_medium(self):
        orig_url = self.book_image.url
        new_url = orig_url.split(".")
        picture_url = ".".join(new_url[:-1]) + "_250." + new_url[-1]
        return picture_url
    
    def book_picture_small(self):
        orig_url = self.book_image.url
        new_url = orig_url.split(".")
        picture_url = ".".join(new_url[:-1]) + "_40." + new_url[-1]
        return picture_url