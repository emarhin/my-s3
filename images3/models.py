from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.conf import settings
import os

# Create your models here.


class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

 


@receiver(post_delete, sender=UploadedImage)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `YourModel` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)