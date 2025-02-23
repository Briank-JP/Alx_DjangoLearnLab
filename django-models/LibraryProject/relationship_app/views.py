from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
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
    

# User Authentication
class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    
class UserLogoutView(LogoutView):
    template_name ='registration/logout.html'
    
# User Registration

def register(request):
    if request.method == 'POST':
        form  = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
        return render(request,'relationship_app/registration/register.html', {'form':form})