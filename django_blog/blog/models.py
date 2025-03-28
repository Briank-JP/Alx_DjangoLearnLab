from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# My blog post models
class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'posts')
    tags = TaggableManager()  # include the tags attribut to the post model
    def __str__(self):
        return self.title
    
# creating profiles
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(default='default.jpg' ,upload_to='profile_pictures')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
# creating comments

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'
    
    
    
    

