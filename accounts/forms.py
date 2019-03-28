#from django import forms
from django import forms as s
from django.contrib import auth
from django.contrib.auth.models import User, Group
from accounts.models import *
from passwords.fields import PasswordField
from ced_main.models import imp_party_values
from phonenumber_field.modelfields import PhoneNumberField

WavCHOICES = (('1', 'Accept',), ('2', 'Decline',))
UserApproved = (('1', 'Approve User',), ('0', 'Decline User',))

class HorizontalRadioRenderer(s.RadioSelect):
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        css_style = 'style="display: inline-block; margin-right: 10px;"'
        self.renderer.inner_html = '<li ' + css_style + '>{choice_value}{sub_widgets}</li>'

appoffsget = User.objects.filter(id__in=usergroups.objects.values_list('userid', flat=True).filter(groupid=1))
appoffs = []
appoffs.append(["","---Select an Agency---"])
appoffs.append(["","---Select an Office---"])
appoffs.append(["","---Select an Approving Official---"])

for app in appoffsget:
    name = User.get_full_name(app)
    agency = userprofile.objects.values_list('Agency', flat=True).get(User_id=app)
    useroffice = userprofile.objects.values_list('Field_Office', flat=True).get(User_id=app)
    name1 = str(name) + ", User: " + str(app) + ", Agency: " + agency + ", Field_Office: " + useroffice
    appoffs.append([str(app),str(name1)])

officesget = office_values.objects.values_list('office', flat=True).all().order_by('office')
offices = []
for off in officesget:

    state = office_values.objects.values_list('state', flat=True).get(office=off)
    agency = office_values.objects.values_list('agency', flat=True).get(office=off)
    if str(off) == '---Select an Agency---' or str(off) == '---Select an Office---':
        name =str(off)
    else:
        name =str(off) + ", " + str(state) + ", " + str(agency)
    offices.append([str(off),str(name)])

def createeditlist():
    editusersget = User.objects.all()
    editusers = []
    for edi in editusersget:
        try:
            approve = userprofile.objects.values_list('User_Approved', flat=True).get(User=edi)

            if approve == 1:
                name = User.get_full_name(edi)
                useragency = userprofile.objects.values_list('Agency', flat=True).get(User=edi)
                useroffice = userprofile.objects.values_list('Field_Office', flat=True).get(User=edi)
                name1 =str(name) + " (User: " + str(edi) + "), " + str(useragency) + ", " + str(useroffice)
                usid = userprofile.objects.get(User=edi)
                try:
                    checkadd = elidgbleusers.objects.get(username=str(usid))
                    if checkadd == "" or checkadd == None or checkadd == "None":
                        obj = elidgbleusers()
                        obj.username = str(usid)
                        obj.userdisplay = str(name1)
                        obj.save()
                except:
                    obj = elidgbleusers()
                    obj.username = str(usid)
                    obj.userdisplay = str(name1)
                    obj.save()

                editusers.append([str(usid),str(name1)])

                
        except:
            NoAdd = "DoNotAdd"
    return editusers


    
class USPhoneNumberMultiWidget(s.MultiWidget):
    """
    A Widget that splits US Phone number input into three <input type='text'> boxes.
    """
    def __init__(self,attrs=None):
        widgets = (
            s.TextInput(attrs={'size':'2','maxlength':'3', 'class':'phone'}),
            s.TextInput(attrs={'size':'2','maxlength':'3', 'class':'phone'}),
            s.TextInput(attrs={'size':'3','maxlength':'4', 'class':'phone'}),
        )
        super(USPhoneNumberMultiWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split('-')
        return (None,None,None)

    def value_from_datadict(self, data, files, name):
        value = [u'',u'',u'']
        # look for keys like name_1, get the index from the end
        # and make a new list for the string replacement values
        for d in filter(lambda x: x.startswith(name), data):
            index = int(d[len(name)+1:]) 
            value[index] = data[d]
        if value[0] == value[1] == value[2] == u'':
            return None
        return u'%s-%s-%s' % tuple(value)


class UserForm(s.ModelForm):
    username = s.CharField(widget=s.HiddenInput())
    first_name = s.CharField(label = 'First Name*', widget=s.TextInput(attrs={'size':'9'}))
    last_name = s.CharField(label = 'Last Name*', widget=s.TextInput(attrs={'size':'9'}))
    email = s.EmailField(label = 'Email Address*')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:

            self.fields['username'].widget.attrs['readonly'] = True
            self.fields['email'].widget.attrs['readonly'] = True

    def clean_sku(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.username
        else:
            return self.cleaned_data['username']


class profile_Form(s.ModelForm):

    User_Phone_Number = PhoneNumberField()
    Agency = s.ModelChoiceField(queryset=imp_party_values.objects.all().order_by('Implementation_Party'), label = "Agency/Conservation Partner*", required=False)
    Field_Office = s.ChoiceField(choices=offices, label = "Office/Name of Agency or Organization*", required=False)
    Waiver_V2_Approved = s.ChoiceField(widget=s.RadioSelect(), choices=WavCHOICES, label = "Terms of the CED V2.1 Agreement*", initial=0, required=False)
    Approving_Official = s.ChoiceField(choices=appoffs, label = "Approving Official*")
    User_Approved = s.BooleanField(widget=s.HiddenInput(), required=False, label='')
    Date_Approved = s.DateTimeField(label="Date User Approved", required=False)
    Date_V2_Waiver_Approved = s.DateTimeField(label="Date CED Version 2.1 Waiver Accepted", required=False)
    Attempts_Remaining = s.IntegerField(widget=s.HiddenInput(), required=False, label='')

     # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = userprofile
        fields = ('User_Phone_Number', 'Agency', 'Field_Office', 'Approving_Official', 'Date_Approved', 'Waiver_V2_Approved', 'Date_V2_Waiver_Approved')

    def __init__(self, *args, **kwargs):
        super(profile_Form, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:

            lock = userprofile.objects.values_list('Waiver_V2_Approved', flat=True).get(User_id=instance.pk)
            office = userprofile.objects.values_list('Field_Office', flat=True).get(User_id=instance.pk)
            username = User.objects.values_list('username', flat=True).get(id=instance.pk)

            if lock == 1:
                self.fields['Waiver_V2_Approved'].widget.attrs['disabled'] = True
                self.fields['Date_V2_Waiver_Approved'].widget.attrs['readonly'] = True

            self.fields['Date_Approved'].widget.attrs['readonly'] = True

            office = str(office)
            if office == "DEMONSTRATION USER ACCESS ONLY" or username == "jwelty" or username == "kathyhollar" or username == "Lief_Wiechman" or office == "" or office == "Null" or office == "None" or office == "---Select an Office---":
                test = "Test"
            else:
                if office > "":
                    self.fields['Agency'].widget.attrs['disabled'] = True
                    self.fields['Field_Office'].widget.attrs['disabled'] = True


    def clean_sku(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.User_Approved
        else:
            return self.cleaned_data['User_Approved']

class useredits_form(s.ModelForm):
    editinguser = s.ModelMultipleChoiceField(queryset=elidgbleusers.objects.none().order_by(), widget=s.CheckboxSelectMultiple, required=False, label = "Indicate Other Users Who Can Edit Your Project")

    class Meta:
        model = useredits
        fields = ('editinguser',)

    def __init__(self, *args, **kwargs):
        super(useredits_form, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:

            useroffice = userprofile.objects.values_list('Field_Office', flat=True).get(User_id=useredits.objects.values_list('userid', flat=True).get(id=instance.pk))
            useroffice = str(useroffice)
            useragency = userprofile.objects.values_list('Agency', flat=True).get(User_id=useredits.objects.values_list('userid', flat=True).get(id=instance.pk))
            useragency = str(useragency)
            edituser = []
            edituserid = []
            editusers = createeditlist()
            for editlist in editusers:
                if editlist[0] != str(instance):
                    office = editlist[1].split(", ")
                    officecheck = office[2]
                    if officecheck == useroffice:
                        edituser.append(editlist)
                        edituserid.append(editlist[0])

            for editlist1 in editusers:
                if editlist1[0] != str(instance):
                    agency = editlist1[1].split(", ")
                    agencycheck = agency[1]
                    if agencycheck == useragency:
                        if editlist1 not in edituser:
                            edituser.append(editlist1)
                            edituserid.append(editlist1[0])

            self.fields['editinguser'].queryset = elidgbleusers.objects.filter(username__in=edituserid).order_by()



class UsereditForm(s.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(UsereditForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['username'].widget.attrs['readonly'] = True
            self.fields['email'].widget.attrs['readonly'] = True
            self.fields['first_name'].widget.attrs['readonly'] = True
            self.fields['last_name'].widget.attrs['readonly'] = True

    def clean_sku(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.username
        else:
            return self.cleaned_data['username', 'email', 'first_name', 'last_name']


class profileedit_Form(s.ModelForm):
    Agency = s.CharField(label = "Agency")
    Field_Office = s.CharField(label = "Field Office")
    Approving_Official = s.CharField(label = "Approving Official")
    User_Approved = s.ChoiceField(widget=s.RadioSelect, choices=UserApproved, label='Do you approve this user?*')
    Date_Approved = s.DateTimeField(required=False)

     # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = userprofile
        fields = ('Agency', 'Field_Office', 'Approving_Official', 'User_Approved', 'Date_Approved')
        exclude = ('User_Level',)

    def __init__(self, *args, **kwargs):
        super(profileedit_Form, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['Agency'].widget.attrs['readonly'] = True
            self.fields['Field_Office'].widget.attrs['readonly'] = True
            self.fields['Approving_Official'].widget.attrs['readonly'] = True
            self.fields['Date_Approved'].widget.attrs['readonly'] = True

    def clean_sku(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.User_Approved
        else:
            return self.cleaned_data['Agency', 'Field_Office', 'Approving_Official', 'Date_Approved']

class profilegrp_edit(s.ModelForm):
    groupid = s.ModelMultipleChoiceField(queryset=Groups.objects.exclude(name='Approving Officials').exclude(name='Administrators'), widget=s.CheckboxSelectMultiple, label = "")

    class Meta:
        model = usergroups
        fields = ('groupid',)


class profilemanage_Form(s.ModelForm):
    Agency = s.CharField(label = "Agency")
    Field_Office = s.CharField(label = "Field Office")
    Approving_Official = s.CharField(label = "Approving Official")
    User_Approved = s.ChoiceField(widget=s.RadioSelect, choices=UserApproved, label='Approving Officials Only: Do You Approve This User?*')
    Date_Approved = s.DateTimeField(required=False)
    Attempts_Remaining = s.IntegerField(required=False, label='Attempts Remaining')

     # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = userprofile
        fields = ('Agency', 'Field_Office', 'Approving_Official', 'User_Approved', 'Date_Approved', 'Attempts_Remaining')

    def __init__(self, *args, **kwargs):
        super(profilemanage_Form, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['Agency'].widget.attrs['readonly'] = True
            self.fields['Field_Office'].widget.attrs['readonly'] = True
            self.fields['Approving_Official'].widget.attrs['readonly'] = True
            self.fields['Date_Approved'].widget.attrs['readonly'] = True

    def clean_sku(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.User_Approved
        else:
            return self.cleaned_data['Agency', 'Field_Office', 'Approving_Official', 'Date_Approved']

class profilegrp_manage(s.ModelForm):
    groupid = s.ModelMultipleChoiceField(queryset=Groups.objects.all(), widget=s.CheckboxSelectMultiple, label = "")

    class Meta:
        model = usergroups
        fields = ('groupid',)



class ValidatingSetPasswordForm(s.Form):
    new_password2 = PasswordField()



class ValidatingPassStrength(s.Form):
    MIN_LENGTH = 8
    MAX_LENGTH = 20

    def __init__(self, *args, **kwargs):
        super(ValidatingPassStrength, self).__init__(*args, **kwargs)

    def clean_new_password1(self):
        password1 = self.cleaned_data.get('password')
        test=0
        # At least MIN_LENGTH long
        if len(password1) < self.MIN_LENGTH:
            test=1

        # No Longer than MAX_LENGTH long
        if len(password1) > self.MAX_LENGTH:
            test=1

        first_islower = password1[0].islower()
        if all(c.islower() == first_islower for c in password1):
            test=1

        first_isupper = password1[0].isupper()
        if all(c.isupper() == first_isupper for c in password1):
            test=1

        first_isnumeric = password1[0].isnumeric()
        if all(c.isnumeric() == first_isnumeric for c in password1):
            test=1

        first_isnonascii = password1[0]
        if all(((ord(c) > 32 and ord(c) < 48) or (ord(c) > 57 and ord(c) < 65) or (ord(c) > 90 and ord(c) < 97)) for c in first_isnonascii):
            Test = "Test"
        else:
            test=1

        # ... any other validation you want ...
        if test==1:
            return "Weak"
        else:
            return "Strong"



 
class ValidatingPasswordChangeForm(auth.forms.PasswordChangeForm):
    MIN_LENGTH = 8
    MAX_LENGTH = 20

    def clean_new_password1(self):
        password1 = self.cleaned_data.get('new_password1')

        # At least MIN_LENGTH long
        if len(password1) < self.MIN_LENGTH:
            raise s.ValidationError("The new password must be at least %d characters long." % self.MIN_LENGTH)

        # No Longer than MAX_LENGTH long
        if len(password1) > self.MAX_LENGTH:
            raise s.ValidationError("The new password can be no more than %d characters long." % self.MAX_LENGTH)

        first_islower = password1[0].islower()
        if all(c.islower() == first_islower for c in password1):
            raise s.ValidationError("The new password must contain at least one lower case character.")

        first_isupper = password1[0].isupper()
        if all(c.isupper() == first_isupper for c in password1):
            raise s.ValidationError("The new password must contain at least one upper case character.")

        first_isnumeric = password1[0].isnumeric()
        if all(c.isnumeric() == first_isnumeric for c in password1):
            raise s.ValidationError("The new password must contain at least one number.")

        Test = 0
        for i in range(len(password1)):
            if (ord(password1[i]) > 32 and ord(password1[i]) < 48) or (ord(password1[i]) > 57 and ord(password1[i]) < 65) or (ord(password1[i]) > 90 and ord(password1[i]) < 97):
                Test = 1
        if Test == 0:
            raise s.ValidationError("The new password must contain at least one special character.")

        # ... any other validation you want ...

        return password1

        

    

    
