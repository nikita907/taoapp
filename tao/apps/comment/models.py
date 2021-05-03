from django.db import models

class Users(models.Model):
    users_nick=models.CharField('NickName',max_length=20)
    users_email=models.EmailField('email',unique=True)
    userOnRedaction = models.BooleanField('On redaction', default=False)
    admin = models.BooleanField(default=False)

    class Meta:
        verbose_name="Пользователь"
        verbose_name_plural="Пользователи"

class UserInfo(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default='1', unique='True')
    userAge=models.IntegerField('Age',blank=True)
    userTown=models.CharField('Town',blank=True,max_length=20,default='не указано')
    userCountry=models.CharField('Country',blank=True,max_length=20,default='не указано')
    userSex=models.CharField('Sex',blank=True,max_length=10)
    userAbout=models.CharField('About',blank=True,max_length=100)

    class Meta:
        verbose_name = "Информация о пользователе"

class Image(models.Model):
    user=models.ForeignKey(Users,on_delete=models.CASCADE,default='1',unique='True')
    photo = models.ImageField(upload_to='avatar/%Y/%M/%D', blank=True,default='test.jpg')
    user_has_photo=models.BooleanField(default=False)

class Comment(models.Model):
    comment_id = models.ForeignKey(Users,on_delete=models.CASCADE)
    comment_author = models.CharField('автор коммента',max_length=20)
    comment_text=models.TextField('текст коммента',max_length=400)
    comment_likes=models.IntegerField("лайки")
    comment_dislikes=models.IntegerField("дизлайки")
    pub_date=models.DateTimeField('дата публикации')
    like_done = models.ManyToManyField(Users, related_name='userscom')
    dislike_done=models.ManyToManyField(Users,related_name='userscom2')
    onlike=models.BooleanField(default=False)
    ondislike=models.BooleanField(default=False)

    class Meta:
        verbose_name='Мнение'
        verbose_name_plural='Мнения'

class Statistics(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default='1', unique='True')
    wholeComments = models.IntegerField("Всего комментов: ")
    wholeLikes = models.IntegerField("Всего лайков: ")
    wholeDislikes = models.IntegerField("Всего дизлайков: ")

    class Meta:
        managed = True
        verbose_name='Статистика'
        verbose_name_plural = 'Статистика'


