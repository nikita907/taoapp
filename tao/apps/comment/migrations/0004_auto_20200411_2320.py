# Generated by Django 3.0.2 on 2020-04-11 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_auto_20200411_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='users_email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email'),
        ),
    ]
