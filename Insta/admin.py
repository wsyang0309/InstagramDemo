from django.contrib import admin

from .models import Post, InstaUser, Comment, Like, UserConnection

# Register your models here.
admin.site.register(InstaUser)
admin.site.register(Post)
admin.site.register(UserConnection)
admin.site.register(Comment)
admin.site.register(Like)