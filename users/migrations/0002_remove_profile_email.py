# Generated by Django 5.0.6 on 2024-07-16 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]
