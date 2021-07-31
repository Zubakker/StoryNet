from django.db import models

# Create your models here.
class Post(models.Model):
    author      = models.CharField(max_length=128)
    title       = models.CharField(max_length=256)
    epigraph    = models.CharField(max_length=512)
    # epigraph_author
    text        = models.TextField()
    # cycle
    # genres
    # comments
    # likes_count

