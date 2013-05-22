from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views

from darkoob.social import views as social_views
from darkoob.social.forms import AuthenticationFormPlaceholder

urlpatterns = patterns('',
    url(r'^home/', social_views.home, name='home'),
    url(r'^signup/$', social_views.signup, name='signup'),
    url(r'^login/$', auth_views.login,
        {'template_name': 'social/login.html',
         'authentication_form': AuthenticationFormPlaceholder
        }, name='login'),
    url(r'^logout/$', auth_views.logout_then_login, name='logout'),
    url(r'^change_password/$', social_views.change_password, name='change_password'),
    url(r'^profile/$', social_views.profile, name='profile'),


    url(r'^accounts/password/reset/$', 'django.contrib.auth.views.password_reset', 
        {'post_reset_redirect' : '/accounts/password/reset/done/'}, name='reset_pass'),
    url(r'^accounts/password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^accounts/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/accounts/password/done/'}),
    url(r'^accounts/password/done/$', 'django.contrib.auth.views.password_reset_complete'),


)
