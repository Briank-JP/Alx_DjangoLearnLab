from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token



class CustomUserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField()
    class Meta:
        model = CustomUser
        fields = ['username', 'password','bio', 'email']
          
          
    # the create method will help us get information from the user and use the creat_uer()function to create the user with validated data
        def create(self, validated_data):
            
    # required fields are categoried with the [field] while optional field are seen with .get(fiel, default field)
    
            user = get_user_model().objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password'],
                bio=validated_data.get('bio', ""),
                profile_picture=validated_data.get('profile_picture', None)
            )
            token = Token.objects.create(user=user)
            return {
                'user': CustomUserSerializer(user).data,
                'token': token.key,
            }
        
"""
Generally this serialiser file, we are utilizing  the custom user model and  the get_user_model, this will help choose the current user; if itss the default user or our custom user model.
We then included the extra kwargs and added a write_only on the password in order to make it private or hidden in API responses what a GET request is done, the passwword will not be seen in the response.
Then the create method validates the user data provided and creates the user instance.
"""       