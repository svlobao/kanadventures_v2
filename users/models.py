import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class Language(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    iso_code = models.ChatField(max_length=2, unique=True, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    class __str__(self):
        return self.name


class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.Charfield(max_length=100, unique=True)
    iso_code = models.CharField(max_length=2, unique=True, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    class __str__(self):
        return self.name


class CustomUser(AbstractUser):
    """'
    Inherited from AbstractUser:
        username
        first_name
        last_name
        email
        is_staff
        is_active
        is_superuser
        date_joined
        groups
        user_permissions

    Inherited from AbstractBaseUser:
        password
        last_login
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    proficient_languages = models.ManyToManyField(
        Language, blank=True, related_name="proficient_users"
    )
    learning_languages = models.ManyToManyField(
        Language, blank=True, related_name="learning_users"
    )
    country = models.ForeignKey(max_length=50)
    is_premium = models.BooleanField(default=False)
