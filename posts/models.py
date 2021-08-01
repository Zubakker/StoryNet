from django.db import models
from django.urls import reverse

from django.conf import settings


# Create your models here.
class Post(models.Model):
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, 
                            blank=True, null=True, default=1
                  )
    title       = models.CharField(max_length=256)
    epigraph    = models.CharField(max_length=512, blank=True, null=True)
    # epigraph author
    text        = models.TextField()
    # cycle
    # genres
    # comments
    # likes_number
    def get_absolute_url(self):
        return reverse('posts:post-details', kwargs={'pk': self.id})
    def get_absolute_edit_url(self):
        return reverse('posts:post-update', kwargs={'pk': self.id})
    def get_absolute_delete_url(self):
        return reverse('posts:post-delete', kwargs={'pk': self.id})
