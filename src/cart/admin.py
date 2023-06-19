from django.contrib import admin

# Register your models here.
from .models import Cart, BookInCart

admin.site.register(BookInCart)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "get_total_price"
    )