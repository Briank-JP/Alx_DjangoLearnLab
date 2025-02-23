from django.urls import path
from .views import list_books, LibraryDetialView
# from .views import L SignUpView, register
from . import views


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('books/<int:pk>/', LibraryDetialView.as_view(), name='book_detail'),
     path("register/", views.register, name='register'),
    path("login/", views.LoginView.as_view(template_name='relationship_app/registration/login.html'), name='login'),
    path("logout/", views.LogoutView.as_view(template_name='relationship_app/registration/logout.html') ,name="logout"),
]
