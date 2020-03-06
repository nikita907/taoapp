from django.contrib import admin
from .models import Users,Comment,AdditionalComments

admin.site.register(Users)
admin.site.register(Comment)
admin.site.register(AdditionalComments)
