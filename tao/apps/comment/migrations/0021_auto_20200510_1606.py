# Generated by Django 3.0.2 on 2020-05-10 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0020_auto_20200510_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user',
            field=models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='comment.Users', unique='True'),
        ),
    ]