from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Book
from .models import Library
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'list_books':books}
    return render(request, 'relationship_app/list_books.html', context)

# class bassed view
class LibraryDetialView(DetailView):
    model = Library
    template_name ='relationship_app/library_detail.html'
    context_object_name = 'library'
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, template_name='relationship_app/register.html', name='register')
    else:
        form = UserCreationForm()
        return render(request, template_name='relationship_app/register.html')

class LoginView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy(login)
    template_name = 'relationship_app/login.html'
    

# Role-checking functions
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")  # Ensure this path is present

# Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")  # Ensure this path is present

# Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")  # Ensure this path is present
