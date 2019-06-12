from django.conf.urls import *
from accounts import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout

urlpatterns = [
    ###Login URLs
    url(r'^login_user/$', views.login_user, name='login_user'),
    # url(r'^login/$', views.login, name='login'),

    ### Login URLs
    url(r'^loginpage/$', views.loginpage, name='loginpage'),

    ### Logout URLs
    # url(r'^logout/$', auth_views.logout, {'template_name': 'accounts/logout.html'}, name='logout'), #Python 2.7
    url(r'^logoutpage/$', views.logoutpage, name='logoutpage'),

    ### Lockout URLs
    url(r'^locked_reqsub/$', views.locked_reqsub, name='locked_reqsub'),
    url(r'^locked/$', views.locked, name='locked'),

    ### User Profile URLs
    url(r'^profile/$', views.ProfUp_Main, name='profile_main'),

    url(r'^profile_useredits/$', views.profile_useredits, name='profile_useredits'),

    url(r'^profile_success/$', views.profile_success, name='profile_success'),

    url(r'^email_success/$', views.email_success, name='email_success'),

    ### Manage User URLs
    url(r'^viewusers/$', views.viewusers, name='viewusers'),

    url(r'(?P<prid>\d+)/edituser/$', views.edituser, name='edituser'),

    url(r'^profile_edit_success/$', views.profile_edit_success, name='profile_edit_success'),

    url(r'^viewallusers/$', views.viewallusers, name='viewallusers'),

    url(r'(?P<prid>\d+)/manageuser/$', views.manageuser, name='manageuser'),

    url(r'^profile_manage_success/$', views.profile_manage_success, name='profile_manage_success'),

    # url(r'^password_change/$', auth_views.password_change, name='password_change'), #python 2.7
    url(r'^password_change/$', auth_views.PasswordChangeView, name='password_change'),

    # url(r'^password_change_done/$', auth_views.password_change_done, name='password_change_done'), #python 2.7
    url(r'^password_change_done/$', auth_views.PasswordChangeDoneView, name='password_change_done'),

    ### Password Reset URLs
    # url(r'^password/reset/$', auth_views.password_reset, name='password_reset_form'), #python 2.7
    url(r'^password/reset/$', auth_views.PasswordResetView.as_view(), name='password_reset_form'),

    # url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm,
    #     name='password_reset_confirm'), #python 2.7
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.PasswordResetConfirmView,
        name='password_reset_confirm'),

    # url(r'^password/reset/complete/$', auth_views.password_reset_complete, name='password_reset_complete'), #python 2.7
    url(r'^password/reset/complete/$', auth_views.PasswordResetCompleteView, name='password_reset_complete'),

    # url(r'^password/reset/auth_password_reset_done/$', auth_views.password_reset_done, name='password_reset_done'), #python 2.7
    url(r'^password/reset/auth_password_reset_done/$', auth_views.PasswordResetDoneView, name='password_reset_done'),

    url(r'^accounts/', include('registration.backends.hmac.urls')),

    url(r'^logoutfirst/$', views.logoutfirst, name='logoutfirst'),
]
