from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    email = models.EmailField(_('email address'), unique=True, blank=False, null=False)
    phone_number = PhoneNumberField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number', 'first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email