#from django import forms
import datetime
from django import forms
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError

from .models import Feedback_contact


class FeedbackForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        # print self.request
        self.request = request

        # Call super() after deleting the extra kwargs.
        super(FeedbackForm, self).__init__(*args, **kwargs)

        if self.request.user.is_authenticated():
            user = User.objects.get(pk=self.request.user.pk)
            self.fields['first_name'].initial = user.username
            self.fields['first_name'].widget.attrs['readonly'] = str(user.username.strip()) is not ''
            self.fields['last_name'].initial = user.last_name
            self.fields['last_name'].widget.attrs['readonly'] = str(user.last_name.strip()) is not ''

    class Meta:
        model = Feedback_contact
        fields = ('first_name', 'last_name', 'subject')
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "subject": "Subject"
        }
        widgets = {
            "first_name": forms.TextInput(attrs={'placeholder': 'Your First Name ...', 'id': 'fname', 'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'placeholder': 'Your Last Name ...', 'id': 'lname', 'class': 'form-control'}),
            "subject": forms.Textarea(attrs={'placeholder': 'Subject ...', 'id': 'subject', 'class': 'form-control'}),
        }