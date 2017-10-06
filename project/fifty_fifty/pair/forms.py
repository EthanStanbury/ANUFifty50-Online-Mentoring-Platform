from django import forms
from .models import Pair


class PairForm(forms.ModelForm):

    class Meta:
        model = Pair
        fields = ['name', 'mentor', 'mentee']


    def clean(self):
        cleaned_data = super(PairForm, self).clean()
        check = Pair.objects.filter(mentor=cleaned_data['mentor'], mentee=cleaned_data['mentee'])
        if check:
            return self.add_error('mentor', 'Mentor and Mentee combination already exists.')
