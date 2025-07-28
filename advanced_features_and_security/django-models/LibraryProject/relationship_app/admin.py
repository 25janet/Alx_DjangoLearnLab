from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile, Author, Book
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = list(UserAdmin.fieldsets) + [
        (_('Additional Info'), {'fields': ('date_of_birth', 'profile_photo')}),
    ]

    add_fieldsets = list(UserAdmin.add_fieldsets) + [
        (_('Additional Info'), {'fields': ('date_of_birth', 'profile_photo')}),
    ]

    list_display = ['username', 'email', 'date_of_birth', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
admin.site.register(Author)
admin.site.register(Book)
