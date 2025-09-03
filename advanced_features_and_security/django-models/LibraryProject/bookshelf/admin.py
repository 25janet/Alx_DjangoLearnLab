from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book,CustomUser,CustomUserManager
admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author',)
    list_filter = ('publication_year',)

# Register your models here.
admin.site.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email","date_of_birth","is_staff","is_superuser")
    search_fields = ("email",)
    ordering = ("email",)



