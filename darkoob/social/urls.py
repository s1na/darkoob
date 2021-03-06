from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views

from darkoob.social import views as social_views
from darkoob.social.forms import AuthenticationFormPlaceholder

urlpatterns = patterns('',
    url(r'^home/$', social_views.home, name='home'),
    url(r'^home/stream/$', social_views.home_stream, name='home_stream'),
    url(r'^signup/$', social_views.signup, name='signup'),
    url(r'^login/$', auth_views.login,
        {'template_name': 'social/login.html',
         'authentication_form': AuthenticationFormPlaceholder
        }, name='login'),
    url(r'^logout/$', auth_views.logout_then_login, name='logout'),
    url(r'^change_password/$', social_views.change_password, name='change_password'),
    url(r'^profile/$', social_views.profile, name='profile'),

    url(r'^password/reset/$', auth_views.password_reset, 
        {'post_reset_redirect': 'password/reset/done/'}, name='reset_pass'),
    url(r'^password/reset/done/$', auth_views.password_reset_done),
    url(r'^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm, 
        {'post_reset_redirect': 'password/done/'}),
    url(r'^password/done/$', auth_views.password_reset_complete),

    url(r'^post/new/$', social_views.new_post, name='new_post'),
    url(r'^user/(?P<username>\w+)/$', social_views.user_profile, name='user_profile'),

    url(r'^user/(?P<username>\w+)/following$', social_views.user_following, name='user_following'),
    url(r'^user/(?P<username>\w+)/followers$', social_views.user_followers, name='user_followers'),
    url(r'^user/(?P<username>\w+)/favorite_books$', social_views.user_favorite_books, name='user_favorite_books'),

    url(r'^profile/followers/$', social_views.followers, name='followers'),
    url(r'^profile/following/$', social_views.following, name='following'),
    url(r'^profile/favorite_books$', social_views.favorite_books, name='favorite_books'),
)
