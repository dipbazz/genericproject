from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from .models import ActivityLog, Profile, Company


@receiver(post_save, sender=Profile)
def activity_on_save_for_profile(sender, instance, created, **kwargs):
    if created:
        instance.activity.create(activity=ActivityLog.CREATE)
    else:
        instance.activity.create(activity=ActivityLog.UPDATE)


@receiver(post_delete, sender=Profile)
def activity_on_delete_for_profile(sender, instance, **kwargs):
    instance.activity.create(activity=ActivityLog.DELETE)
