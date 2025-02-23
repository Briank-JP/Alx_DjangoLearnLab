from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Author
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
    
