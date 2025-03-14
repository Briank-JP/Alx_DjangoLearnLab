
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


# Create your tests here.

class BookListTests(APITestCase):
    def setUp(self):
        # create a new user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
    def test_authentcated_user_can_access_book_list(self):
        # login the user
        self.client.login(username='testuser', password='testpassword')
        
        # make a request 
        response = self.client.get('/api/books/')
        
        # check the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
      
        
    def test_book_list(self):
        response = self.client.get("/api/books/")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])
    