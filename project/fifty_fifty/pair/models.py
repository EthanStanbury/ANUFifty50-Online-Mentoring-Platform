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
        if(check(str(self.mentor))==True):
            self.shortcode = transfer(str(self.mentee),str(self.mentor)) ## trimming mentee and mentor, and transfering them to Profile.paired_with
            self.name = str(self.mentee) +" -> "+ str(self.mentor)  ## Changing name of pair as mentee -> mentor
            super(Pair, self).save(*args, **kwargs)
        else:
            return

    def __str__(self):
        return str(self.mentee) +" -> "+ str(self.mentor)

def transfer(mentee,mentor):
    menteeId = mentee.split(' ', 1)[1]
    mentorId = mentor.split(' ', 1)[1]
    print(Profile.objects.all())
    x = Profile.objects.filter(uniId__contains=mentorId).values_list('mentee_number',flat=True)[0]
    print(x)
    Profile.objects.filter(uniId__contains=menteeId).update(paired_with=mentorId)
    Profile.objects.filter(uniId__contains=mentorId).update(paired_with=menteeId,mentee_number = x-1)



def check(mentor):
    mentorId = mentor.split(' ', 1)[1]
    x = Profile.objects.filter(uniId__contains=mentorId).values_list('mentee_number',flat=True)[0]
    if (x==0):
        return False
    else:
        return True

class Meta:
    db_table = "pair"
