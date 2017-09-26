from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from content.models import Post, Mentee, Mentor, Training
from blog.models import Post
from webcore.models import Profile, Xpairs
from feedback.forms import FeedbackForm
from feedback.models import Feedback_contact
from django.utils import timezone
#from content

# Create your views here.
def home(request):
    context = locals()
    template = 'index.html'
    return render(request,template,context)

@login_required
def userProfile(request):
    user = request.user
    context = {'user':user}
    template = 'menteelogin.html'
    return render(request,template,context)

@login_required
def userProfileNews(request):
    user = request.user
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    template = 'blog/post_list.html'
    return render(request,template, {'posts': posts})

## post_detail views the blog posts individually
@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    template = 'blog/post_detail.html'
    return render(request, template, {'post': post})


@login_required
def userProfileMentor(request):
    user = request.user
    template = 'mentor.html'
    return render(request,template)

@login_required
def userProfileResources(request):
    user = request.user
    context = {'user':user, 'post_list':Post.objects.all(), 'mentee_list':Mentee.objects.all(), 'mentor_list':Mentor.objects.all(), 'training_list':Training.objects.all()}
    template = 'resources.html'
    return render(request,template,context)

@login_required
def userProfileFAQ(request):
    user = request.user
    context = {'user':user}
    template = 'FAQ.html'
    return render(request,template,context)

@login_required
def userProfileProfile(request):
    user = request.user
    context = {'user':user}
    template = 'profile.html'
    return render(request,template,context)

@login_required
def userProfileContent(request):
    user = request.user
    context = {'user':user, 'mentee_list':Mentee.objects.all()}
    template = 'content.html'
    return render(request,template,context)

@login_required
def userProfileSettings(request):
    user = request.user
    context = {'user':user}
    template = 'settings.html'
    return render(request,template,context)

@login_required
def feedback_process(request):
    User = get_object_or_404(Profile, pk=request.user.pk)
    contact_template = 'feedback/feedback_contact.html'
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
