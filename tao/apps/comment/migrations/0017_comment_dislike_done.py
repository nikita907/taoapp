# Generated by Django 3.0.2 on 2020-05-09 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0016_comment_like_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='dislike_done',
            field=models.ManyToManyField(related_name='userscom2', to='comment.Users'),
        ),
    ]
