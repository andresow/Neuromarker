# Generated by Django 2.2.2 on 2019-08-02 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('docfile', models.ImageField(upload_to='static/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('value', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('restriction', models.BooleanField()),
                ('state', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=200)),
                ('picture', models.ImageField(null=True, upload_to='')),
                ('discount', models.IntegerField(default=0)),
            ],
        ),
    ]
