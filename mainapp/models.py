from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.conf import settings



# Create your models here.
class ExcelFile(models.Model):
    file_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='excel_files/', validators=[FileExtensionValidator(allowed_extensions=['xlsx', 'xls'])])
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Sector(models.Model):
    name = models.CharField(max_length=100)
    sector_id = models.AutoField(primary_key=True)
    

    def __str__(self):
        return self.name

class StandardTableFormat(models.Model):
    name = models.CharField(max_length=100)
    format_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

