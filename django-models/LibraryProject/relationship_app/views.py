from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Book
from .models import Library

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
            return render(request, template_name='relationship_app/registration/register.html', name='register')
    else:
        form = UserCreationForm()
        return render(request, template_name='relationship_app/registration/register.html')

class LoginView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy(login)
    template_name = 'relationship_app/registration/login.html'
    
    
