# Generated by Django 2.2.2 on 2019-07-18 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Nodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_red', models.BooleanField()),
                ('name', models.TextField(blank=True, max_length=500)),
                ('percentage_commission', models.IntegerField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Node_father',
            fields=[
                ('node', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='nodes.Nodes')),
                ('initial_date', models.DateField()),
                ('final_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Comission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_commision', models.IntegerField()),
                ('type_payment', models.TextField(blank=True, max_length=500)),
                ('type_commission', models.TextField(blank=True, max_length=500)),
                ('current_balance', models.IntegerField(null=True)),
                ('node', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
