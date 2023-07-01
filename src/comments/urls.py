from django.urls import path

from . import views

app_name = 'comments'

urlpatterns = [
      path('view_book/<int:pk>', views.book_comments, name='book_comments'),  
      path('add_comment/<int:pk>', views.add_comment, name='add_comment'),  
]