from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

class Contacts(models.Model):
    fname = models.CharField(max_length=75, null=False, blank=False)
    lname = models.CharField(max_length=75, null=False, blank=False)
    email = models.EmailField(_('email address'), unique=True, blank=False)
    phone_number = PhoneNumberField()
    created_on = models.DateTimeField(auto_now_add=True)