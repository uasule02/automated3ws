from django.contrib import admin

# Register your models here.

from .models import ExcelFile, StandardTableFormat, Sector

'''@admin.register(ExcelFile)
class ExcelFileAdmin(admin.ModelAdmin):
    list_display = ('file_id','user','file', 'uploaded_at')


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ('sector_id', 'name')


@admin.register(StandardTableFormat)
class FormatAdmin(admin.ModelAdmin):
    list_display = ('format_id', 'name') '''

#admin.site.register(ExcelFile)

