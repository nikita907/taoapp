# Generated by Django 3.0.2 on 2020-04-25 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0010_users_users_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='users_photo',
        ),
    ]