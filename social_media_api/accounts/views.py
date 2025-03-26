from django.shortcuts import render
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework.response import Response #to return a json respons
from rest_framework import generics, status #help us use the create api vies and the status codes
from rest_framework.authtoken.models import Token #will  help generate tokens forusers when created
from rest_framework.permissions import AllowAny, IsAuthenticated # will help us know if a user has certain permisions before accessing the api
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

# Create your views here.
class Register(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (AllowAny,) # any user can register
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):   
            user = serializer.save()
            # generate a token for the user
            token, created = Token.objects.get_or_create(user=user)
            # return the user and the token
            return Response({
                'user': CustomUserSerializer(user).data,
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # login a user with token
class Login(generics.GenericAPIView):
    serializer_class = CustomUserSerializer
    
    def post(self, request,  *args, **kwargs):
        username  = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            # generate a token for the user
            token,created = Token.objects.get_or_create(user=user)
            # return the user and the token
            return Response({
                'user': {'username': user.username, 'email': user.email},
                'token': token.key
            }, status=status.HTTP_200_OK)
            
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
# logout a user by deleting their token
class Logout(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    
# following and unfollowing other users

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    # check if the user isnt following themselves
    if request.user.id == user_id:
        return Response({'error': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)
    
    # user a try block to follow the user if they exist
    try:
        user_to_follow = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    # if they exists add them to the list 
    request.user.following.add(user_to_follow)
    
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    # check if the user isnt unfollowing themselves
    if request.user.id == user_id:
        return Response({'error': 'You cannot unfollow yourself'}, status=status.HTTP_400_BAD_REQUEST)
    
    # user a try block to unfollow the user if they exist
    try:
        user_to_unfollow = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    # if they exist remove them from the list 
    request.user.following.remove(user_to_unfollow)
    
    return Response(status=status.HTTP_200_OK)

