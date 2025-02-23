from django.urls import path
from .views import list_books, LibraryDetialView, UserLogoutView, UserLoginView, register


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('books/<int:pk>/', LibraryDetialView.as_view(), name='book_detail'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', register, name='register'),
]
