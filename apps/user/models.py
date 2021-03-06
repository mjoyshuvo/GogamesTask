from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager


# Create your models here.


class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""

    def create_user(self, email, username, password=None):
        """Creates a new user profile."""
        if not email:
            raise ValueError('Users must have an email addresss.')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, )

        user.set_password(password)
        user.save(using=self._db)
        print('cr')
        return user

    def create_superuser(self, email, username, password):
        """Creates and saves a new superuser with given details."""
        print('csr')
        user = self.create_user(email, username, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(null=False, blank=False, max_length=30)
    last_name = models.CharField(null=False, blank=False, max_length=30)
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    username = models.CharField(max_length=30, unique=True, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_username(self):

        return self.username

    def __str__(self):

        return self.email
