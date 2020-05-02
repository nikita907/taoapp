from django.contrib import admin
from .models import Users,Comment,AdditionalComments,Image,UserInfo

admin.site.register(Users)
admin.site.register(Comment)
admin.site.register(AdditionalComments)
admin.site.register(Image)
admin.site.register(UserInfo)


