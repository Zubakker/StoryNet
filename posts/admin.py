from django.contrib import admin

from .models import Post, Genre, Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(Genre)
admin.site.register(Comment)
