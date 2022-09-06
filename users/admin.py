from django.contrib import admin
from .models import CustomUser

class UserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'phone_number'] 

admin.site.register(CustomUser, UserAdmin)