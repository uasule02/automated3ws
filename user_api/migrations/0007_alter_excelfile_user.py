# Generated by Django 4.1.5 on 2023-07-03 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0006_appuser_is_active_alter_appuser_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excelfile',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_api_excelfiles', to=settings.AUTH_USER_MODEL),
        ),
    ]