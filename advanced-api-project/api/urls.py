from django.urls import path
from .views import BookListView, BookCreateView, BookDeleteView, BookUpdateView, BookDetailView

app_name = 'library'

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/create', BookCreateView.as_view(), name='book_add'),
    path('books/delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),
    path('update/update/<int:pk>', BookUpdateView.as_view(), name='book_update'),
    path('detail/<int:pk>', BookDetailView.as_view(), name='book_detail'),
]