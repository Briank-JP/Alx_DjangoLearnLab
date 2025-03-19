from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
from .models import Profile, Comment


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
# this will allow a useer to update their username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']

        
# this will allow a user to update their profile picture
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']
        
# this will allow a user to comment on a post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
