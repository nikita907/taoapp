# Generated by Django 3.0.2 on 2020-04-12 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_auto_20200411_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='photo_id',
        ),
        migrations.RemoveField(
            model_name='users',
            name='photo',
        ),
        migrations.AddField(
            model_name='image',
            name='user',
            field=models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, to='comment.Users'),
        ),
    ]
