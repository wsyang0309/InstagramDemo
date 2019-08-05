from django.contrib import admin

from .models import Post, InstaUser

# Register your models here.
admin.site.register(InstaUser)
admin.site.register(Post)