from typing import Optional
from django.views import generic
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views
from django.views.generic import View
from django.http import HttpResponseRedirect

from cart.models import Cart, BookInCart

from directories.models import Book
from . import models


# Create your views here.

class AddToCartView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        cart = Cart.objects.get(user=user)
        book_pk = kwargs.get("pk")
        book = Book.objects.get(pk=book_pk)
        if cart.check_if_book_already_in_cart(book):
            return redirect(to=reverse("directories:view-book", kwargs={
                "pk": book_pk
            }))
        book_in_cart = BookInCart.objects.create(
            book=book,
            count=1,
        )
        cart.books.add(book_in_cart)
        return redirect(to=reverse("directories:view-book", kwargs={  
            "pk": book_pk
        }))


class CartView(generic.DetailView):
    model = models.Cart
    template_name = "cart/cart.html"

    def get_object(self):
        user = self.request.user
        if user.is_authenticated:
            return Cart.objects.get(user=user, id=self.kwargs.get('cart_id'))
        return None
    
    def post(self, request, *args, **kwargs):
      cart = self.get_object()
      item_id = request.POST.get('item_id')
      quantity = request.POST.get('count')
      item = cart.books.get(id=item_id)
      item.count = quantity
      item.save()
      return redirect('cart:view_cart', cart_id=cart.id)

    def remove_item(request, cart_id, item_id):
      cart = Cart.objects.get(id=cart_id)
      item = cart.books.get(id=item_id)
      item.delete()
      return redirect('cart:view_cart', cart_id=cart.id)