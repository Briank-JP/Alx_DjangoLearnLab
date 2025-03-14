from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


# Create your tests here.

class BookListTests(TestCase):
    def setUp(self):
        print("setting up....")
        
    def test_book_list(self):
        response = self.client.get("/api/books/")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])
    