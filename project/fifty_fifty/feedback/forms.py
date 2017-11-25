# from django import forms
import datetime
from django import forms
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError

from .models import Feedback_contact


class FeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        #     # Call super() after deleting the extra kwargs.
        super(FeedbackForm, self).__init__(*args, **kwargs)

        if self.user:
            self.fields['first_name'].initial = self.user.first_name
            self.fields['first_name'].widget.attrs['readonly'] = str(self.user.first_name) is not ''
            self.fields['last_name'].initial = self.user.last_name
            self.fields['last_name'].widget.attrs['readonly'] = str(self.user.last_name) is not ''
            self.fields['email'].initial = self.user.email
            self.fields['email'].widget.attrs['readonly'] = str(self.user.email) is not ''

    def subject(self, role):
        message = self.cleaned_data['first_name'] + " " + self.cleaned_data['last_name']
        return message + "-" + str(role) if role else message

    class Meta:
        model = Feedback_contact
        exclude = ('user',)
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email",
            "message": "Message"
        }
        widgets = {
            "first_name": forms.TextInput(
                attrs={'placeholder': 'Your First Name ...', 'id': 'fname', 'class': 'form-control'}),
            "last_name": forms.TextInput(
                attrs={'placeholder': 'Your Last Name ...', 'id': 'lname', 'class': 'form-control'}),
            "email": forms.TextInput(
                attrs={'placeholder': 'Your email ...', 'id': 'email', 'class': 'form-control'}),
            "message": forms.Textarea(attrs={'placeholder': 'Message ...', 'id': 'message', 'class': 'form-control'}),
        }
