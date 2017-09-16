
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.conf import settings

from webcore.models import Profile
from .forms import FeedbackForm
from .models import Feedback_contact


def feedback_process(request):
    User = get_object_or_404(Profile, pk=request.user.pk)
    contact_template = 'feedback_contact.html'
    # sucess_template = 'thanks.html'

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FeedbackForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            receiver_email = settings.EMAIL_HOST_USER
            subject = form.subject(User.role)
            message = form.cleaned_data['message']

            # handle email eceptions
            try:
                send_mail(subject, message, request.user.email, [receiver_email])
            except Exception as ex:
                data = messages.add_message(request, messages.ERROR,'An error occurred. {}'.format(str(ex)))
            else:
                feedback_form = form.save(commit=False)
                # feedback_form.receiver_email = receiver_email
                feedback_form.user = User
                feedback_form.save()
                data = messages.add_message(request, messages.INFO, 'Thanks for sending a feedback.')

            # render thank you message
            return  render(request, contact_template, {'message': data})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FeedbackForm(user=User.user)

    return render(request, contact_template, {'form': form})