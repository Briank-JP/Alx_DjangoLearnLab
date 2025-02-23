from django.urls import path
from .views import list_books, LibraryDetialView


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('books/<int:pk>/', LibraryDetialView.as_view(), name='book_detail'),
]
