from django.conf.urls import url
from . import views

app_name = 'feedback'

urlpatterns = [

    # /profile/contact:url to take the feedback form
    url(r'^$', views.feedback_process, name='feedback_process'),
    # url(r'^mentee_fedback$', views.feedback_process, name='feedback_form'),
    # url(r'^mentor_fedback$', views.feedback_process, name='feedback_form'),
]
