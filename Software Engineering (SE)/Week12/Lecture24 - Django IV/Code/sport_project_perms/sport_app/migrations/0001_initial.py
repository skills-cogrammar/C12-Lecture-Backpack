# Generated by Django 5.1.6 on 2025-02-26 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30, unique=True)),
                ('sport', models.CharField(max_length=25)),
                ('team_name', models.CharField(max_length=30, unique=True)),
                ('registration_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
