# Generated by Django 3.0.2 on 2020-04-11 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_users_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='users_email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
    ]