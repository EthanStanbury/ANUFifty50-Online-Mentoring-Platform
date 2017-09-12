from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback_contact
from webcore.models import Profile

# #the function executes with the signup url to take the inputs
# def feedback_process(request):
#     contact_template = 'feedback_contact.html'
#     # sucess_template = 'thanks.html'
#
#     if request.method == 'POST':  # if the form has been filled
#
#         form = Feedback_contact(request.POST)
#
#         # creating an feedback contact object containing all the data
#         form = FeedbackForm(request.user)
#         # It should return an HttpResponse.
#         form.send_email()
#         # saving all the data in the current object into the database
#         form.save()
#
#     else:
#         form = FeedbackForm()  # an unboundform
#
#     return render(request, contact_template, {'feedback_form': form})


def feedback_process(request):
    contact_template = 'feedback_contact.html'
    # sucess_template = 'thanks.html'

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FeedbackForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            feedback_form = form.save(commit=False)
            feedback_form.user = User.objects.get(user=request.user)  # use your own profile here
            feedback_form.save()
            # return HttpResponseRedirect(self.get_success_url())
        # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FeedbackForm(request)

    return render(request, contact_template, {'form': form})