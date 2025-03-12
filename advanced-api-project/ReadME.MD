This is my week 13 task instruction file. this week we are making custom serializers
steps;
Step 1: Install Django and Django REST Framework
    - Action Items:
        - create a virtual environment and install all dependencies
        - Install Django and Django REST Framework using pip.
        - Create a new Django project named advanced_api_project.
        - Inside the project, create a new Django app named api.

Step 2: Configure the Project
    - Settings Configuration:
        - Add rest_framework to INSTALLED_APPS in your project’s settings.py.
        - Ensure the project is set to use Django’s default SQLite database for simplicity, or configure another database if preferred.

Step 3: Define Data Models
Model Requirements:
    - Create two models, Author and Book.
        - The Author model should have the following fields:
            - name: a string field to store the author’s name.
        - The Book model should have the following fields:
            - title: a string field for the book’s title.
            - publication_year: an integer field for the year the book was published.
            - author: a foreign key linking to the Author model, establishing a one-to-many relationship from Author to Books.
    Action Items:
        - Define these models in api/models.py.
        - Run migrations to create these models in the database.

Step 4: Create Custom Serializers
Create a serializer.py file in the app directory
Serializer Details:
    - Create a BookSerializer that serializes all fields of the Book model.
    - Create an AuthorSerializer that includes:
        - The name field.
        - A nested BookSerializer to serialize the related books dynamically.
    - Validation Requirements:
        - Add custom validation to the BookSerializer to ensure the publication_year is not in the future.
        - for validation we create a validate function that takes on self and the value of the publucation year.
Step 6: Implement and Test
Testing Guidelines:
    - Use Django admin or the Django shell to manually test creating, retrieving, and serializing Author and Book instances to ensure your serializers work as expected.
    - forthis run the python shell using python manage.py runserver, then import the models and the serializer classes. 
    - create instanses of the author, using author.objects.create()pass the name of the author and books.objects.create()pass the attributes of the book model including the foreignkey.
    - remember we creatwd a custom/ nested serializer in the author class and we need to refrence to it in the author model(you add a related_name = the books custom field created.)
    - the retireve the instnaces ; author_serializer=Authorserializer(author) same to the book