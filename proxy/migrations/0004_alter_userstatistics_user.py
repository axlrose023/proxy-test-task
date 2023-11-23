# Generated by Django 4.2.3 on 2023-11-22 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proxy', '0003_alter_userstatistics_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstatistics',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]