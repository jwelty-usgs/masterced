from django.conf.urls import *
from grsgmap import views

urlpatterns = [
    ### Home Page URLs
    url(r'^$', views.index, name='index'),
    url(r'^CEDPSummary/$', views.CEDPSummary, name='CEDPSummary'),
    url(r'^(?P<prid>\d+)/footprinteditor/$', views.footprinteditor, name='footprinteditor'),
]
