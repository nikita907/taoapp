# Generated by Django 3.0.2 on 2020-02-28 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_nick', models.CharField(max_length=20, verbose_name='NickName')),
                ('user_age', models.IntegerField(verbose_name='Возраст')),
                ('user_information', models.TextField(max_length=400, verbose_name='о себе')),
                ('user_town', models.CharField(max_length=25, verbose_name='город')),
                ('user_country', models.CharField(max_length=25, verbose_name='страна')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=20, verbose_name='автор коммента')),
                ('comment_text', models.TextField(max_length=400, verbose_name='текст коммента')),
                ('comment_likes', models.IntegerField(verbose_name='лайки')),
                ('comment_dislikes', models.IntegerField(verbose_name='дизлайки')),
                ('pub_date', models.DateTimeField(verbose_name='дата публикации')),
                ('users_id', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='comment.Users')),
            ],
            options={
                'verbose_name': 'Мнение',
                'verbose_name_plural': 'Мнения',
            },
        ),
        migrations.CreateModel(
            name='AdditionalComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=20, verbose_name='автор коммента')),
                ('comment_text', models.TextField(max_length=400, verbose_name='текст коммента')),
                ('comment_likes', models.IntegerField(verbose_name='лайки')),
                ('comment_dislikes', models.IntegerField(verbose_name='дизлайки')),
                ('pub_date', models.DateTimeField(verbose_name='дата публикации')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.Comment')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]