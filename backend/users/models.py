from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class UserProfileManager(BaseUserManager):
    """Manager for custom user profiles"""

    def create_user(self, email, fname, lname, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("Email address must be provided for user")

        email = self.normalize_email(email)
        user = self.models(email=email, fname=fname, lname=lname)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, fname, lname, password):
        """Create a new superuser"""
        user = self.create_user(email, fname, lname, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users"""

    email = models.EmailField("Email", max_length=255, unique=True)
    fname = models.CharField("First Name", max_length=255)
    lname = models.CharField("Last Name", max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fname', 'lname']

    def get_full_name(self):
        """Retrieve full name of user"""
        return '{} {}'.format(self.fname, self.lname)

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.fname

    def __str__(self):
        """Return string representation of the UserProfile model"""
        return self.email
