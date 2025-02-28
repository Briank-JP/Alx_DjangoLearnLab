from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.contrib.auth.decorators import permission_required


# Create your views here.
"""
the @permision_required method passes
"""
# veiw book permissions
@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request):
   book = Book.objects.all()
   return render(request, 'bookshelf/view_book.html', {'book': book})

# add  book permission
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        book = Book(title=title, author=author, publication_year = publication_year)
        book.save()
        return redirect('view_book')
    else:
        return render(request, 'bookshelf/add_book.html')
    
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        book.title = title
        book.author = author
        book.publication_year = publication_year
        book.save()
        return redirect('view_book')
    else:
        return render(request, 'bookshelf/edit_book.html', {'book': book})
    
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('view_book')