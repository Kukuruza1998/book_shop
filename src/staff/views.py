from typing import Optional
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views
from django.views.generic import View
from django.http import HttpResponseRedirect

from staff.models import Cart, BookInCart

from directories.models import Book


# Create your views here.

class LoginView(auth_views.LoginView):
    template_name = "staff/login.html"


class LogoutView(auth_views.LogoutView):
    next_page = 'homepage'


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("staff:login")
    template_name = "staff/signup.html"


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
        return redirect(to=reverse("directories:view-book", kwargs={  # ПЕРЕДАТЬ MESSAGE
            "pk": book_pk
        }))
