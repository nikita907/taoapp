# Generated by Django 3.0.2 on 2020-02-28 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='users_id',
            new_name='members',
        ),
    ]