from django.urls import path
from .views import list_books, LibraryDetialView
# from .views import L SignUpView, register
from . import views
# task 3 views
from .views import admin_view, librarian_view, member_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('books/<int:pk>/', LibraryDetialView.as_view(), name='book_detail'),
    path("register/", views.register, name='register'),
    path("login/", views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path("logout/", views.LogoutView.as_view(template_name='relationship_app/logout.html') ,name="logout"),
    
    # user authentication views
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
   
]
