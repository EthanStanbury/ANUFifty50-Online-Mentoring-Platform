from django.db import models
from django.db.models.fields import IntegerField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

YEAR_OF_STUDY = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5+','5+'),
)

UNIVERSITY = (
    ('','-'),
    ('ANU', 'The Australian National University'),
)

# Degree choices for Program 1
# The first degree has to be STEM
# It cannot be non-STEM
STEM_DEGREE_PROGRAMME = (
    ('','-'),
    ('AACOM','Bachelor of Advanced Computing (Honours)'),
    ('AACRD','Bachelor of Advanced Computing (R&D) (Honours)'),
    ('BADAN','Bachelor of Applied Data Analytics'),
    ('HADAN','Bachelor of Applied Data Analytics (Honours)'),
    ('BBIOT','Bachelor of Biotechnology'),
    ('HBIOT','Bachelor of Biotechnology (Honours)'),
    ('AENGI','Bachelor of Engineering (Honours)'),
    ('AENRD','Bachelor of Engineering (R&D) (Honours)'),
    ('BENSU','Bachelor of Environment and Sustainability'),
    ('HENSU','Bachelor of Environment and Sustainability (Honours)'),
    ('AENSU','Bachelor of Environment and Sustainability Advanced (Honours)'),
    ('HENVS','Bachelor of Environemntal Studies'),
    ('BGENE','Bachelor of Genetics'),
    ('HGENE','Bachelor of Genetics (Honours)'),
    ('BHLTH','Bachelor of Health Science (Honours)'),
    ('BIT','Bachelor of Information Technology'),
    ('HIT','Bachelor of Information Technology (Honours)'),
    ('BMASC','Bachelor of Mathematical Sciences'),
    ('HMASC','Bachelor of Mathematical Sciences (Honours)'),
    ('BMEDS','Bachelor of Medical Science'),
    ('HMEDS/HMDSA','Bachelor of Medical Science (Honours)'),
    ('PHBSCIENCE', 'PhB/Bachelor of Philosophy (Honours) in Science'),
    ('APSYC','Bachelor of Psychology (Honours)'),
    ('BSC','Science'),
    ('HSC','Bachelor of Science (Honours)'),
    ('ASCAD','Bachelor of Science (Advanced) (Honours)'),
    ('BSPSY','Science (Psychology)'),
    ('HSPSY','Bachelor of Science (Psychology) (Honours)'),
    ('ASENG','Bachelor of Software Engineering (Honours)'),
    ('ESCIE','Diploma of Science'),
    ('ECOMP','Diploma of Computing'),
    ('PHD','PhD/Doctor of Philosophy'),
    ('GDCP','Graduate Diploma of Computing'),
    ('MCOMP','Master of Computing'),
    ('VCOMP','Master of Computing (Advanced)'),
    ('MADAN','Master of Applied Data Analytics'),
    ('NDSTE','Master of Engineering in Digital Systems and Telecommunications'),
    ('NMECH','Master of Engineering in Mechatronics'),
    ('NENPH','Master of Engineering in Photonics'),
    ('NENRE','Master of Engineering in Renewable Energy'),
    ('MHCD','Doctor of Medicine and Surgery'),
    ('CSCIE','Graduate Certificate of Science'),
    ('DENVI','Graduate Diploma of Environment'),
    ('GDSCI','Graduate Diploma of Science'),
    ('VASTP','Master of Astronomy and Astrophysics (Advanced)'),
    ('MBIOS','Master of Biological Sciences'),
    ('VBIOS','Master of Biological Sciences (Advanced)'),
    ('MBIOT','Master of Biotechnology'),
    ('VBIOT','Master of Biotechnology (Advanced)'),
    ('MCPSY','Master of Clinical Psychology'),
    ('VEASC','Master of Earth Sciences (Advanced)'),
    ('MENCH','Master of Energy Change'),
    ('VENCH','Master of Energy Change (Advanced)'),
    ('MENVI','Master of Environment'),
    ('VENVI','Master of Environment (Advanced)'),
    ('MENVS','Master of Environemntal Science'),
    ('VENVS','Master of Environemntal Science (Advanced)'),
    ('MFORE','Master of Forestry'),
    ('VFORE','Master of Forestry (Advanced)'),
    ('VMASC','Master of Mathematical Sciences (Advanced)'),
    ('MNEUR','Master of Neuroscience'),
    ('VNEUR','Master of Neuroscience (Advanced)'),
    ('MNUCL','Master of Nuclear Science'),
    ('MPUBH','Master of Public Health'),
    ('VPUBH','Master of Public Health (Advanced)'),
    ('MSCHK','Master of Science Communication'),
    ('MSCO','Master of Science Communication Outreach'),
    ('MSCAU','Master of Science in Science Communication'),
)

# This will be used in case someone is doing a double degree
# The second degree can either be STEM or non-STEM
DEGREE_PROGRAMME_2 = (
    ('','-'),
    ('AACOM','Bachelor of Advanced Computing (Honours)'),
    ('AACRD','Bachelor of Advanced Computing (R&D) (Honours)'),
    ('BADAN','Bachelor of Applied Data Analytics'),
    ('HADAN','Bachelor of Applied Data Analytics (Honours)'),
    ('BBIOT','Bachelor of Biotechnology'),
    ('HBIOT','Bachelor of Biotechnology (Honours)'),
    ('AENGI','Bachelor of Engineering (Honours)'),
    ('AENRD','Bachelor of Engineering (R&D) (Honours)'),
    ('BENSU','Bachelor of Environment and Sustainability'),
    ('HENSU','Bachelor of Environment and Sustainability (Honours)'),
    ('AENSU','Bachelor of Environment and Sustainability Advanced (Honours)'),
    ('HENVS','Bachelor of Environemntal Studies'),
    ('BGENE','Bachelor of Genetics'),
    ('HGENE','Bachelor of Genetics (Honours)'),
    ('BHLTH','Bachelor of Health Science (Honours)'),
    ('BIT','Bachelor of Information Technology'),
    ('HIT','Bachelor of Information Technology (Honours)'),
    ('BMASC','Bachelor of Mathematical Sciences'),
    ('HMASC','Bachelor of Mathematical Sciences (Honours)'),
    ('BMEDS','Bachelor of Medical Science'),
    ('HMEDS/HMDSA','Bachelor of Medical Science (Honours)'),
    ('PHBSCIENCE', 'PhB/Bachelor of Philosophy (Honours) in Science'),
    ('APSYC','Bachelor of Psychology (Honours)'),
    ('BSC','Science'),
    ('HSC','Bachelor of Science (Honours)'),
    ('ASCAD','Bachelor of Science (Advanced) (Honours)'),
    ('BSPSY','Science (Psychology)'),
    ('HSPSY','Bachelor of Science (Psychology) (Honours)'),
    ('ASENG','Bachelor of Software Engineering (Honours)'),
    ('ESCIE','Diploma of Science'),
    ('ECOMP','Diploma of Computing'),
    ('PHD','PhD/Doctor of Philosophy'),
    ('GDCP','Graduate Diploma of Computing'),
    ('MCOMP','Master of Computing'),
    ('VCOMP','Master of Computing (Advanced)'),
    ('MADAN','Master of Applied Data Analytics'),
    ('NDSTE','Master of Engineering in Digital Systems and Telecommunications'),
    ('NMECH','Master of Engineering in Mechatronics'),
    ('NENPH','Master of Engineering in Photonics'),
    ('NENRE','Master of Engineering in Renewable Energy'),
    ('MHCD','Doctor of Medicine and Surgery'),
    ('CSCIE','Graduate Certificate of Science'),
    ('DENVI','Graduate Diploma of Environment'),
    ('GDSCI','Graduate Diploma of Science'),
    ('VASTP','Master of Astronomy and Astrophysics (Advanced)'),
    ('MBIOS','Master of Biological Sciences'),
    ('VBIOS','Master of Biological Sciences (Advanced)'),
    ('MBIOT','Master of Biotechnology'),
    ('VBIOT','Master of Biotechnology (Advanced)'),
    ('MCPSY','Master of Clinical Psychology'),
    ('VEASC','Master of Earth Sciences (Advanced)'),
    ('MENCH','Master of Energy Change'),
    ('VENCH','Master of Energy Change (Advanced)'),
    ('MENVI','Master of Environment'),
    ('VENVI','Master of Environment (Advanced)'),
    ('MENVS','Master of Environemntal Science'),
    ('VENVS','Master of Environemntal Science (Advanced)'),
    ('MFORE','Master of Forestry'),
    ('VFORE','Master of Forestry (Advanced)'),
    ('VMASC','Master of Mathematical Sciences (Advanced)'),
    ('MNEUR','Master of Neuroscience'),
    ('VNEUR','Master of Neuroscience (Advanced)'),
    ('MNUCL','Master of Nuclear Science'),
    ('MPUBH','Master of Public Health'),
    ('VPUBH','Master of Public Health (Advanced)'),
    ('MSCHK','Master of Science Communication'),
    ('MSCO','Master of Science Communication Outreach'),
    ('MSCAU','Master of Science in Science Communication'),
    # Non-STEM degrees from here on
    ('ALLB','Bachelor of Laws (Honours)'),
    ('BACCT','Bachelor of Accounting'),
    ('BACTS','Bachelor of Actuarial Studies'),
    ('BBUSA','Bachelor of Business Administration'),
    ('BCOMM','Bachelor of Commerce'),
    ('BECON','Bachelor of Economics'),
    ('BFINN','Bachelor of Finance'),
    ('BINBS','Bachelor of International Business'),
    ('BSTAT','Bachelor of Statistics'),
    ('BASIA','Bachelor of Asian Studies'),
    ('BINSS','Bachelor of International Security Studies'),
    ('BPAST','Bachelor of Pacific Studies'),
    ('BARTS','Bachelor of Arts'),
    ('BCLAS','Bachelor of Classical Studies'),
    ('BCRIM','Bachelor of Criminology'),
    ('BDESN','Bachelor of Design'),
    ('BDEVS','Bachelor of Developmental Studies'),
    ('BIR','Bachelor of International Relations'),
    ('BLANG','Bachelor of Languages'),
    ('BPOLS','Bachelor of Policy Studies'),
    ('BPLSC','Bachelor of Political Science'),
    ('BPPE','Bachelor of Philosophy, Politics and Economics'),
    ('BVART','Bachelor of Visual Arts'),
)

ROLES = (
    ('Mentee', 'Mentee'),
    ('Mentor', 'Mentor'),
)

GENDER = (
    ('','-'), #error-checking st. "-" isn't a valid answer
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
    ('Prefer not to say', 'Prefer not to say'),
)

MENTOR_GENDER = (
    ('Definitely', 'Definitely'),
    ('If possible', 'If possible'),
    ('Unconcerned', 'Unconcerned'),
)

MEDIUM_OF_INTERACTION = (
    ('','-'),
    ('Online', 'Online'),
    ('In person', 'In person'),
    ('Both', 'Both')
)

class Profile(models.Model):
    role = models.CharField(max_length=15, null = True ,choices=ROLES)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uniId = models.CharField(max_length=100)
    university = models.CharField(max_length=100, choices=UNIVERSITY, null=True, blank=False)
    study_year = models.CharField(max_length=100,choices=YEAR_OF_STUDY, blank=False)
    degree_programme = models.CharField(max_length=50, null = True ,blank=False,choices=STEM_DEGREE_PROGRAMME)
    degree_programme_2 = models.CharField(max_length=50, null = True ,choices=DEGREE_PROGRAMME_2)
    degree_major = models.CharField(max_length=50, null = True)
    gender = models.CharField(max_length=15, null = True ,choices=GENDER)
    mentor_gender = models.CharField(max_length=15, null = True ,choices=MENTOR_GENDER)
    why_mentor = models.CharField(max_length=150, null = True)
    why_div_equ_inc = models.CharField(max_length=150, null = True)
    mentee_number = models.IntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(3)])
    hear_about = models.CharField(max_length=150, null = True)
    paired_with = models.CharField(max_length=50, null = True, blank = True)
    paired_with2 = models.CharField(max_length=50, null = True, blank = True) # Added second paired_with
    paired_with3 = models.CharField(max_length=50, null = True, blank  = True) # Added third paired_with
    medium_interaction = models.CharField(max_length=50, null=True, choices=MEDIUM_OF_INTERACTION)
    mentee_number_remaning = models.IntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(3)],null = True) # Added mentee numbers remaining


    def __str__(self):
       return str(self.role)+ " "+ str(self.uniId)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
