from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.contrib import admin

import datetime
now = datetime.datetime.now()

class Groups(models.Model):
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return "%s" % self.name

class usergroups(models.Model):
    userid = models.ForeignKey(User, on_delete=models.PROTECT)
    groupid = models.ManyToManyField(Groups)

    def __str__(self):
        return "%s" % self.user

class useredits(models.Model):
    userid = models.ForeignKey(User, on_delete=models.PROTECT)
    editinguser = models.ManyToManyField('elidgbleusers', db_column='username')

    def __str__(self):
        return "%s" % self.userid

class elidgbleusers(models.Model):
    username = models.CharField(max_length=100)
    userdisplay = models.CharField(max_length=250)

    def __str__(self):
        return "%s" % self.userdisplay

class office_values(models.Model):
    office = models.CharField(max_length=100, unique=True)
    state = models.CharField(max_length=2)
    agency = models.CharField(max_length=75)

    def __str__(self):
        return "%s" % self.office

class userprofile(models.Model): 
    User = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True, unique=True)
    User_Phone_Number = models.CharField(max_length=15)
    Agency = models.CharField(max_length=50)
    Field_Office = models.CharField(max_length=100)
    Approving_Official = models.CharField(max_length=50)
    Date_Approved = models.DateTimeField()
    Waiver_V2_Approved = models.IntegerField(default=0)
    Date_V2_Waiver_Approved = models.DateTimeField()
    Waiver_Approved = models.IntegerField(default=0)
    Date_Waiver_Approved = models.DateTimeField()
    User_Approved = models.IntegerField(default=0)
    Attempts_Remaining = models.IntegerField(default=3)

    def __str__(self):
        return "%s" % self.User

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        userprofile.objects.create(User=instance)

post_save.connect(create_user_profile, sender=User)


