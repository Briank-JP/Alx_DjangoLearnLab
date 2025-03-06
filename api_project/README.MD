Task 0; 
process of writting my first API
step on i;
 - created a directory api_project
 - created a virtual environment (python venv .venv)
 - installed django in the environment(pip install django)
 - insalled the django restframework (pip install drf)
        - alternatively you can create a django project and cd into it and install the drf inside the project directory then start and app.
 - used the alternative cose it the best way as it keeps your project work organised. Below are the steps i followed
        1️⃣ Create a virtual environment
        2️⃣ Install Django
        3️⃣ Create a Django project and cd into the project directory
        4️⃣ Install Django Rest Framework
        This keeps your project organized and ensures you don’t install unnecessary packages.
- created a Book model that has a title and an author. END task 0

Task 1
In this task we are told to create a serializer file inside the app directory
- the serializer is used to serialize the book model instances.. or to convert sql/python data into json
   - this serializer takes on the serializer class.modelserializer.
   - inside the serializer file we shall import the book model that we shall serialize. create a meta class and pass the model and all fields to be serialized(converted into json)
- then we create a view for our api that uses the serializer to retrieve or get and return the  book data
- then configured url patterns also know as the endpoints
   - This will ensure the API endpoint is accessible via HTTP
   - but first we have to register the app url file in the project url feil using the include function.
   -
Task 2(Perfom CRUD operations)
