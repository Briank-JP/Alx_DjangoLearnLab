from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# We create a custom user that inherits from django's abstract user and we also included a filed followers that is symetrical set to false meaning user A follows user B, user B doesnt automatically follow user A, and the related name helps us to have access to the users being followed.
# include the rest framework auth tokens to the setting.py file
class CustomUser(AbstractUser):
    bio = models.CharField(max_length=350, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')
    
    def __str__(self):
        return self.username
    # now after registering the custom auth user model we can run migrations.