from django.db import models
from django.contrib.auth.models import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

User = get_user_model()

class Notifications(models.Model):
    # These lines link to the users ie; the person notified and the one notifiying
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications') #who gets notified
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_sent') #th person who sent the notification
    verb = models.CharField(max_length=200) #shows what happened; user1 liked your comment/post

    # These lines link the notification to any type of object (like a post, comment, or user).
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) #creates a generic relation to the model
    object_id = models.PositiveIntegerField()
    target = GenericForeignKey('content_type', 'object_id') #the actual object involved in the notification.
    timestamp = models.DateTimeField(auto_now_add=True) #when the notification was sent
    is_read = models.BooleanField(default=False)  # Whether the user has seen it

    
    def __str__(self):
        return f'{self.actor.username} {self.verb} {self.target}'
    
    
"""
This model stores and organizes notifications so that users can see interactions on their posts, follows, and comments. Instead of creating separate models for different types of notifications, we use a generic system that works for all types of activities.


"""