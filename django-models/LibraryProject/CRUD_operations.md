Create;
from bookshelf.models import Book
book = Book.object.create(title = '1984', author = 'George Orwell', publication_year = 1949)

<!-- # Expected output: <Book: 1984> -->

Retrieve 
retriev_book = Book.objects.get(title = "1984")
retriev_book.__dict__
<!-- {'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949} -->

update
retriev_book.title = "Nineteen Eighty-four"
retriev_book.save()
Book.object.get(id = retriev__book.id).title

<!-- 'Nineteen Eighty-Four' -->

Delete
retriev_book.delete()
Book.objects.all

<!-- <QuerySet []>
 -->