# Generated by Django 2.1.7 on 2019-07-29 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0004_auto_20190729_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node_father',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
