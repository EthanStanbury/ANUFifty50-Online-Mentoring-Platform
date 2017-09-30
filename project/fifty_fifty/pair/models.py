from django.db import models
from webcore.models import Profile
# Create your models here.

class Pair(models.Model):
    """
    This class defines a mentor-mentee pair
    It contains mentor name matched with mentee name
    """
    name = models.CharField(max_length=50, help_text='Enter a unique pair name',blank=True, null = True)
    mentor = models.ForeignKey('webcore.Profile', related_name="mentors", null = True, limit_choices_to={'role': 'Mentor'})
    mentee = models.ForeignKey('webcore.Profile', related_name="mentees", null= True, limit_choices_to={'role':'Mentee'})


    def save(self, *args, **kwargs): ## Overiding the save function of Pair
        self.name = str(self.mentee) +" -> "+ str(self.mentor)  ## Changing name of pair as mentee -> mentor
        self.shortcode = transfer(str(self.mentee),str(self.mentor)) ## trimming mentee and mentor, and transfering them to Profile.paired_with
        super(Pair, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.mentee) +" -> "+ str(self.mentor)

def transfer(tee,tor):
    menteeId = tee.split(' ', 1)[1]
    mentorId = tor.split(' ', 1)[1]
    print(Profile.objects.all())
    Profile.objects.filter(uniId__contains=menteeId).update(paired_with=mentorId)
    Profile.objects.filter(uniId__contains=mentorId).update(paired_with=menteeId, mentee_number = 1)

    x = Profile.objects.filter(uniId__contains=mentorId).get(mentee_number)
    print(x)
class Meta:
    db_table = "pair"
