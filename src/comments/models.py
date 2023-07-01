from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from directories.models import Book

# Create your models here.
User = get_user_model()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits = 2, decimal_places = 1, default = 0)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Комментарий {self.user.username} к книге {self.book.book_name} с рейтингом {self.rating}' 