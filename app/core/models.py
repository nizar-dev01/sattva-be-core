from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission
import os
import uuid

def user_avatar_upload(instance, filename):
    """Generate filepath the user avatar."""
    ext = os.path.splitext(filename)[1]
    filename = f"{uuid.uuid4()}{ext}"


class UserManager(BaseUserManager):
    """Custom user model manager."""

    def create_user(self, email, password=None, first_name=None, middle_name=None, last_name=None, username=None, **extra_fields):
        """Create and save a new user."""
        if not email or not username or not first_name:
            # raise an error with the missing fields
            raise ValueError(f"""
            The following required fields are missing:
                {'email, ' if not email else ''}
                {'username, ' if not username else ''}
                {'first_name' if not first_name else ''}
            """)
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, first_name=None, middle_name=None, last_name=None, username=None):
        """Create and save a new superuser."""
        # pop all many to many fields from extra_fields

        user = self.create_user(
            email=email,
            password=password,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            username=username
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username."""
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    social_media_links = models.JSONField(blank=True, null=True)
    avatar = models.ImageField(
        null=True,
        upload_to=user_avatar_upload
    )

    objects = UserManager()
    USERNAME_FIELD = 'username'

