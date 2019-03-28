from django.conf.urls import *
from welcome import views

urlpatterns = [


	### Home Page URLs
    url(r'^$', views.index, name='index'),

    ### News Page URLs
    url(r'news/$', views.news, name='news'),

    ###FAQ URLs
    url(r'faq/$', views.faq, name='faq'),

    ###FAQ URLs
    url(r'help/$', views.help, name='help'),

    ### State Module Page URLs
    url(r'statemods/$', views.statemods, name='statemods'),

    ### Decision Support Tool Page URLs
    url(r'dst/$', views.dst, name='dst'),

    ### About Page URLs
    url(r'about/$', views.about, name='about'),

    ### Temp Under Construction URLs
    url(r'under_construction/$', views.under_construction, name='under_construction'),
    
    ]