from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

# we want a profile to be created for each new user automatically when the user is created.
@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
# now we save the reciever
@receiver(post_save, sender = User)
def save_profile(sender, instance,  **kwargs):
    instance.profile.save()
