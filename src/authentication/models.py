from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    Group,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """
    Custom user model that uses email as the unique identifier for authentication
    """

    def create_user(self, email, password=None):
        """
        Create and save a user, parameters : email and password, returns user
        """
        if email is None:
            raise TypeError("The email cannot be empty")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        """
        Create and save a user, parameters: email and password
        """
        if password is None:
            raise TypeError("Passwod cannot be empty")
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
