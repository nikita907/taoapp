# Generated by Django 3.0.2 on 2020-05-10 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0019_userinfo_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='admin',
        ),
        migrations.AddField(
            model_name='users',
            name='admin',
            field=models.BooleanField(default=False),
        ),
    ]