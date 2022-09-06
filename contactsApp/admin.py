from django.contrib import admin
from .models import Contacts

class ContactsAdmin(admin.ModelAdmin):
    model = Contacts
    list_display = ['phone_number', 'fname', 'lname', 'email', 'created_on'] 

admin.site.register(Contacts, ContactsAdmin)
