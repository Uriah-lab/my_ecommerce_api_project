# users/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Avoids clash
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Avoids clash
        blank=True
    )



