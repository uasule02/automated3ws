from django.contrib import admin
from .models import AppUser, ExcelFile
# Register your models here.

@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('user_id','email','username', 'is_superuser' )

@admin.register(ExcelFile)
class ExcelFileAdmin(admin.ModelAdmin):
    list_display = ('file_id', 'file', 'uploaded_at')
