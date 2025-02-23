from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('books/<int:pk>/', views.LibraryDetialView.as_view(), name='book_detail'),
]
