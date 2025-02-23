from django.urls import path
from .views import list_books, LibraryDetialView
# from .views import L SignUpView, register
from . import views
# task 3 views
from relationship_app.views.admin_view import admin_dashboard
from relationship_app.views.librarian_view import librarian_dashboard
from relationship_app.views.member_view import member_dashboard


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('books/<int:pk>/', LibraryDetialView.as_view(), name='book_detail'),
    path("register/", views.register, name='register'),
    path("login/", views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path("logout/", views.LogoutView.as_view(template_name='relationship_app/logout.html') ,name="logout"),
    # user authentication views
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_dashboard, name='librarian_dashboard'),
    path('member-dashboard/', member_dashboard, name='member_dashboard'),
]
