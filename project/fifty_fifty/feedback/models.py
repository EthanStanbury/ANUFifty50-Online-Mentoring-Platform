from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator

# Create your models here.
class Feedback_contact(models.Model):
    user = models.ForeignKey(User)
    receiver_email = models.CharField(max_length=255, )
    first_name = models.CharField(max_length=255, )
    last_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + ' ' + self.last_name