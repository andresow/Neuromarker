# Generated by Django 2.1.7 on 2019-07-21 05:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0003_auto_20190720_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodes',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]