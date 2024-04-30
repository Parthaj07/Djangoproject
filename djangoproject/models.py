from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Patient(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='patient_users')
    user_permissions = models.ManyToManyField(Permission, related_name='patient_users_permissions')

class Doctor(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)
    groups = models.ManyToManyField('auth.Group', related_name='doctor_users')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='doctor_users_permissions')

