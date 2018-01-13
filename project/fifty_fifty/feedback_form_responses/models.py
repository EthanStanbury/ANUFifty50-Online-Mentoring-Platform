from django.db import models
from webcore.models import Profile
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

MEET_UP_CHOICES = (
    ('NO','NO'),
    ('ONLINE','ONLINE'),
    ('IN_PERSON','IN PERSON')
)

# Create your models here.
class Feedback(models.Model):
    user = models.ForeignKey(Profile)
    first_name = models.CharField(max_length=255)
    meet_up = models.CharField(max_length=100, choices=MEET_UP_CHOICES)
    rate_f50 = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    anymore_feedback = models.TextField()
