# Generated by Django 3.0.2 on 2020-04-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0008_auto_20200419_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='user_has_photo',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(blank=True, default='/media/test.jpg', upload_to='avatar/%Y/%M/%D'),
        ),
    ]
