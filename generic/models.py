from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

class ActivityLog(models.Model):
    CREATE = 'C'
    UPDATE = 'U'
    DELETE = 'D'
    ACTIVITIES = (
        (CREATE, 'Create'),
        (UPDATE, 'Update'),
        (DELETE, 'Delete'),
    )
    activity = models.CharField(max_length=1, choices=ACTIVITIES)
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    activity = GenericRelation(ActivityLog)


class Company(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    activity = GenericRelation(ActivityLog)
