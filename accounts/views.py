from django.shortcuts import render, render_to_response
from django_tables2 import RequestConfig
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from accounts.forms import *
from accounts.models import *
from ced_main.models import imp_party_values
from django.core.mail import send_mail
from accounts.tables import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import auth as passcheck
from django.shortcuts import redirect
from django.utils import timezone
import datetime
from django.views.decorators.clickjacking import xframe_options_sameorigin
now = datetime.datetime.utcnow()
now = now.replace(tzinfo=timezone.utc)

from django.conf import settings
DEFAULT_FROM_EMAIL = settings.DEFAULT_FROM_EMAIL

class ValidatingPasswordChangeForm(passcheck.forms.PasswordChangeForm):
    MIN_LENGTH = 8

    def clean_new_password1(self):
        password1 = self.cleaned_data.get('new_password1')

        # At least MIN_LENGTH long
        if len(password1) < self.MIN_LENGTH:
            raise forms.ValidationError("The new password must be at least %d characters long." % self.MIN_LENGTH)

        # At least one letter and one non-letter
        first_isalpha = password1[0].isalpha()
        if all(c.isalpha() == first_isalpha for c in password1):
            raise forms.ValidationError("The new password must contain at least one letter and at least one digit or" \
                                        " punctuation character.")

        # ... any other validation you want ...

        return password1

def checkgroup(appoff):
    authority = 'none'
    try:
        for app in appoff:
            if app == 'Data Entry' or app == 'Bulk Uploaders' or app == 'Approving Officials' or app == 'Administrators':
                if app == 'Administrators':
                    return 'authenadmin'
                if app == 'Approving Officials':
                    return 'authenapp'
    except:
        return 'none'

def useraccess(request):
    try:
        access = tbl_userprofile.objects.values_list('user_type',flat=True).get(user_id=int(str(request.user.id)))
    except:
        access = 'denied'
    return access

def userapproved(request):
    try:
        approved = tbl_userprofile.objects.values_list('supervisor_approved',flat=True).get(user_id=int(str(request.user.id)))
    except:
        approved = 'denied'    
    return approved

def loginpage(request):
    useraccesslev = useraccess(request)
    if request.method == 'POST':
        # username = request.POST['username']
        if '@' in request.POST['username']:
            username = User.objects.values_list('username').get(email=str(request.POST['username']))
        else:
            try:
                username = User.objects.values_list('username').get(username=str(request.POST['username'])) #request.POST['username']
            except:
                username = 'None'
        username = str(username).replace("(u'","")
        username = str(username).replace("',)","")
        username = str(username).replace("('","")

        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if str(username) != 'None':
            userid = User.objects.values_list('id', flat=True).get(username=username)
            remainingleft = userprofile.objects.values_list('Attempts_Remaining', flat=True).get(User_id=userid)
            if remainingleft == 0:
                return redirect('/sgce/accounts/locked/')

        if str(user) != 'None':
            if user.is_active:
                auth_login(request, user)
                request.session['member_id'] = user.id

                obj1=userprofile.objects.get(User_id=userid)
                obj1.Attempts_Remaining = 3
                obj1.save()

                urlcheck = request.get_full_path()
                urlcheck = str(urlcheck)

                approved = userprofile.objects.values_list('Waiver_V2_Approved', flat=True).get(User_id=user.id)
                if approved == 0:
                    return redirect('/sgce/accounts/profile/')
                try:
                    urlcheck1 = urlcheck.split('?next=')[1]
                    return redirect(urlcheck1)
                except:
                    return redirect('/sgce')
            else:
                context = {'useraccess':useraccesslev, 'usepass':'Please activate your account'}
                return render(request, 'accounts/loginpage.html', context)
        else:
            isactive = User.objects.values_list('is_active', flat=True).get(username=username)
            if isactive == 0:
                context = {'useraccess':useraccesslev, 'usepass':'Account deactivated please contact the CED team'}

            else:

                obj1=userprofile.objects.get(User_id=userid)
                obj1.Attempts_Remaining = remainingleft - 1
                obj1.save()

                context = {'useraccess':useraccesslev, 'usepass':'Username or password is incorrect'}
            return render(request, 'accounts/loginpage.html', context)
    else:
        context = {'useraccess':useraccesslev, 'usepass':'None'}
        return render(request, 'accounts/loginpage.html', context)

@login_required
def logoutpage(request):
    auth_logout(request, user)
    return redirect('/welcome', context)

@login_required
def ProfUp_Main(request):
    siteurl = request.build_absolute_uri()
    siteurl1 = siteurl.split("/")
    siteurl2 = siteurl1[0] + "//" + siteurl1[2]
# Get the context from the request.
    profile = request.user
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    sf = userprofile.objects.get(pk=request.user.id)
    try:
        sfid = useredits.objects.get(userid_id=request.user.id)
    except:
        obj=useredits()
        obj.userid_id = request.user.id
        obj.save()
        sfid = useredits.objects.get(userid_id=request.user.id)

    sfid1 = User.objects.get(pk=request.user.id)

    
    if request.method == 'POST':
        # A HTTP POST?
        form = UserForm(request.POST, instance=profile)
        subform1 = profile_Form(request.POST, instance=sf)
        subform2 = useredits_form(request.POST, instance=sfid)
        # Have we been provided with a valid form?
        if form.is_valid() and subform1.is_valid() and subform2.is_valid():
            # if request.user.is_authenticated(): Pythoon 2.7
            if request.user.is_authenticated:
                # Save the new category to the database.
                form.save(commit=True)
                obj = subform1.save(commit=False)
                username = request.user.username
                try:
                    office = str(userprofile.objects.values_list('Field_Office',flat=True).get(pk=request.user.id))
                except:
                    office = "None"
                try:
                    agency = str(userprofile.objects.values_list('Agency',flat=True).get(pk=request.user.id))
                except:
                    agency = "None"
                if office == "DEMONSTRATION USER ACCESS ONLY" or username == "jwelty" or username == "Lief_Wiechman" or office == "" or office == "Null" or office == "None" or office == "---Select an Office---":
                    test = 'test'
                else:
                    obj.Field_Office = office
                    obj.Agency = agency

                if obj.Waiver_V2_Approved == 1:
                    if obj.Date_V2_Waiver_Approved == "" or obj.Date_V2_Waiver_Approved == None or obj.Date_V2_Waiver_Approved == "None":
                        obj.Date_V2_Waiver_Approved = now
                        obj.Waiver_V2_Approved = 1
                    else:
                        obj.Waiver_V2_Approved = 1
                else:
                    wavapp = userprofile.objects.values_list('Waiver_Approved',flat=True).get(pk=request.user.id)
                    if wavapp == 1:
                        obj.Waiver_V2_Approved = 1
                    else:
                        obj.Waiver_Approved = 0

                if obj.User_Approved == 1:
                    obj.User_Approved = 1
                else:
                    userapp = userprofile.objects.values_list('User_Approved',flat=True).get(pk=request.user.id)
                    if userapp == 1:
                        obj.User_Approved = 1
                    else:
                        obj.User_Approved = 0
                   

                if 'emailapp' in request.POST:
                    Subject = "Please approve " + request.user.first_name + " " + request.user.last_name
                    Message = "The user " + request.user.first_name + " " + request.user.last_name + " (username: " + request.user.username + ") has listed you as their approving official and is requesting they be given access to the Sage Grouse CED database to enter data.  Please login to the CED (" + siteurl2 + "/sgce/) and approve or decline their account."
                    From = DEFAULT_FROM_EMAIL
                    qresult = User.objects.values_list('email').get(username=obj.Approving_Official)
                    To = ""
                    for rst in qresult:
                        To = To + rst
                    send_mail(Subject, Message, From, [To], fail_silently=False)
                    obj.save()
                    context = {'authen':authen}
                    return redirect('/sgce/accounts/email_success', context)

                obj.save()
                # thcnt = 0

                # subform2.save_m2m(commit=True)
                thcnt = 0
                for level in request.POST.getlist('editinguser'):
                    obj2 = subform2.save(commit=False)

                    obj2.userid = sfid1
                    obj2.save()
                    thcnt = 1
                if thcnt == 1:
                    subform2.save_m2m()
                    obj2.save()
                # Now call the index() view.
                # The user will be shown the homepage.
                # return render(request, '/sgce/accounts/profile_success/')

                return redirect('/sgce/accounts/profile_success/')
        else:
            # The supplied form contained errors - just print them to the terminal.
            
            print(form.errors)
            print(subform1.errors)
            print(subform2.errors)

    else:
        # If the request was not a POST, display the form to enter details.
        form = UserForm(instance=profile)
        try:
            subform1 = profile_Form(initial = {
                    'Agency' : imp_party_values.objects.get(Implementation_Party=userprofile.objects.values_list('Agency', flat=True).get(User_id=request.user.id)),                   
                    'Approving_Official' : User.objects.get(username=userprofile.objects.values_list('Approving_Official', flat=True).get(User_id=request.user.id)),
                    }, instance=sf)
        except:
            subform1 = profile_Form(instance=sf)
        try:
            subform2 = useredits_form(instance=sfid)
        except:
            subform2 = useredits_form()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).

    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        context = {'form': form, 'subform1': subform1, 'subform2':subform2, 'authen':authen, 'showlogin':'True'}
        return render(request, 'accounts/profile.html', context)
    else:
        context = {'authen':authen, 'showlogin':'True'}
        return render(request, 'accounts/permission_denied.html', context)

@login_required
def viewusers(request):
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    profile = request.user.username
    table = viewuser_table(User.objects.filter(userprofile__Approving_Official=profile))
    RequestConfig(request).configure(table)
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        if authen == 'authenadmin' or authen == 'authenapp':
            context = {'viewusers': table, 'authen':authen}
            return render(request, 'accounts/viewusers.html', context)
        else:
            context = {'authen':authen}
            return render(request, 'accounts/permission_denied.html', context)

@login_required
def edituser(request, prid):
    profile = User.objects.get(pk=prid)
    sf = userprofile.objects.get(pk=prid)
    try:
        pid = usergroups.objects.get(userid=prid)
    except:
        NoGrp = "NoGrp"
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    # A HTTP POST?
    if request.method == 'POST':
        form = UsereditForm(request.POST, instance=profile)
        subform1 = profileedit_Form(request.POST, instance=sf)

        try:
            subform2 = profilegrp_edit(request.POST, instance=pid)
        except:
            subform2 = profilegrp_edit(request.POST)
        # subform2.user = prid
        # Have we been provided with a valid form?
        # Have we been provided with a valid form?

        if form.is_valid() and subform1.is_valid() and subform2.is_valid():
            # Save the new category to the database.
            for level in request.POST.getlist('groupid'):
                obj = subform2.save(commit=False)
                obj.userid = User.objects.get(pk=prid)
                obj.save()
                g = Group.objects.get(id=level) 
                g.user_set.add(User.objects.get(pk=prid))
            subform2.save_m2m()
            obj2 = form.save(commit=False)
            obj1 = subform1.save(commit=False)
            if obj1.User_Approved == 1 or obj1.User_Approved == 2:
                if obj1.Date_Approved == "" or obj1.Date_Approved == None or obj1.Date_Approved == "None":
                    obj1.Date_Approved = now
                obj1.save()
                obj2.save()
                if obj1.User_Approved == 1:
                    rqst = 'approved'
                else:
                    rqst = 'denied'
                Subject = "Your request to enter data in the CED has been " + rqst
                Message = "The approving official " + request.user.first_name + " " + request.user.last_name + " (username: " + request.user.username + ") has " + rqst + " your request to enter data into the CED.  If you feel your status is incorrect please contact your approving official at: " + request.user.email + " or email the CED directly at fw1sagegrouseced@fws.gov"
                From = DEFAULT_FROM_EMAIL
                qresult = User.objects.values_list('email').get(username=obj2.username)
                To = ""
                for rst in qresult:
                    To = To + rst
                send_mail(Subject, Message, From, [To], fail_silently=False)
            else:
                obj1.save()
                obj2.save()

            
            context = {'authen':authen}
            return redirect('/sgce/accounts/profile_edit_success/')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
            print(subform1.errors)
            print(subform2.errors)

    else:
        # If the request was not a POST, display the form to enter details.
        form = UsereditForm(instance=profile)
        subform1 = profileedit_Form(instance=sf)
        try:
            subform2 = profilegrp_edit(initial = {
                    'groupid' : usergroups.objects.values_list('groupid', flat=True).filter(userid=prid),
                    'userid' : User.objects.get(pk=prid)
                    }, instance=pid)
        except:
            subform2 = profilegrp_edit()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    if authen == 'authenadmin' or authen == 'authenapp':
        context = {'form': form, 'subform1': subform1, 'subform2': subform2, 'authen':authen}
        return render(request, 'accounts/editprofile.html', context)
    else:
        context = {'authen':authen}
        return render(request, 'accounts/permission_denied.html', context)

@login_required
def email_success(request):
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        if authen == 'authenadmin':
            context = {'authen':authen}
            return render(request, 'accounts/email_success.html', context)
        else:
            context = {'authen':authen}
            return render(request, 'accounts/permission_denied.html', context)

@login_required
def viewallusers(request):
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    table = viewalluser_table(User.objects.order_by('last_name', 'first_name').all())
    RequestConfig(request).configure(table)
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        if authen == 'authenadmin':
            context = {'viewallusers': table, 'authen':authen}
            return render(request, 'accounts/viewallusers.html', context)
        else:
            context = {'authen':authen}
            return render(request, 'accounts/permission_denied.html', context)



@login_required
def manageuser(request, prid):
    profile = User.objects.get(pk=prid)
    sf = userprofile.objects.get(pk=prid)
    conoffice = userprofile.objects.values_list('Field_Office', flat=True).get(User_id__exact=User.objects.values_list('id', flat=True).get(username__exact=request.user))
    try:
        pid = usergroups.objects.get(userid=prid)
    except:
        NoGrp = "NoGrp"
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    # A HTTP POST?
    if request.method == 'POST':
        if conoffice == 'Congress':
            return redirect('/sgce/readonly/')

        form = UsereditForm(request.POST, instance=profile)
        subform1 = profilemanage_Form(request.POST, instance=sf)
        try:
            subform2 = profilegrp_manage(request.POST, instance=pid)
        except:
            subform2 = profilegrp_manage(request.POST)
        # Have we been provided with a valid form?
        # Have we been provided with a valid form?

        if form.is_valid() and subform1.is_valid() and subform2.is_valid():
            # Save the new category to the database.
            for level in request.POST.getlist('groupid'):
                obj = subform2.save(commit=False)
                obj.userid = User.objects.get(pk=prid)
                obj.save()
                g = Group.objects.get(id=level) 
                g.user_set.add(User.objects.get(pk=prid))
            subform2.save_m2m()
            obj2 = form.save(commit=False)
            obj1 = subform1.save(commit=False)

            if obj1.User_Approved == 1 or obj1.User_Approved == 2:
                # if obj1.Date_Approved == "" or obj1.Date_Approved == None:
                obj1.Date_Approved = now
                obj1.save()
                obj2.save()
                if obj1.User_Approved == 1:
                    rqst = 'approved'
                else:
                    rqst = 'denied'
                Subject = "Your request to enter data in the CED has been " + rqst
                Message = "The approving official " + request.user.username + " has " + rqst + " your request to enter data into the CED.  If you feel your status is incorrect please contact your approving official at: " + request.user.email
                From = DEFAULT_FROM_EMAIL
                qresult = User.objects.values_list('email').get(username=obj2.username)
                To = ""
                for rst in qresult:
                    To = To + rst
                send_mail(Subject, Message, From, [To], fail_silently=False)
            else:
                obj1.save()
                obj2.save()
            context = {'authen':authen}
            return redirect('/sgce/accounts/profile_manage_success/')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
            print(subform1.errors)
            print(subform2.errors)

    else:
        # If the request was not a POST, display the form to enter details.
        form = UsereditForm(instance=profile)
        subform1 = profilemanage_Form(instance=sf)
        try:
            subform2 = profilegrp_manage(initial = {
                    'groupid' : usergroups.objects.values_list('groupid', flat=True).filter(userid=prid),
                    'userid' : User.objects.get(pk=prid)
                    }, instance=pid)
        except:
            subform2 = profilegrp_manage()


    # Render the form with error messages (if any).
    if authen == 'authenadmin':
        context = {'form': form, 'subform1': subform1, 'subform2': subform2, 'authen':authen}
        return render(request, 'accounts/manageuser.html', context)
    else:
        context = {'authen':authen}
        return render(request, 'accounts/permission_denied.html', context)

def logoutfirst(request):
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    context = {'authen':authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'accounts/logoutfirst.html', context)
    else:
        return render(request, 'accounts/permission_denied.html', context)

@xframe_options_sameorigin
def login_user(request):
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    context = {'authen':authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'accounts/logoutfirst.html', context)
    else:
        return render(request, 'accounts/login_user.html')

@login_required
def profile_success(request):
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    context = {'authen':authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'accounts/profile_success.html', context)
    else:
        return render(request, 'accounts/permission_denied.html', context)

@login_required
@xframe_options_sameorigin
def password_change(request):
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    context = {'authen':authen, 'showlogin':'True'}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        # return password_change(template_name='change_password.html', extra_context={'my_var1': 'my_var1'})
        return render(request, 'accounts/password_change.html', context)
    else:
        return render(request, 'accounts/permission_denied.html', context)

@login_required
def profile_edit_success(request):
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    context = {'authen':authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        if authen == 'authenadmin' or authen == 'authenapp':
            return render(request, 'accounts/profile_edit_success.html', context)
        else:
            return render(request, 'accounts/permission_denied.html', context)
    else:
        return render(request, 'accounts/permission_denied.html', context)

@login_required
def profile_manage_success(request):
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    context = {'authen':authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        if authen == 'authenadmin':
            return render(request, 'accounts/profile_manage_success.html', context)
        else:
            return render(request, 'accounts/permission_denied.html', context)
    else:
        return render(request, 'accounts/permission_denied.html', context)


def locked(request):
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    context = {'authen':authen}
    if request.method == 'POST':
        useremail = request.POST['email']
        Subject = "Reset password request"
        Message = "The user " + useremail +" has requested their account be unlocked."
        From = DEFAULT_FROM_EMAIL
        qresult = 'jwelty@usgs.gov'
        To = ""
        for rst in qresult:
            To = To + rst

        send_mail(Subject, Message, From, [To], fail_silently=False)
        return render(request, 'accounts/locked_reqsub.html', context)
    else:
        # if request.user.is_authenticated(): Pythoon 2.7
        if request.user.is_authenticated:
            return render(request, 'accounts/permission_denied.html', context)
        else:
            return render(request, 'accounts/locked.html', context)

def locked_reqsub(request):
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    context = {'authen':authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'accounts/permission_denied.html', context)
    else:
        return render(request, 'accounts/locked_reqsub.html', context)

def password_reset_form(request):
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    context = {'authen':authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'accounts/permission_denied.html', context)
    else:
        return render(request, 'accounts/password_reset_form.html', context)

def profile_useredits(request):
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    context = {'authen':authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'accounts/profile_useredits.html', context)
    else:
        return render(request, 'accounts/password_reset_main.html', context)