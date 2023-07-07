from django.conf import settings
from rest_framework import serializers
from .models import ExcelFile

class ExcelFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelFile
        fields = ['file_id', 'user', 'file', 'uploaded_at']
