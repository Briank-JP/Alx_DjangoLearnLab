from relationship_app.models import Author, Book, Library, Librarian

# retrieving all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books =  Book.objects.filter(author=author)
    return books

# List all books in a library.
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    all_books = library.books.all() #retreve all books in that library
    return all_books

# Retrieve the librarian for a library.
def get_librarian_for_library(library_name):
    librarian = librarian.object.get(library__name = library_name)
    return librarian
    