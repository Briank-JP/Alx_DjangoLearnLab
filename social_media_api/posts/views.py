from django.shortcuts import render
from rest_framework import viewsets, permissions, filters, status
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# overide default pagination number
class Post_pagination(PageNumberPagination):
    page_size = 10
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class Postviewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] #aloow users who are authenitcated to view but only logged in user can edit.
    pagination_class = Post_pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['author']  # Allow filtering by author
    search_fields = ['title', 'content']  # Allow searching by title or content
    
    # set the current author to be the logged in user
    def perfomcreate(self, serializer):
        serializer.save(author=self.request.user)
        
        
class Commentviewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] #aloow users who are authenitcated to view but only logged in user can edit.
    
    # set the current author to be the logged in user
    def perfomcreate(self, serializer):
        serializer.save(author=self.request.user)
        
        
# implement feeds functionality where the user can see feeds from the people he follows
@api_view(['GET'])
@permission_classes([IsAuthenticated])

def feeds_view(request):
    user = request.user
    following_users = user.following.all() #get all the users being followed
    
    # get posts by the folowd users
    post = Post.objects.filter(author__in=following_users).order_by('-created_at')
    
    serializer = PostSerializer(post, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)