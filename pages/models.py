from django.db import models
from django.urls import reverse

from django.conf import settings 

# Create your models here.
class MyUser(models.Model):
    user     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                        null=True
               )
    full_name = models.CharField(max_length=256, blank=False, null=False)
    contacts = models.CharField(max_length=512, blank=True, null=True)
    biography = models.CharField(max_length=2048, blank=True, null=True)
    status   = models.CharField(max_length=128, blank=True, null=True)
    photo = models.ImageField(upload_to='pages/avatars', blank=True)

    def get_absolute_url(self):
        return reverse('author-by-id', kwargs={'pk': self.id})
