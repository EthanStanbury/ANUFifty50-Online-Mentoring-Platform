"""fifty_fifty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from webcore import views
from allauth.account.views import PasswordResetView
from django.views.generic.base import TemplateView

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^profile/$', views.userProfile, name='profile'),
    url(r'^profile/content.html', views.userProfileContent, name='profileContent'),
    url(r'^profile/blog/post_list.html', views.userProfileNews, name='profileNews'),
    #url(r'^profile/news.html', views.userProfileNews, name='profileNews'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^profile/mentor.html', views.userProfileMentor, name='profileMentor'),
    url(r'^profile/resources.html', views.userProfileResources, name='profileResources'),
    url(r'^profile/FAQ.html', views.userProfileFAQ, name='profileFAQ'),
    url(r'^profile/profile.html', views.userProfileProfile, name='profileProfile'),
    url(r'^profile/menteelogin.html', views.userProfile, name='profile'),
    url(r'^profile/feedback/feedback_contact.html', views.feedback_process, name='feedback_process'),
    url(r'^profile/contact_form/contact_form.html', include('contact_form.urls')),
    #url(r'^profile/contact_form/sent/', include('contact_form.urls')),
    url(r'^profile/settings.html', views.userProfileSettings, name='profileSettings'),
    #url(r'^profile/contact', include('feedback.urls')),
    url(r'^profile/feedback/form-to-email.php', views.feedback_process),
    url(r'^accounts/password/reset', PasswordResetView.as_view(template_name='password_reset.html')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^content/', include('content.urls')),
    url(r'^feedback/', include('feedback.urls')),
    url(r'', include('blog.urls')),
    url(r'^contact/sent/$',
        TemplateView.as_view(
            template_name='contact_form/contact_form_sent.html'
        ),
        name='contact_form_sent'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
