# Generated by Django 3.0.2 on 2020-05-09 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0015_auto_20200501_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='like_done',
            field=models.ManyToManyField(related_name='userscom', to='comment.Users'),
        ),
    ]
