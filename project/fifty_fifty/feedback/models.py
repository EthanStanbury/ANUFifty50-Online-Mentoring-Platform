from django.db import models
from django.contrib.auth.models import User
from webcore.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator


class Feedback_contact(models.Model):
    user = models.ForeignKey(Profile)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = "Feedback"
