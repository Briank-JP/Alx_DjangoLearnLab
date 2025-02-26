from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, date_of_birth =None, profile_picture = None ):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            profile_picture=profile_picture,)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, username, email, password=None, date_of_birth =None, profile_picture =None ):
        user = self.create_user(username, email, password, date_of_birth, profile_picture)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user      
        
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    
    objects = CustomUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'date_of_birth', 'profile_picture']
    
    def __str__(self):
        return self.username



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()