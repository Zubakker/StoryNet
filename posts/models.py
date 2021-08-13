from django.db import models
from django.urls import reverse

from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name        = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    def __str__(self):
        return self.name

class Comment(models.Model):
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, 
                            blank=True, null=True, default=1
                  )
    text        = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    like_number = models.PositiveIntegerField()
    who_liked   = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='+')

class Post(models.Model):
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, 
                            blank=True, null=True, default=1
                  )
    updated_at = models.DateTimeField(auto_now=True)
    title       = models.CharField(max_length=256)
    epigraph    = models.CharField(max_length=512, blank=True, null=True)
    epigr_author = models.CharField(max_length=128, blank=True, null=True)
    text        = models.TextField()
    genres      = models.ManyToManyField(Genre)
    summary     = models.CharField(max_length=1024, blank=True, null=True)
    comments    = models.ManyToManyField(Comment)
    who_liked   = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='+')
    like_number = models.PositiveIntegerField(default=0, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse('posts:post-details', kwargs={'pk': self.id})
    def get_absolute_edit_url(self):
        return reverse('posts:post-update', kwargs={'pk': self.id})
    def get_absolute_delete_url(self):
        return reverse('posts:post-delete', kwargs={'pk': self.id})
    def get_absolute_comments_url(self):
        return reverse('posts:post-comments', kwargs={'pk': self.id})



