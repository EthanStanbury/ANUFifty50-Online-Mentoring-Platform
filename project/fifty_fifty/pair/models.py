from django.db import models
from webcore.models import Profile
from django.core.exceptions import ValidationError
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
        if(check(str(self.mentee),str(self.mentor))==True):
            self.shortcode = transfer(str(self.mentee),str(self.mentor)) ## Trimming mentee and mentor, and transfering them to Profile.paired_with
            self.name = str(self.mentee) +" -> "+ str(self.mentor)  ## Changing name of pair as mentee -> mentor
            super(Pair, self).save(*args, **kwargs)
        else:
            return False

    def delete(self): ## Overiding the delete function of Pair
        tee = str(self.mentee)
        tor = str(self.mentor)
        menteeId = tee.split(' ', 1)[1]
        mentorId = tor.split(' ', 1)[1]

        mentee_numbers_left = Profile.objects.filter(uniId__contains=mentorId).values_list('mentee_number_remaning',flat=True)[0]
        curr_paired_with = Profile.objects.filter(uniId__contains=mentorId).values_list('paired_with',flat=True)[0] # Find current mentee selected mentor is paired with value.
        curr_paired_with2 = Profile.objects.filter(uniId__contains=mentorId).values_list('paired_with2',flat=True)[0]
        curr_paired_with3 = Profile.objects.filter(uniId__contains=mentorId).values_list('paired_with3',flat=True)[0]

        if(curr_paired_with3 == menteeId):
            Profile.objects.filter(uniId__contains=mentorId).update(paired_with3="",mentee_number_remaning = mentee_numbers_left+1)
        elif(curr_paired_with2 == menteeId):
            Profile.objects.filter(uniId__contains=mentorId).update(paired_with2="",mentee_number_remaning = mentee_numbers_left+1)
        elif(curr_paired_with == menteeId):
            Profile.objects.filter(uniId__contains=mentorId).update(paired_with="",mentee_number_remaning = mentee_numbers_left+1)


        Profile.objects.filter(uniId__contains=mentorId).update()

        super(Pair, self).delete()

    def __str__(self):
        return str(self.mentee) +" -> "+ str(self.mentor)

"""
Function 'transfer' updates Mentor and Mentee Profile
with mentee number left and updates paired_with values
"""
def transfer(mentee,mentor):
    menteeId = mentee.split(' ', 1)[1]
    mentorId = mentor.split(' ', 1)[1]

    mentee_numbers = Profile.objects.filter(uniId__contains=mentorId).values_list('mentee_number',flat=True)[0] # Finds mentee numbers the mentor originally signed up for.
    mentee_numbers_left = Profile.objects.filter(uniId__contains=mentorId).values_list('mentee_number_remaning',flat=True)[0] # Finds mentee numbers left.

    print(mentee_numbers)
    print(mentee_numbers_left)

    curr_paired_with = Profile.objects.filter(uniId__contains=mentorId).values_list('paired_with',flat=True)[0] # Find current mentee selected mentor is paired with value.
    curr_paired_with2 = Profile.objects.filter(uniId__contains=mentorId).values_list('paired_with2',flat=True)[0]
    curr_paired_with3 = Profile.objects.filter(uniId__contains=mentorId).values_list('paired_with3',flat=True)[0]

    print(curr_paired_with)
    print(curr_paired_with2)
    print(curr_paired_with3)

    # Combs through paired_with and updates who the user is paired_with.

    if (curr_paired_with == "" or curr_paired_with == None):
        Profile.objects.filter(uniId__contains=mentorId).update(paired_with=menteeId, mentee_number_remaning = mentee_numbers_left-1)
    elif (curr_paired_with2 == "" or curr_paired_with2 == None):
        Profile.objects.filter(uniId__contains=mentorId).update(paired_with2=menteeId, mentee_number_remaning = mentee_numbers_left-1)
    elif (curr_paired_with3 == "" or curr_paired_with3 == None):
        Profile.objects.filter(uniId__contains=mentorId).update(paired_with3=menteeId,  mentee_number_remaning = mentee_numbers_left-1)






# Function checks if mentor can take in more mentees or not
def check(mentee,mentor):
    menteeId = mentee.split(' ', 1)[1]
    mentorId = mentor.split(' ', 1)[1]

    mentee_numbers_left = Profile.objects.filter(uniId__contains=mentorId).values_list('mentee_number_remaning',flat=True)[0]
    curr_paired_with = Profile.objects.filter(uniId__contains=mentorId).values_list('paired_with',flat=True)[0] # Find current mentee selected mentor is paired with value.
    curr_paired_with2 = Profile.objects.filter(uniId__contains=mentorId).values_list('paired_with2',flat=True)[0]
    curr_paired_with3 = Profile.objects.filter(uniId__contains=mentorId).values_list('paired_with3',flat=True)[0]


    if (mentee_numbers_left==0):
        return False
    else:
        if (curr_paired_with3 == menteeId):
            return False
        elif (curr_paired_with2 == menteeId):
            return False
        elif (curr_paired_with == menteeId):
            return False
        else:
            return True




class Meta:
    db_table = "pair"
