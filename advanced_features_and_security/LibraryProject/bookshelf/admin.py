from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year',)
    search_fields = ('title', 'author')
    


# customuser admin
class ModelAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('date_of_birth', 'profile_picture')}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_picture')}),
    )
    
admin.site.register(CustomUser, ModelAdmin)
    
admin.site.register(Book, BookAdmin)
