import os
from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver


class Mentor(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='mentor/images/', default="blog_images/stock_photo.jpg")
    docfile = models.FileField(upload_to='mentor/', null=True)

    def __str__(self):
        return self.title


###DON'T CHANGE THIS MODEL
class Mentee(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='mentee/images/', default="blog_images/stock_photo.jpg")
    docfile = models.FileField(upload_to='mentee/', null=True)

    def __str__(self):
        return self.title

class Content_Summary(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='content_summary/images/', default="blog_images/stock_photo.jpg")
    ###docfile = models.FileField(upload_to='content_summary/', null=True)

    def __str__(self):
        return self.title


#Delete content from folder
@receiver(post_delete, sender=Mentor)
@receiver(post_delete, sender=Mentee)
@receiver(post_delete, sender=Content_Summary)
def delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.docfile.delete(False)

#Delete images from folder
@receiver(post_delete, sender=Mentor)
@receiver(post_delete, sender=Mentee)
@receiver(post_delete, sender=Content_Summary)
def delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)

#Edit docfile from folder
@receiver(pre_save, sender=Mentor)
@receiver(pre_save, sender=Mentee)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = sender.objects.get(pk=instance.pk).docfile
    except sender.DoesNotExist:
        return False
    new_file = instance.docfile
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

#Edit images from folder
@receiver(pre_save, sender=Mentor)
@receiver(pre_save, sender=Mentee)
@receiver(pre_save, sender=Content_Summary)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return False
    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
