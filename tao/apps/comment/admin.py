from django.contrib import admin
from .models import Users,Comment,Image,UserInfo,Statistics

admin.site.register(Users)
admin.site.register(Comment)
admin.site.register(Statistics)
admin.site.register(Image)
admin.site.register(UserInfo)


