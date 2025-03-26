from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Postviewset, Commentviewset

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'posts', Postviewset)  # /api/posts/
router.register(r'comments', Commentviewset)  # /api/comments/

urlpatterns = [
    path('', include(router.urls)),  # Include all the routes from the router
]
