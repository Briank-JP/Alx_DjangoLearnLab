from django.urls import path
from .views import list_books, LibraryDetialView

# login, logout and registr urls
from django.contrib.auth.views import LoginView, LogoutView
from . import views

# task 3 views
from .views import admin_view, librarian_view, member_view


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('books/<int:pk>/', LibraryDetialView.as_view(), name='book_detail'),
    
    # user registration and loging in and out
    path("register/", views.register, name='register'),
    path("login/", LoginView.as_view(template_name='relationship_app/login.html', next_page = 'list_books'), name='login'),
    path("logout/", LogoutView.as_view(template_name='relationship_app/logout.html') ,name="logout"),
    
    # user authentication views
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
    
      # perfoming crud operations on the books models
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),

   
]
