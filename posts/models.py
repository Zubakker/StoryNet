from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author      = models.CharField(max_length=128)
    title       = models.CharField(max_length=256)
    epigraph    = models.CharField(max_length=512, blank=True, null=True)
    # epigraph author
    text        = models.TextField()
    # cycle
    # genres
    # comments
    # likes_number
    def get_absolute_url(self):
        return reverse('posts:post-details', kwargs={'id': self.id})
    def get_absolute_edit_url(self):
        return reverse('posts:post-edit', kwargs={'id': self.id})
    def get_absolute_delete_url(self):
        return reverse('posts:post-delete', kwargs={'id': self.id})
