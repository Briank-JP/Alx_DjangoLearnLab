retriev_book = Book.objects.get(title = "1984")
retriev_book.__dict__
<!-- {'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949} -->