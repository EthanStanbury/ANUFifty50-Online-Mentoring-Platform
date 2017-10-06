from django import forms
from .models import Pair


class PairForm(forms.ModelForm):

first_name = forms.CharField(error_messages={'required': 'Please let us know what to call you!'})
    class Meta:
        model = Pair
