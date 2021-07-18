from django.db.models.signals import post_save
from django.contrib.auth.models import Users
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=Users)
def creat_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Users)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()