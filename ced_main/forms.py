from django import forms as s
from django.forms import ModelChoiceField
from form_utils import forms
from form_utils.forms import BetterModelForm, BetterForm
# from django.forms.extras.widgets import SelectDateWidget #python 2.7
from django.forms.widgets import SelectDateWidget
from django.forms.models import inlineformset_factory
from django.forms.models import BaseInlineFormSet
from django.forms.formsets import formset_factory
from django.contrib.auth.models import User
from accounts.models import userprofile, office_values
import django_tables2 as tables
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from ced_main.models import *
from django.db.models import Q
from django.utils import timezone
import datetime
from operator import itemgetter, attrgetter
from itertools import chain

now = datetime.datetime.utcnow()
now = now.replace(tzinfo=timezone.utc)

# Horizontal checkbox renderer
from django.utils.encoding import force_text
from django.utils.html import format_html


class HorizontalRadioSelect(s.RadioSelect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        css_style = 'style="display: inline-block; margin-right: 10px;"'

        self.renderer.inner_html = '<li ' + css_style + '>{choice_value}{sub_widgets}</li>'


class HorizontalCheckboxSelect(s.CheckboxSelectMultiple):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        css_style = 'style="display: inline-block; margin-right: 10px;"'

        self.renderer.inner_html = '<li ' + css_style + '>{choice_value}{sub_widgets}</li>'


class HorizontalCheckboxRendererYears(s.CheckboxSelectMultiple):
    def render(self):
        id_ = self.attrs.get('id', None)
        start_tag = format_html('<div id="{0}">', id_) if id_ else '<div>'
        output = [start_tag]
        for widget in self:
            output.append(format_html(u'<span style="padding-right:13px;">{0}</span>', force_text(widget)))
        output.append('</div>')
        return mark_safe('\n'.join(output))


class HorizontalCheckboxRendererStates(s.CheckboxSelectMultiple):
    def render(self):
        id_ = self.attrs.get('id', None)
        start_tag = format_html('<div id="{0}">', id_) if id_ else '<div>'
        output = [start_tag]
        for widget in self:
            output.append(format_html(u'<span style="padding-right:7px;">{0}</span>', force_text(widget)))
        output.append('</div>')
        return mark_safe('\n'.join(output))


class HorizontalCheckboxRendererCounties(s.CheckboxSelectMultiple):
    def render(self):
        id_ = self.attrs.get('id', None)
        start_tag = format_html('<div" id="{0}">', id_) if id_ else '<div>'
        output = [start_tag]
        for widget in self:
            output.append(format_html(u'<div class="spnwdth"><span>{0}</span></div>', force_text(widget)))
        output.append('</div>')
        return mark_safe('\n'.join(output))


seedchoices = (('Only Native', 'Only Native'), ('Only Non-Native', 'Only Non-Native'),
               ('Native/Non-Native Mixed', 'Native/Non-Native Mixed'))
firechoices = (('Non-Wildfire Effort', 'Non-Wildfire Effort'), ('Post Wildfire Effort', 'Post Wildfire Effort'))

IMPCHOICES = ((2, 'In Progress',), (3, 'Completed',))
LENGTHCHOICES = (
(0, '---Select a Length---',), (1, '0-4 Years',), (2, '5-9 Years',), (3, '10-14 Years',), (4, '15-19 Years',),
(5, '20-24 Years',), (6, '25-29 Years',), (7, '>30 Years',), (8, 'In Perpetuity',))
YEARCHOICES = (
(2009, '2009',), (2010, '2010',), (2011, '2011',), (2012, '2012',), (2013, '2013',), (2014, '2014',), (2015, '2015',),
(2016, '2016',), (2017, '2017',), (2018, '2018',), (2019, '2019',), (2020, '2020',))
StatCHOICES = ((1, 'Draft Record',), (2, 'Awaiting Approval',), (3, 'Approved',), (4, 'Marked for Deletion',))
WavCHOICES = ((1, 'Accept',), (2, 'Decline',))
YesNo = ((1, 'Yes',), (2, 'No',), (0, 'N/A',))
fwsresponses = ((1, 'Yes',), (2, 'No',), (3, 'Any Response',), (4, 'No Response',))
YesNoOnly = ((1, 'Yes',), (2, 'No',))
YesNoUnk = (('Yes', 'Yes',), ('No', 'No',), ('Unknown', 'Unknown',))
YesUnk = ((1, 'Yes',), (2, 'Unknown',), (0, 'N/A',))
powerchoice = (('-------', '-------',), ('Distribution', 'Distribution',), ('Transmission', 'Transmission',))
StatusChoice = (
(1, 'Yes: project is already effective. Describe further in 2a below and upload supporting documents in Step 2.',), (3,
                                                                                                                     'Highly Likely: project is reasonably certain to be effective given adequate time. Describe further in 2a below, upload supporting documents in Step 2, and complete questions below in Part 3.',),
(2,
 'Uncertain or Unlikely: project is uncertain or unlikely to be effective based on current information. Describe further in 2a below, and complete questions below in Part 3.',))
StatusChoice1 = ((1, 'Yes: project is already effective.',),
                 (3, 'Highly Likely: project is reasonably certain to be effective given adequate time.',), (2,
                                                                                                             'Uncertain or Unlikely: project is uncertain or unlikely to be effective based on current information.',))
StatusChoice2 = ((1, 'Effort is already effective',), (4, 'Effort is already effective (Not applicable for 3 years)',), (3, 'Effort has a high likelihood of being effective given adequate time',), (2, 'Effort is uncertain or unlikely to be effective',))

File_Types = (
('---Select/Update File Type---', '---Select/Update File Type---',), ('Project Proposal', 'Project Proposal',),
('Habitat Assessment', 'Habitat Assessment',), ('Management Plan', 'Management Plan',), ('Data', 'Data',),
('Map(s)', 'Map(s)',), ('Photo(s)', 'Photo(s)',), ('Seed Information', 'Seed Information',),
('Monitoring Report', 'Monitoring Report',), ('Peer-Reviewed Science', 'Peer-Reviewed Science'), ('Other', 'Other',))

File_Types1 = (('Project Proposal', 'Project Proposal',), ('Habitat Assessment', 'Habitat Assessment',),
               ('Management Plan', 'Management Plan',), ('Data', 'Data',), ('Map(s)', 'Map(s)',),
               ('Photo(s)', 'Photo(s)',), ('Seed Information', 'Seed Information',),
               ('Monitoring Report', 'Monitoring Report',), ('Peer-Reviewed Science', 'Peer-Reviewed Science'),
               ('Other', 'Other',))

metrictypes = (('----Choose a Metric----', '----Choose a Metric----'), ('Acres', 'Acres'), ('Miles', 'Miles'))

queryypes = ((1, 'Phased Assessment',), (2, 'Refined Query',))

metricequ = (('----Choose an Equation----', '----Choose an Equation----'), ('Greater Than', 'Greater Than or Equal To'),
             ('Less Than', 'Less Than or Equal To'), ('Equal To', 'Equal To'))

datequ = (('1', 'Before or Equal to'), ('2', 'After'), ('3', 'Between'))


All_Imp_Choices = (('1', 'Effort is already effective'), ('2', 'Effort has a high likelihood of being effective given adequate time'), ('3', 'Effort is uncertain or unlikely to be effective'), ('4', 'Effort is already effective'), ('5', 'Effort has a high likelihood of being effective given adequate time'), ('6', 'Effort is uncertain or unlikely to be effective'), ('7', 'Effort is already effective (Not applicable for 3 years)'), ('8', 'Effort has a high likelihood of being effective given adequate time'), ('9', 'Effort is uncertain or unlikely to be effective'), ('10', 'Effort is already effective'), ('11', 'Effort is already effective (Not applicable for 3 years)'), ('12', 'Effort has a high likelihood of being effective given adequate time'), ('13', 'Effort is uncertain or unlikely to be effective'), ('14', 'Effort is already effective (Not applicable for 3 years)'), ('15', 'Effort has a high likelihood of being effective given adequate time'), ('16', 'Effort is uncertain or unlikely to be effective'), ('17', 'Effort is already effective'), ('18', 'Effort is already effective (Not applicable for 3 years)'), ('19', 'Effort has a high likelihood of being effective given adequate time'), ('20', 'Effort is uncertain or unlikely to be effective'), ('21', 'Effort is already effective (Not applicable for 3 years)'), ('22', 'Effort has a high likelihood of being effective given adequate time'), ('23', 'Effort is uncertain or unlikely to be effective'), ('24', 'Effort is already effective (Not applicable for 3 years)'), ('25', 'Effort has a high likelihood of being effective given adequate time'), ('26', 'Effort is uncertain or unlikely to be effective'), ('27', 'Effort is already effective (Not applicable for 3 years)'), ('28', 'Effort has a high likelihood of being effective given adequate time'), ('29', 'Effort is uncertain or unlikely to be effective'), ('30', 'Effort is already effective (Not applicable for 3 years)'), ('31', 'Effort has a high likelihood of being effective given adequate time'), ('32', 'Effort is uncertain or unlikely to be effective'), ('33', 'Effort is already effective'), ('34', 'Effort has a high likelihood of being effective given adequate time'), ('35', 'Effort is uncertain or unlikely to be effective'), ('36', 'Effort is already effective (Not applicable for 3 years)'), ('37', 'Effort has a high likelihood of being effective given adequate time'), ('38', 'Effort is uncertain or unlikely to be effective'), ('39', 'Effort is already effective'), ('40', 'Effort has a high likelihood of being effective given adequate time'), ('41', 'Effort is uncertain or unlikely to be effective'), ('42', 'Effort is already effective'), ('43', 'Effort has a high likelihood of being effective given adequate time'), ('44', 'Effort is uncertain or unlikely to be effective'), ('45', 'Effort is already effective'), ('46', 'Effort has a high likelihood of being effective given adequate time'), ('47', 'Effort is uncertain or unlikely to be effective'), ('48', 'Effort is already effective'), ('49', 'Effort has a high likelihood of being effective given adequate time'), ('50', 'Effort is uncertain or unlikely to be effective'), ('51', 'Effort is already effective'), ('52', 'Effort has a high likelihood of being effective given adequate time'), ('53', 'Effort is uncertain or unlikely to be effective'), ('54', 'Effort is already effective'), ('55', 'Effort has a high likelihood of being effective given adequate time'), ('56', 'Effort is uncertain or unlikely to be effective'), ('57', 'Effort is already effective'), ('58', 'Effort has a high likelihood of being effective given adequate time'), ('59', 'Effort is uncertain or unlikely to be effective'), ('60', 'Effort is already effective'), ('61', 'Effort has a high likelihood of being effective given adequate time'), ('62', 'Effort is uncertain or unlikely to be effective'), ('63', 'Effort is already effective'), ('64', 'Effort has a high likelihood of being effective given adequate time'), ('65', 'Effort is uncertain or unlikely to be effective'), ('66', 'Effort is already effective'), ('67', 'Effort has a high likelihood of being effective given adequate time'), ('68', 'Effort is uncertain or unlikely to be effective'), ('69', 'Effort is already effective'), ('70', 'Effort has a high likelihood of being effective given adequate time'), ('71', 'Effort is uncertain or unlikely to be effective'))

ActivityLabels = (('NON-REGULATORY CONSERVATION PLANS (Strategies, BMPs)',
                   'NON-REGULATORY CONSERVATION PLANS (Strategies, BMPs) (Non-Spatial Plan)')
                  , ('REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders)',
                     'REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders) (Non-Spatial Plan)')
                  , ('RESTORATION: Infrastructure Removal and Modification',
                     'RESTORATION: Infrastructure Removal and Modification (Non-Spatial Project)')
                  , ('RESTORATION: Livestock & Rangeland Management',
                     'RESTORATION: Livestock & Rangeland Management (Non-Spatial Project)')
                  ,
                  ('RESTORATION: Population Augmentation', 'RESTORATION: Population Augmentation (Non-Spatial Project)')
                  , ('RESTORATION: Travel Management', 'RESTORATION: Travel Management (Non-Spatial Project)')
                  , ('RESTORATION: Wild Equid Management', 'RESTORATION: Wild Equid Management (Non-Spatial Project)')
                  , ('RESTORATION: Conifer Removal', 'RESTORATION: Conifer Removal (Spatial Project)')
                  , ('RESTORATION: Post-Disturbance and/or Habitat Enhancement',
                     'RESTORATION: Post-Disturbance and/or Habitat Enhancement (Spatial Project)')
                  , ('SAGEBRUSH PROTECTION', 'SAGEBRUSH PROTECTION (Spatial Project)'))

SubActivityLabels = (('Minimization  and Avoidance Strategies / BMPs',
                      'Minimization  and Avoidance Strategies / BMPs (NON-REGULATORY MECHANISMS: (Plans, Strategies, BMPs))')
                     , ('Non-regulatory Conservation Strategies',
                        'Non-regulatory Conservation Strategies (NON-REGULATORY MECHANISMS: (Plans, Strategies, BMPs))')
                     , ('Compensatory Mitigation Plans',
                        'Compensatory Mitigation Plans (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))')
                     , (
                     'Conservation Agreements (including but not limited to: CCAs, CCAAs, Farm Bill and other Incentive-based programs)',
                     'Conservation Agreements (including but not limited to: CCAs, CCAAs, Farm Bill and other Incentive-based programs) (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))')
                     , ('Conservation Banking / Advanced Crediting Systems',
                        'Conservation Banking / Advanced Crediting Systems (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))')
                     , ('County/Local Government Plan',
                        'County/Local Government Plan (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))')
                     , ('Federal Land Use Plan',
                        'Federal Land Use Plan (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))')
                     , ('Fire Mutual Aid Agreement',
                        'Fire Mutual Aid Agreement (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))')
                     , ('Fire Related Conservation Strategy (Pre-suppression Plans)',
                        'Fire Related Conservation Strategy (Pre-suppression Plans) (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))')
                     , ('Grazing and Rangeland Management Plans (Regulatory)',
                        'Grazing and Rangeland Management Plans (Regulatory) (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))')
                     , ('Programmatic Candidate Conservation Agreement',
                        'Programmatic Candidate Conservation Agreement (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))')
                     , ('Programmatic Candidate Conservation Agreement with Assurances',
                        'Programmatic Candidate Conservation Agreement with Assurances (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))')
                     , ('Reclamation Plan',
                        'Reclamation Plan (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))')
                     , ('State Conservation Plan',
                        'State Conservation Plan (REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders))')
                     , ('Fence Marking', 'Fence Marking (RESTORATION: Infrastructure Removal and Modification)')
                     ,
                     ('Fence Modification', 'Fence Modification (RESTORATION: Infrastructure Removal and Modification)')
                     , ('Fence Removal', 'Fence Removal (RESTORATION: Infrastructure Removal and Modification)')
                     , ('Powerline Burial', 'Powerline Burial (RESTORATION: Infrastructure Removal and Modification)')
                     , ('Powerline Retrofitting / Modification',
                        'Powerline Retrofitting / Modification (RESTORATION: Infrastructure Removal and Modification)')
                     , ('Structure Removal', 'Structure Removal (RESTORATION: Infrastructure Removal and Modification)')
                     , ('Improved Grazing Practices (Rest, Rotation, Etc.)',
                        'Improved Grazing Practices (Rest, Rotation, Etc.) (RESTORATION: Livestock & Rangeland Management)')
                     , ('Translocation', 'Translocation (RESTORATION: Population Augmentation)')
                     , ('Rerouted Roads and/or Trails', 'Rerouted Roads and/or Trails (RESTORATION: Travel Management)')
                     , ('Road and Trail closure', 'Road and Trail closure (RESTORATION: Travel Management)')
                     , ('Wild Equid Gather', 'Wild Equid Gather (RESTORATION: Wild Equid Management)')
                     , ('Wild Equid Population Control',
                        'Wild Equid Population Control (RESTORATION: Wild Equid Management)')
                     , ('Conifer Removal (All Phases)', 'Conifer Removal (All Phases) (RESTORATION: Conifer Removal)')
                     , ('Annual Grass, Forb, or Noxious Weed Treatments',
                        'Annual Grass, Forb, or Noxious Weed Treatments (RESTORATION: Post-Disturbance and/or Habitat Enhancement)')
                     , ('Area Closure (Area and/or Seasonal)',
                        'Area Closure (Area and/or Seasonal) (RESTORATION: Post-Disturbance and/or Habitat Enhancement)')
                     , ('Energy development reclamation with the goal of sagebrush restoration',
                        'Energy development reclamation with the goal of sagebrush restoration (RESTORATION: Post-Disturbance and/or Habitat Enhancement)')
                     ,
                     ('Fuels Management', 'Fuels Management (RESTORATION: Post-Disturbance and/or Habitat Enhancement)')
                     , ('Vegetation Management / Habitat Enhancement',
                        'Vegetation Management / Habitat Enhancement (RESTORATION: Post-Disturbance and/or Habitat Enhancement)')
                     , ('Conservation Easement', 'Conservation Easement (SAGEBRUSH PROTECTION)'),
                     ('Fuel Breaks', 'Fuel Breaks (SAGEBRUSH PROTECTION)')
                     , ('Land Acquisition', 'Land Acquisition (SAGEBRUSH PROTECTION)')
                     )

officesget1 = office_values.objects.values_list('office', flat=True).all().order_by('state', 'office')
offices1 = []
for off in officesget1:
    state1 = office_values.objects.values_list('state', flat=True).get(office=off)
    agency1 = office_values.objects.values_list('agency', flat=True).get(office=off)
    if str(off) == '---Select an Agency---' or str(off) == '---Select an Office---':
        name = str(off)
    else:
        name = str(off) + ", " + str(state1) + ", " + str(agency1)
    offices1.append([str(off), str(name)])
offices1 = sorted(offices1)

offices2 = []
for off1 in officesget1:
    state2 = office_values.objects.values_list('state', flat=True).get(office=off1)
    agency2 = office_values.objects.values_list('agency', flat=True).get(office=off1)
    if str(off1) != '---Select an Agency---' and str(off1) != '---Select an Office---':
        name1 = str(off1) + ", " + str(state2) + ", " + str(agency2)
        offices2.append([str(off1), str(name1)])
offices2 = sorted(offices2)


def allusers():
    editusersget = User.objects.all()
    editusers = []
    for edi in editusersget:
        firstname = User.objects.values_list('first_name', flat=True).get(username=edi)
        lastname = User.objects.values_list('last_name', flat=True).get(username=edi)
        email = User.objects.values_list('email', flat=True).get(username=edi)
        useragency = userprofile.objects.values_list('Agency', flat=True).get(User=edi)
        useroffice = userprofile.objects.values_list('Field_Office', flat=True).get(User=edi)
        name1 = str(lastname) + ", " + str(firstname) + " (Email: " + str(email) + "), " + str(useragency) + ", " + str(
            useroffice)
        usid = userprofile.objects.get(User=edi)
        if lastname != "":
            editusers.append([str(usid), str(name1)])
    editusers = sorted(editusers, key=itemgetter(1))
    return editusers


def groupusers():
    groupuserlist = []
    groupuserlist.append(["AllUsers", "Email All Users"])
    groupuserlist.append(["Admin", "Email All Administrators"])
    groupuserlist.append(["Approve", "Email All Approving Officials"])
    groupuserlist.append(["ApprovedUsers", "Email All Approved Users"])
    groupuserlist.append(["DemoUsers", "Email All Deomonstration Only Users"])
    groupuserlist.append(["IncompleteUsers", "Email All Users Who Haven't Completed their Profile"])

    return groupuserlist


def officeusers():
    officeusersget = User.objects.all()
    officeusers = []
    for off in officeusersget:
        office = userprofile.objects.values_list('Field_Office', flat=True).get(User_id=User.objects.get(username=off))
        officecheck = 0
        if office == '' or office == '---Select an Agency---' or office == '---Select an Office---' or office == 'DEMONSTRATION USER ACCESS ONLY':
            test = 'Test'
        else:
            for off1 in officeusers:
                if off1[0] == office:
                    officecheck = 1
            if officecheck == 0:
                officeusers.append([str(office), str(office)])
    officeusers = sorted(officeusers)
    return officeusers


def agencyusers():
    agencyusersget = User.objects.all()
    agencyusers = []
    for agn in agencyusersget:
        User_id = User.objects.values_list('id', flat=True).get(username=agn)
        agency = userprofile.objects.values_list('Agency', flat=True).get(
            User_id=User.objects.values_list('id', flat=True).get(username=agn))
        agencycheck = 0
        if agency == '' or agency == '---Select an Agency---':
            test = 'Test'
        else:
            for agn1 in agencyusers:
                if agn1[0] == agency:
                    agencycheck = 1
            if agencycheck == 0:
                agencyusers.append([str(agency), str(agency)])
    agencyusers = sorted(agencyusers)
    return agencyusers


def metchoices(subact):
    chce = []
    cnt = 0
    if subact == "None":
        chce = [("No Data", "--------")]
    else:
        try:
            chceget = activity_plan_values.objects.filter(SubActivity=subact)
            chce.append(["No Data", "--------"])
            for ch in chceget:
                chce.append([str(ch), str(ch)])
                cnt = cnt + 1
            if cnt == 1:
                chce = []
                for ch in chceget:
                    chce.append([str(ch), str(ch)])
        except:
            chce = [("No Data", "--------")]
    return chce


def doc_url(self, obj):
    return '<a href="https://www.sciencebase.gov/catalog/file/get/%s">%s</a>' % (obj.LCMItem, obj.Document_Name)
    doc_url.allow_tags = True


class newprj_Form(s.ModelForm):
    Project_Name = s.CharField(max_length=75, widget=s.TextInput(attrs={'size': '80'}), label="CED Effort Name")
    Entry_Type = s.IntegerField(widget=s.HiddenInput(), initial=None, required=False)
    Shapefile = s.FileField(widget=s.HiddenInput(), required=False)
    Metadata = s.FileField(widget=s.HiddenInput(), required=False)
    Location_Info = s.CharField(widget=s.HiddenInput(), max_length=255, required=False)
    Location_Desc = s.CharField(widget=s.HiddenInput(), max_length=255, required=False)
    Agreement_Length = s.IntegerField(widget=s.HiddenInput(), required=False)
    Agreement_Penalty = s.IntegerField(widget=s.HiddenInput(), required=False)

    TypeAct = s.CharField(widget=s.HiddenInput(), required=False)
    Activity = s.ModelChoiceField(queryset=activity.objects.all().order_by('Activity'), required=False, label="Activity")
    SubActivity = s.ModelChoiceField(queryset=subactivity.objects.all().order_by('SubActivity'), required=False, label="Subactivity")

    Objectives_Desc = s.CharField(widget=s.HiddenInput(), required=False)
    Effects_Desc = s.CharField(widget=s.HiddenInput(), required=False)
    Notes = s.CharField(widget=s.HiddenInput(), required=False)
    Implementing_Party = s.CharField(max_length=100, widget=s.TextInput(attrs={'size': '60'}),
                                     label="Implementing Party")
    Office = s.CharField(max_length=100, widget=s.TextInput(attrs={'size': '60'}))
    Created_By = s.CharField(widget=s.HiddenInput(), required=False)
    Date_Created = s.DateTimeField(initial=datetime.datetime.now(), label="Date Created")
    User_Phone_Number = s.CharField(widget=s.HiddenInput(), required=False)
    User_Email = s.CharField(widget=s.HiddenInput(), required=False)
    Project_Status = s.TypedChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=IMPCHOICES,
                                        label="Effort Status")

    Last_Updated = s.DateTimeField(widget=s.HiddenInput(), required=False)
    Updating_User = s.CharField(widget=s.HiddenInput(), required=False)
    Approved = s.IntegerField(widget=s.HiddenInput(), initial=0, required=False)

    Date_Approved = s.DateTimeField(widget=s.HiddenInput(), required=False)
    PageLoc = s.CharField(widget=s.HiddenInput(), max_length=15, required=False)
    LCMItem = s.CharField(widget=s.HiddenInput(), max_length=50, required=False)
    LC_Zoom = s.IntegerField(widget=s.HiddenInput(), required=False)
    LC_Center_X = s.FloatField(widget=s.HiddenInput(), required=False)
    LC_Center_Y = s.FloatField(widget=s.HiddenInput(), required=False)

    Mark_For_Deletion = s.BooleanField(widget=s.HiddenInput(), required=False)
    Wobble_GIS = s.BooleanField(widget=s.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = project_info
        fields = (
        'Project_Name', 'Project_Status', 'Activity', 'SubActivity', 'Implementing_Party', 'Office', 'Created_By',
        'Date_Created', 'PageLoc', 'LCMItem', 'Date_Approved',)

    def __init__(self, *args, **kwargs):
        super(newprj_Form, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance:
            self.fields['Date_Created'].widget.attrs['readonly'] = True
            self.fields['Implementing_Party'].widget.attrs['readonly'] = True
            self.fields['Office'].widget.attrs['readonly'] = True

    def clean_sku(self):
        instance = getattr(self, 'instance', None)

        if instance:
            return instance.Date_Created
        else:
            return self.cleaned_data['Date_Created']

class editprj_Form(BetterModelForm):
    Project_Name = s.CharField(widget=s.TextInput(attrs={'size': '73'}), max_length=75, label="Effort Name*")
    Entry_Type = s.ChoiceField(widget=s.RadioSelect(), choices=StatCHOICES, required=False, label="Entry Type")
    Shapefile = s.CharField(widget=s.HiddenInput(), max_length=255, label="Shapefile", required=False)
    Metadata = s.CharField(widget=s.HiddenInput(), max_length=255, label="Metadata", required=False)
    Location_Info = s.CharField(widget=s.HiddenInput(), max_length=255, label="Location Information", required=False)
    Location_Desc = s.CharField(widget=s.HiddenInput(), max_length=255, label="Location Description", required=False)

    TypeAct = s.CharField(widget=s.TextInput(attrs={'size': '10'}), max_length=10, label="Effort Type", required=False)
    Activity = s.CharField(widget=s.TextInput(attrs={'size': '100'}), max_length=100, required=False, label="Activity")
    SubActivity = s.CharField(widget=s.TextInput(attrs={'size': '100'}), max_length=100, required=False,
                              label="Subactivity")
    seeding_type = s.TypedChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=seedchoices,
                                      required=False, label="Seeding Type")
    post_fire = s.TypedChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=firechoices,
                                   required=False, label="Post Wildfire Related")
    mitigation = s.TypedChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=YesNoUnk,
                                   required=False, label="Mitigation Treatment")
    Agreement_Length = s.ChoiceField(choices=LENGTHCHOICES, required=False, label="Agreement Length")
    Agreement_Penalty = s.TypedChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=YesNoOnly,
                                           required=False, label="Agreement Penalty")

    dtrng = []
    for i in range(0, 100):
        dtrng.append(2020 - i)

    dtrngend = []
    for i in range(0, 100):
        dtrngend.append(2100 - i)
    Start_Date = s.DateField(required=False, widget=SelectDateWidget(years=dtrng), label="Start Date*")
    End_Date = s.DateField(required=False, widget=SelectDateWidget(years=dtrngend), label="End Date*")

    Metric = s.ModelChoiceField(queryset=metric.objects.all(), required=False, label="Metric Type*")
    Metric_Value = s.FloatField(required=False, widget=s.TextInput(attrs={'size': '9'}), label="Metric Value*")
    GIS_Acres = s.FloatField(required=False, widget=s.TextInput(attrs={'size': '9'}), label="GIS Acres*")

    Objectives_Desc = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 100}), initial="", label='Objectives*',
                                  required=False)
    Effects_Desc = s.CharField(widget=s.HiddenInput(), initial="", label='Effects*', required=False)
    Notes = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 100}), initial="", label='Notes', required=False)
    Implementing_Party = s.CharField(max_length=50, label="Implementing Party", required=False)

    Office = s.CharField(max_length=100, label="Office", required=False)
    Created_By = s.CharField(max_length=50, label="Created By", required=False)
    Date_Created = s.DateTimeField(label="Date Created", required=False)
    User_Phone_Number = s.CharField(widget=s.HiddenInput(), max_length=12, required=False)
    User_Email = s.CharField(max_length=50, label="User Email", required=False)
    Project_Status = s.IntegerField(widget=s.HiddenInput(), required=False)
    Last_Updated = s.DateTimeField(initial=now, label="Last Updated", required=False)
    Updating_User = s.CharField(max_length=50, label="Updating User", required=False)
    Approved = s.IntegerField(widget=s.HiddenInput(), initial=0, required=False)
    Approving_Official = s.CharField(max_length=50, label="Approving Official", required=False)
    Date_Approved = s.DateTimeField(required=False, label="Date Approved")
    PageLoc = s.CharField(widget=s.HiddenInput(), max_length=15, required=False)
    LCMItem = s.CharField(widget=s.HiddenInput(), max_length=50, required=False)

    Mark_For_Deletion = s.BooleanField(label="Mark This Effort for Deletion", required=False)
    Wobble_GIS = s.BooleanField(widget=s.HiddenInput(), required=False)

    # Ag_Conversion_Explain = s.CharField(widget=s.Textarea(attrs={'rows': 3, 'cols': 100}), initial="",
    #                                     label='Ag Conversion Effectiveness*', required=False)
    # Conifer_Encroach_Explain = s.CharField(widget=s.Textarea(attrs={'rows': 3, 'cols': 100}), initial="",
    #                                        label='Conifers Effectiveness*', required=False)
    # Oil_Gas_Explain = s.CharField(widget=s.Textarea(attrs={'rows': 3, 'cols': 100}), initial="",
    #                               label='Oil and Gas Effectiveness*', required=False)
    # Feral_Equids_Explain = s.CharField(widget=s.Textarea(attrs={'rows': 3, 'cols': 100}), initial="",
    #                                    label='Feral Equids Effectiveness*', required=False)
    # Infrastructure_Explain = s.CharField(widget=s.Textarea(attrs={'rows': 3, 'cols': 100}), initial="",
    #                                      label='Infrastructure Effectiveness*', required=False)
    # Mining_Explain = s.CharField(widget=s.Textarea(attrs={'rows': 3, 'cols': 100}), initial="",
    #                              label='Mining Effectiveness*', required=False)
    # Recreation_Explain = s.CharField(widget=s.Textarea(attrs={'rows': 3, 'cols': 100}), initial="",
    #                                  label='Recreation Effectiveness*', required=False)
    # Urban_Devel_Explain = s.CharField(widget=s.Textarea(attrs={'rows': 3, 'cols': 100}), initial="",
    #                                   label='Urban Development Effectiveness*', required=False)
    # Fire_Explain = s.CharField(widget=s.Textarea(attrs={'rows': 3, 'cols': 100}), initial="",
    #                            label='Fire Effectiveness*', required=False)
    # Improper_Grazing_Explain = s.CharField(widget=s.Textarea(attrs={'rows': 3, 'cols': 100}), initial="",
    #                                        label='Improper Grazing Effectiveness*', required=False)
    # Isolated_Explain = s.CharField(widget=s.Textarea(attrs={'rows': 3, 'cols': 100}), initial="",
    #                                label='Isolated Populations Effectiveness*', required=False)
    # Invasives_Explained = s.CharField(widget=s.Textarea(attrs={'rows': 3, 'cols': 100}), initial="",
    #                                   label='Invasives Effectiveness*', required=False)
    # Sagebrush_Loss_Explain = s.CharField(widget=s.Textarea(attrs={'rows': 3, 'cols': 100}), initial="",
    #                                      label='Sagebrush Loss Effectiveness*', required=False)

    CCAA_Num_Permit_Holders = s.IntegerField(widget=s.TextInput(attrs={'size': '3'}), label="# Permit Holders*",
                                             initial=0, required=False)
    Type_of_Powerline = s.ChoiceField(choices=powerchoice, label='Type of Powerline*', required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = project_info

        fieldsets = (('Step 4: Activity Information', {'fields': (
        'Project_Name', 'TypeAct', 'Entry_Type', 'Activity', 'SubActivity', 'Agreement_Length', 'Agreement_Penalty',
        'Type_of_Powerline', 'seeding_type', 'post_fire', 'mitigation', 'CCAA_Num_Permit_Holders', 'Start_Date', 'End_Date', 'Metric',
        'Metric_Value', 'GIS_Acres', 'Project_Status', 'Objectives_Desc', 'Notes','Location_Info',
        'Location_Desc', 'Mark_For_Deletion', 'Created_By', 'User_Email', 'Date_Created', 'Implementing_Party',
        'Office', 'Updating_User', 'Last_Updated', 'Approving_Official', 'Date_Approved', 'PageLoc', 'LCMItem'), }),
                     ('Step 2: Location Information', {'fields': ('Location_Info', 'Location_Desc'), }),
                     )

        row_attrs = {'Project_Name': {'class': 'style_names'}}

    def __init__(self, *args, **kwargs):
        super(editprj_Form, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['TypeAct'].widget.attrs['readonly'] = True
            self.fields['Activity'].widget.attrs['readonly'] = True
            self.fields['SubActivity'].widget.attrs['readonly'] = True
            self.fields['SubActivity'].widget.attrs['readonly'] = True
            self.fields['Metric'].widget.attrs['readonly'] = True
            self.fields['GIS_Acres'].widget.attrs['readonly'] = True
            self.fields['Implementing_Party'].widget.attrs['readonly'] = True
            self.fields['Office'].widget.attrs['readonly'] = True
            self.fields['Created_By'].widget.attrs['readonly'] = True
            self.fields['Date_Created'].widget.attrs['readonly'] = True
            self.fields['User_Email'].widget.attrs['readonly'] = True
            # self.fields['Entry_Type'].widget.attrs['readonly'] = True
            self.fields['Last_Updated'].widget.attrs['readonly'] = True
            self.fields['Updating_User'].widget.attrs['readonly'] = True
            self.fields['Approving_Official'].widget.attrs['readonly'] = True
            self.fields['Date_Approved'].widget.attrs['readonly'] = True
            self.fields['Shapefile'].widget.attrs['readonly'] = True
            self.fields['Metadata'].widget.attrs['readonly'] = True

    def clean_sku(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.Implementing_Party
        else:
            return self.cleaned_data['Implementing_Party']

class metrics_Form(s.ModelForm):
    Project_ID = s.CharField(widget=s.HiddenInput(), required=False)
    TotalAcres = s.FloatField(widget=s.TextInput(attrs={'size': '5'}), label="Total Acres", required=False)
    TotalMiles = s.FloatField(widget=s.TextInput(attrs={'size': '5'}), label="Total Miles", required=False)
    TotalNumberBirds = s.FloatField(widget=s.TextInput(attrs={'size': '5'}), label="Total Birds", required=False)
    TotalNumberRemoved = s.FloatField(widget=s.TextInput(attrs={'size': '5'}), label="Total Number Removed",
                                      required=False)
    TotalNumberKilled = s.FloatField(widget=s.TextInput(attrs={'size': '5'}), label="Total Number Killed",
                                     required=False)
    TotalEquids = s.FloatField(widget=s.TextInput(attrs={'size': '5'}), label="Total Number Equids", required=False)
    Target_Species = s.CharField(widget=s.TextInput(attrs={'size': '50'}), max_length=75, required=False)
    Date_Entered = s.DateTimeField(widget=s.HiddenInput(), required=False)
    User = s.CharField(max_length=50, widget=s.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = metrics
        fields = (
        'TotalAcres', 'TotalMiles', 'TotalNumberBirds', 'TotalNumberBirds', 'TotalNumberKilled', 'TotalEquids',
        'Target_Species')


class agreement_protect_Form(s.ModelForm):
    Project_ID = s.CharField(widget=s.HiddenInput(), required=False)
    Sage_Elim = s.FloatField(widget=s.TextInput(attrs={'size': '3'}), label="Sagebrush Elimination", required=False)
    Ag_Conv = s.FloatField(widget=s.TextInput(attrs={'size': '3'}), label="Agricultural Conversion", required=False)
    Improper_Graze = s.FloatField(widget=s.TextInput(attrs={'size': '3'}), label="Improper Grazing", required=False)
    Infastructure = s.FloatField(widget=s.TextInput(attrs={'size': '3'}), label="Infastructure", required=False)
    Energy_Development = s.FloatField(widget=s.TextInput(attrs={'size': '3'}), label="Energy Development",
                                      required=False)
    Mining = s.FloatField(widget=s.TextInput(attrs={'size': '3'}), label="Mining", required=False)
    Recreation = s.FloatField(widget=s.TextInput(attrs={'size': '3'}), label="Recreation", required=False)
    Urbanization_SubDevel = s.FloatField(widget=s.TextInput(attrs={'size': '3'}),
                                         label="Urbanization/Subdivision Development", required=False)
    Date_Entered = s.DateTimeField(widget=s.HiddenInput(), required=False)
    User = s.CharField(max_length=50, widget=s.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = agreement_protect
        fields = (
        'Ag_Conv', 'Energy_Development', 'Improper_Graze', 'Infastructure', 'Mining', 'Recreation', 'Sage_Elim',
        'Urbanization_SubDevel',)


class threats_Form(s.ModelForm):
    Project_ID = s.CharField(widget=s.HiddenInput(), required=False)
    threat = s.ModelMultipleChoiceField(queryset=threat_values.objects.all(), widget=s.CheckboxSelectMultiple,
                                        required=False)
    Date_Entered = s.DateTimeField(widget=s.HiddenInput(), initial=now, required=False)
    User = s.CharField(max_length=50, widget=s.HiddenInput(), required=False)

    class Meta:
        model = threats
        fields = ('threat',)

    def __init__(self, *args, **kwargs):
        super(threats_Form, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['threat'].widget.attrs['readonly'] = True

    def clean_sku(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.threat
        else:
            return self.cleaned_data['threat']


class collab_party_Form(s.ModelForm):
    Project_ID = s.CharField(widget=s.HiddenInput(), required=False)
    collab_party = s.ModelMultipleChoiceField(queryset=imp_party_values.objects.all().order_by('Implementation_Party'),
                                              widget=s.CheckboxSelectMultiple, required=False)
    Date_Entered = s.DateTimeField(widget=s.HiddenInput(), initial=now, required=False)
    User = s.CharField(max_length=50, widget=s.HiddenInput(), required=False)

    class Meta:
        model = collab_party
        fields = ('collab_party',)


class MultiFileInput(s.FileInput):
    def render(self, name, value, attrs={}):
        attrs['multiple'] = 'multiple'
        return super(MultiFileInput, self).render(name, None, attrs=attrs)

    def value_from_datadict(self, data, files, name):
        if hasattr(files, 'getlist'):
            return files.getlist(name)
        else:
            return [files.get(name)]


class MultiFileField(s.FileField):
    widget = MultiFileInput
    default_error_messages = {
        'min_num': u"Ensure at least %(min_num)s files are uploaded (received %(num_files)s).",
        'max_num': u"Ensure at most %(max_num)s files are uploaded (received %(num_files)s).",
        'file_size': u"File: %(uploaded_file_name)s, exceeded maximum upload size."
    }

    def __init__(self, *args, **kwargs):
        self.min_num = kwargs.pop('min_num', 0)
        self.max_num = kwargs.pop('max_num', None)
        self.maximum_file_size = kwargs.pop('maximum_file_size', None)
        super(MultiFileField, self).__init__(*args, **kwargs)

    def to_python(self, data):
        ret = []
        for item in data:
            ret.append(super(MultiFileField, self).to_python(item))
        return ret

    def validate(self, data):
        super(MultiFileField, self).validate(data)
        num_files = len(data)
        if len(data) and not data[0]:
            num_files = 0
        if num_files < self.min_num:
            raise ValidationError(self.error_messages['min_num'] % {'min_num': self.min_num, 'num_files': num_files})
        elif self.max_num and num_files > self.max_num:
            raise ValidationError(self.error_messages['max_num'] % {'max_num': self.max_num, 'num_files': num_files})
        for uploaded_file in data:
            if uploaded_file.size > self.maximum_file_size:
                raise ValidationError(self.error_messages['file_size'] % {'uploaded_file_name': uploaded_file.name})


class implementation_info_Form(BetterModelForm):
    Project_ID = s.IntegerField(required=False)
    Imp_Status = s.TypedChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=IMPCHOICES,
                                    required=False,
                                    label="1) What is the current implementation status of the activity?*", initial=0)

    Start_Date = s.DateTimeField(widget=s.HiddenInput(), required=False)
    Finish_Date = s.DateTimeField(widget=s.HiddenInput(), required=False)
    In_Perpetuity = s.BooleanField(widget=s.HiddenInput(), label="No Finish Date, In Perpetuity", required=False)
    # Effective_Determined = s.TypedChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}),
    #                                           choices=StatusChoice2, required=False,
    #                                           label="2) Has the activity been deemed effective?*", initial=0)
    Methods_Explained = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 100}), required=False, label="Methods Explained*")

    Effective_Determined = s.TypedChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=All_Imp_Choices, required=False, label="2) Has the activity been deemed effective?*", initial=0)
    Effective_Explained = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 100}), required=False,
                                      label="2a) Explain why the activity was deemed effective, is highly likely, uncertain, or unlikely to be effective*")

    Reas_Certain = s.TypedChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=YesNoOnly,
                                      required=False, label="a. The activity will be implemented:", initial=0)
    Legal_Authority = s.TypedChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=YesNoOnly,
                                         required=False,
                                         label="b. The implementing party has the legal authority to conduct the activity:",
                                         initial=0)
    Staff_Available = s.TypedChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=YesNoOnly,
                                         required=False,
                                         label="c. Financial, staffing, and administrative resources necessary to carry out the conservation effort are available:",
                                         initial=0)
    Regulatory_Mech = s.TypedChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=YesNoOnly,
                                         required=False,
                                         label="d. Regulatory and/or procedural mechanisms are in place to carry out the efforts:",
                                         initial=0)
    Compliance = s.TypedChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=YesNoOnly,
                                    required=False,
                                    label="e. All Federal/State/Local legal project compliance requirements have been met or are reasonably certain to be met:",
                                    initial=0)
    Vol_Incentives = s.TypedChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=YesNo,
                                        required=False,
                                        label="f. If voluntary participation is needed, are incentives adequate to ensure the level of participation necessary to carry out the conservation effort:",
                                        initial=0)

    Reduce_Threats = s.TypedChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=YesNoOnly,
                                        required=False,
                                        label="a. Describe how the conservation effort reduces the threats:", initial=0)
    Incremental_Objectives = s.TypedChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}),
                                                choices=YesNoOnly, required=False,
                                                label="b. Provide incremental objectives and dates for achieving them:",
                                                initial=0)
    Quantifiable_Measures = s.TypedChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}),
                                               choices=YesNoOnly, required=False,
                                               label="c. Provide quantifiable performance measures to monitor both implementation and effectiveness:",
                                               initial=0)
    AD_Strategy = s.TypedChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=YesNoOnly,
                                     required=False,
                                     label="d.  Incorporate principles of adaptive management (e.g. a corrective management strategy):",
                                     initial=0)

    Imp_and_Effect_Correct = s.TypedChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=YesNo,
                                                required=False,
                                                label="USFWS Only: Was the activity implementation and activity form correct?",
                                                initial=0)
    Imp_and_Effect_Cor_Explan = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 100}), required=False,
                                            label="USFWS Only: Explain your reasoning")

    Date_Entered = s.DateTimeField(required=False)
    User = s.CharField(max_length=50, required=False)

    # An inline class to provide additional information on the form.

    class Meta:
        # Provide an association between the ModelForm and a model
        model = implementation_info
        fieldsets = (
        ('Part 3: Methods', {'fields': ('Methods_Explained',), }),

        ('Step 3: Implementation', {'fields': ('Imp_Status', 'Reas_Certain', 'Legal_Authority', 'Staff_Available', 'Regulatory_Mech', 'Compliance', 'Vol_Incentives'), }),

        
        ('Part 3: Effectiveness Information', {'fields': ('Effective_Determined', 'Effective_Explained', 'Reduce_Threats', 'Incremental_Objectives',            'Quantifiable_Measures', 'AD_Strategy'), }),('USFWS Approval', {'fields': ('Imp_and_Effect_Correct', 'Imp_and_Effect_Cor_Explan'), }),
        )


class subactivity_objectives_Form(s.ModelForm):
    Project_ID = s.CharField(widget=s.HiddenInput(), required=False)
    objective = s.ModelMultipleChoiceField(queryset=subactivity_objectives_data.objects.all(), widget=s.CheckboxSelectMultiple, required=False)
    Date_Entered = s.DateTimeField(widget=s.HiddenInput(), initial=now, required=False)
    User = s.CharField(max_length=50, widget=s.HiddenInput(), required=False)

    class Meta:
        model = subactivity_objectives
        fields = ('objective',)

class subactivity_methods_Form(s.ModelForm):
    Project_ID = s.CharField(widget=s.HiddenInput(), required=False)
    method = s.ModelMultipleChoiceField(queryset=subactivity_methods_data.objects.all(), widget=s.CheckboxSelectMultiple, required=False)
    Date_Entered = s.DateTimeField(widget=s.HiddenInput(), initial=now, required=False)
    User = s.CharField(max_length=50, widget=s.HiddenInput(), required=False)

    class Meta:
        model = subactivity_methods
        fields = ('method',)

class subactivity_effective_state_Form(s.ModelForm):
    Project_ID = s.CharField(widget=s.HiddenInput(), required=False)
    effectiveness_statement = s.ModelMultipleChoiceField(queryset=subactivity_effective_state_data.objects.all(), widget=s.CheckboxSelectMultiple, required=False)
    Date_Entered = s.DateTimeField(widget=s.HiddenInput(), initial=now, required=False)
    User = s.CharField(max_length=50, widget=s.HiddenInput(), required=False)

    class Meta:
        model = subactivity_effective_state
        fields = ('effectiveness_statement',)

### Location information forms ###

class state_Form(s.ModelForm):
    Project_ID = s.CharField(widget=s.HiddenInput(), required=False)
    state_value = s.ModelMultipleChoiceField(queryset=state.objects.all(), widget=s.CheckboxSelectMultiple,
                                             required=False, label="Select States")
    Date_Entered = s.DateTimeField(widget=s.HiddenInput(), required=False)
    User = s.CharField(max_length=50, widget=s.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = state_info
        fields = ('state_value',)


class county_Form(s.ModelForm):
    Project_ID = s.CharField(widget=s.HiddenInput(), required=False)
    county_value = s.ModelMultipleChoiceField(queryset=state_county.objects.all(), widget=s.CheckboxSelectMultiple,
                                              required=False, label="")
    Date_Entered = s.DateTimeField(widget=s.HiddenInput(), required=False)
    User = s.CharField(max_length=50, widget=s.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = county_info
        fields = ('county_value',)


class huc_Form(s.ModelForm):
    Project_ID = s.CharField(widget=s.HiddenInput(), required=False)
    huc12_value = s.ModelMultipleChoiceField(queryset=huc12.objects.none(), widget=s.CheckboxSelectMultiple,
                                             required=False, label="")
    Date_Entered = s.DateTimeField(widget=s.HiddenInput(), required=False)
    User = s.CharField(max_length=50, widget=s.HiddenInput(), required=False)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = huc12_info
        fields = ('huc12_value',)

    def __init__(self, *args, **kwargs):
        super(huc_Form, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        try:
            prjid = str(instance)
            prjid = int(prjid)
            County1 = state_county.objects.values_list('Cnty_St', flat=True).filter(
                id__in=county_info.objects.values_list('county_value', flat=True).filter(Project_ID=prjid))
            StCnty = "Cnty_St='"
            cnt = 0
            for Cn in County1:
                if cnt == 0:
                    counties = StCnty + Cn + "'"
                    cnt = 1
                else:
                    counties = counties + " OR " + StCnty + Cn + "'"

            self.fields['huc12_value'].queryset = state_county_huc12_values.objects.extra(where=[counties])
        except:
            try:
                prjid = str(instance)
                prjid = int(prjid)
                State1 = state.objects.values_list('State', flat=True).filter(
                    id__in=state_info.objects.values_list('state_value', flat=True).filter(Project_ID=prjid))
                StStrt = "State='"
                cnt = 0
                for St in State1:
                    if cnt == 0:
                        states = StStrt + St + "'"
                        cnt = 1
                    else:
                        states = states + " OR " + StStrt + St + "'"

                self.fields['huc12_value'].queryset = state_county_huc12_values.objects.extra(where=[states])
            except:
                Nothing = "None"


class wafwa_Form(s.ModelForm):
    Project_ID = s.CharField(widget=s.HiddenInput(), required=False)
    wafwa_value = s.ModelMultipleChoiceField(queryset=wafwa_zone_values.objects.all(), widget=s.CheckboxSelectMultiple,
                                             required=False, label="")
    Date_Entered = s.DateTimeField(widget=s.HiddenInput(), required=False)
    User = s.CharField(max_length=50, widget=s.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = wafwa_info
        fields = ('wafwa_value',)


class population_Form(s.ModelForm):
    Project_ID = s.CharField(widget=s.HiddenInput(), required=False)
    population_value = s.ModelMultipleChoiceField(queryset=population_values.objects.all().order_by('Populations'),
                                                  widget=s.CheckboxSelectMultiple, required=False, label="")
    Date_Entered = s.DateTimeField(widget=s.HiddenInput(), required=False)
    User = s.CharField(max_length=50, widget=s.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = population_info
        fields = ('population_value',)


class ownership_Form(s.ModelForm):
    Project_ID = s.CharField(widget=s.HiddenInput(), required=False)
    owner_value = s.ModelMultipleChoiceField(queryset=ownership_values.objects.all().order_by('Owners'),
                                             widget=s.CheckboxSelectMultiple, required=False, label="")
    Date_Entered = s.DateTimeField(widget=s.HiddenInput(), required=False)
    User = s.CharField(max_length=50, widget=s.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = ownership_info
        fields = ('owner_value',)


class documentation_Form(s.ModelForm):
    Project_ID = s.CharField(widget=s.HiddenInput(), required=False)
    Date_Entered = s.DateTimeField(widget=s.HiddenInput(), initial=now, required=False)
    User = s.CharField(max_length=50, widget=s.HiddenInput(), required=False)
    File_Type = s.ChoiceField(choices=File_Types, required=False, label="")
    Document_Description = s.CharField(widget=s.TextInput(attrs={'size': '27'}), max_length=255, required=False,
                                       label="", initial="")
    Document_Name = s.CharField(widget=s.TextInput(attrs={'size': '27'}), max_length=255, required=False,
                                label="Document_Name", initial="")
    LCMItem = s.CharField(widget=s.HiddenInput(), max_length=50, required=False)
    LCJason = s.CharField(widget=s.HiddenInput(), max_length=255, required=False, label="Json")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = documentation
        fields = ('File_Type', 'Document_Description', 'Document_Name', 'LCMItem', 'LCJason')

    def __init__(self, *args, **kwargs):
        super(documentation_Form, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)


class documentation_display_Form(s.ModelForm):
    Project_ID = s.IntegerField(required=False)
    Project_Name = s.CharField(max_length=75, required=False)
    User = s.CharField(max_length=50, required=False)
    File_Type = s.CharField(max_length=50, required=False)
    Document_Description = s.CharField(max_length=50, required=False)
    Document_Name = s.CharField(max_length=75, required=False)
    LCMItem = s.CharField(widget=s.HiddenInput(), max_length=50, required=False)
    LCJason = s.CharField(widget=s.HiddenInput(), max_length=255, required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = documentation
        fields = ('Project_ID', 'Project_Name', 'File_Type', 'User', 'Document_Description', 'Document_Name', 'LCMItem',
                  'LCJason')

    def __init__(self, *args, **kwargs):
        super(documentation_display_Form, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance:
            self.fields['Project_ID'].widget.attrs['readonly'] = True
            docid = str(instance)
            docprjname = project_info.objects.values_list('Project_Name', flat=True).get(Project_ID=docid)
            self.fields['Project_Name'].initial = docprjname
            self.fields['Project_Name'].widget.attrs['readonly'] = True
            self.fields['User'].widget.attrs['readonly'] = True
            self.fields['File_Type'].widget.attrs['readonly'] = True
            self.fields['Document_Description'].widget.attrs['readonly'] = True
            self.fields['Document_Name'].widget.attrs['readonly'] = True
            self.fields['LCMItem'].widget.attrs['readonly'] = True
            self.fields['LCJason'].widget.attrs['readonly'] = True

    def clean_sku(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.Project_ID
        else:
            return self.cleaned_data['ID']

class batch_approve_form(s.ModelForm):
    ID = s.IntegerField(required=False, widget=s.TextInput(attrs={'size': '3'}), label="")
    Project_ID = s.IntegerField(required=False, label="")
    Project_Name = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 25}), required=False, max_length=75,
                               label="")
    Office = s.CharField(max_length=100, widget=s.Textarea(attrs={'rows': 2, 'cols': 25}), required=False, label="")
    Created_By = s.CharField(max_length=50, widget=s.TextInput(attrs={'size': '10'}), label="")
    Project_Status = s.IntegerField(widget=s.HiddenInput(), label="")
    Project_Status_Text = s.CharField(required=False, widget=s.TextInput(attrs={'size': '10'}), label="")
    ApprovePrj = s.BooleanField(required=False, label="Approve this Project", initial=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = project_info
        fields = ('ID', 'Office', 'Project_Name', 'SubActivity', 'Project_Status_Text', 'Created_By', 'ApprovePrj',)

    def __init__(self, *args, **kwargs):
        super(batch_approve_form, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['ID'].widget.attrs['readonly'] = True
            self.fields['ID'].initial = instance.Project_ID
            stat = instance.Project_Status
            if stat == 1:
                self.fields['Project_Status_Text'].initial = 'Planned'
            else:
                self.fields['Project_Status_Text'].initial = 'Implemented'
            self.fields['Office'].widget.attrs['readonly'] = True
            self.fields['Created_By'].widget.attrs['readonly'] = True
            self.fields['Project_Name'].widget.attrs['readonly'] = True
            self.fields['Project_ID'].widget.attrs['readonly'] = True
            self.fields['SubActivity'].widget.attrs['readonly'] = True

            self.fields['Project_Status'].widget.attrs['readonly'] = True

    def clean_sku(self):
        instance = getattr(self, 'instance', None)

        if instance and instance.pk:
            return instance.Office
        else:
            return self.cleaned_data['Office']

class emailcedusers_Form(s.Form):
    gusers = groupusers()
    agusers = agencyusers()
    ousers = officeusers()
    ausers = allusers()
    GroupUsers = s.MultipleChoiceField(choices=gusers, widget=s.CheckboxSelectMultiple, label="Select groups to email",
                                       required=False)
    AgencyUsers = s.MultipleChoiceField(choices=agusers, widget=s.CheckboxSelectMultiple,
                                        label="Select agencies to email", required=False)
    OfficeUsers = s.MultipleChoiceField(choices=ousers, widget=s.CheckboxSelectMultiple,
                                        label="Select offices to email", required=False)
    CEDUsers = s.MultipleChoiceField(choices=ausers, widget=s.CheckboxSelectMultiple,
                                     label="Select individual users to email", required=False)
    Subject = s.CharField(widget=s.TextInput(attrs={'size': '80'}), max_length=100)
    Email_Body = s.CharField(widget=s.Textarea(attrs={'rows': 6, 'cols': 70}), initial="")


class query_Form(s.Form):
    Agency = s.ModelMultipleChoiceField(queryset=imp_party_values.objects.all().order_by('Implementation_Party'),
                                        widget=s.CheckboxSelectMultiple, required=False,
                                        label="Agency/Conservation Partner")
    # Field_Office = s.MultipleChoiceField(choices=offices2, widget=s.CheckboxSelectMultiple, required=False, label = "Office/Name of Agency or Organization")
    Field_Office = s.MultipleChoiceField(widget=s.CheckboxSelectMultiple(attrs={'display': 'inline-block'}),
                                         choices=offices2, required=False,
                                         label="Office/Name of Agency or Organization")
    Imp_Status = s.MultipleChoiceField(widget=s.CheckboxSelectMultiple(attrs={'display': 'inline-block'}),
                                       choices=IMPCHOICES, required=False, label="Implementation Status")
    Effective_Determined = s.MultipleChoiceField(widget=s.CheckboxSelectMultiple, choices=StatusChoice1, required=False,
                                                 label="Effectiveness Status")
    StartSelect = s.ChoiceField(choices=metricequ, required=False, label='Start Year Symbol')
    Start_Year = s.MultipleChoiceField(widget=s.CheckboxSelectMultiple(attrs={'display': 'inline-block'}),
                                       choices=YEARCHOICES, required=False, label="Start Year(s)")
    EndSelect = s.ChoiceField(choices=metricequ, required=False, label='End Year Symbol')
    End_Year = s.MultipleChoiceField(widget=s.CheckboxSelectMultiple(attrs={'display': 'inline-block'}),
                                     choices=YEARCHOICES, required=False, label="End Year(s)")
    TypeAct = s.ModelMultipleChoiceField(queryset=typeact.objects.filter(~Q(id=1)),
                                         widget=s.CheckboxSelectMultiple(attrs={'display': 'inline-block'}),
                                         required=False, label="Activity Type")
    Activity = s.MultipleChoiceField(widget=s.CheckboxSelectMultiple, choices=ActivityLabels, required=False,
                                     label="Activity")
    SubActivity = s.MultipleChoiceField(choices=SubActivityLabels, widget=s.CheckboxSelectMultiple, required=False)
    MetType = s.ChoiceField(choices=metrictypes, required=False, label='Metric Type')
    MetEqu = s.ChoiceField(choices=metricequ, required=False, label='Metric Symbol')
    MetValue = s.FloatField(required=False, label='Metric Value')
    Threats = s.ModelMultipleChoiceField(queryset=threat_values.objects.all(), widget=s.CheckboxSelectMultiple,
                                         required=False)
    WAFWA_Zone = s.ModelMultipleChoiceField(queryset=wafwa_zone_values.objects.all(),
                                            widget=s.CheckboxSelectMultiple(attrs={'display': 'inline-block'}),
                                            required=False, label="WAFWA Zone(s)")
    Sage_Grouse_Population = s.ModelMultipleChoiceField(queryset=population_values.objects.all(),
                                                        widget=s.CheckboxSelectMultiple, required=False,
                                                        label="Population(s)")
    State = s.ModelMultipleChoiceField(queryset=state.objects.all(),
                                       widget=s.CheckboxSelectMultiple(attrs={'display': 'inline-block'}),
                                       required=False, label="State(s)")
    County = s.ModelMultipleChoiceField(queryset=state_county.objects.all(),
                                        widget=s.CheckboxSelectMultiple(attrs={'display': 'inline-block'}),
                                        required=False, label="County(s)")
    Key_Words = s.CharField(widget=s.Textarea(attrs={'rows': 5, 'cols': 85}), initial="", label="Key Word Search",
                            required=False)


class fwsquery_Form(s.Form):
    QueryType = s.ChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=queryypes,
                              required=False, label="Query Type")
    State = s.ModelChoiceField(queryset=state.objects.all(), required=False, label="State")
    WAFWA_Zone = s.ModelChoiceField(queryset=wafwa_zone_values.objects.all(), required=False, label="WAFWA Zone")
    Threat = s.ModelChoiceField(queryset=threat_values.objects.all(), required=False, label="Threats")
    Response = s.ChoiceField(choices=fwsresponses, widget=s.RadioSelect(attrs={'display': 'inline-block'}),
                             required=False, label='FWS Assessment')
    dtrng = []
    for i in range(0, 100):
        dtrng.append(2020 - i)
    DateEqu = s.ChoiceField(choices=datequ, widget=s.RadioSelect(attrs={'display': 'inline-block'}), required=False,
                            label='Date Symbol')
    First_Date = s.DateField(required=False, widget=SelectDateWidget(years=dtrng), label="Start Date")
    Second_Date = s.DateField(required=False, widget=SelectDateWidget(years=dtrng), label="Finish Date")


class fwsreview_display_Form(s.ModelForm):
    Project_ID = s.IntegerField(required=False)
    Threat = s.CharField(max_length=60, required=False)
    Service_Assessment = s.CharField(max_length=255, required=False)
    Service_Assessment_Explained = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 40}), required=False)
    Certifier_Name = s.CharField(max_length=255, required=False)
    Date_Certified = s.DateTimeField()

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = fwsreview
        fields = ('Project_ID', 'Threat', 'Service_Assessment', 'Service_Assessment_Explained', 'Certifier_Name',
                  'Date_Certified')

    def __init__(self, *args, **kwargs):
        super(fwsreview_display_Form, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance:
            self.fields['Project_ID'].widget.attrs['readonly'] = True
            self.fields['Threat'].widget.attrs['readonly'] = True
            self.fields['Service_Assessment'].widget.attrs['readonly'] = True
            self.fields['Service_Assessment_Explained'].widget.attrs['readonly'] = True
            self.fields['Certifier_Name'].widget.attrs['readonly'] = True
            self.fields['Date_Certified'].widget.attrs['readonly'] = True

    def clean_sku(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.Project_ID
        else:
            return self.cleaned_data['Project_ID']

class batch_data_available_Form(s.ModelForm):
    Batch_Group_ID = s.IntegerField(widget=s.TextInput(attrs={'size': '4'}), required=False, label="Batch Group ID")
    BatchUpload_ID = s.IntegerField(widget=s.HiddenInput(), required=False, label="Batch Upload ID")
    Group_Designation = s.CharField(widget=s.TextInput(attrs={'size': '20'}), label="Group", required=False)
    Effort_ID_List = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 30}), label="Effort ID List",
                                 required=False)
    TypeAct = s.CharField(widget=s.HiddenInput(), required=False)
    Group_Status = s.CharField(widget=s.TextInput(attrs={'size': '15'}), label="Group Status", required=False)
    Upload_Date = s.DateTimeField(widget=s.TextInput(attrs={'size': '5'}), required=False)
    Uploading_User = s.CharField(widget=s.TextInput(attrs={'size': '10'}), required=False, label="User")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = batchupload_groups
        fields = (
        'BatchUpload_ID', 'Group_Designation', 'Effort_ID_List', 'Group_Status', 'Upload_Date', 'Uploading_User',
        'Batch_Group_ID')

    def __init__(self, *args, **kwargs):
        super(batch_data_available_Form, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance:
            self.fields['Batch_Group_ID'].widget.attrs['readonly'] = True
            self.fields['BatchUpload_ID'].widget.attrs['readonly'] = True
            self.fields['Group_Designation'].widget.attrs['readonly'] = True
            self.fields['Effort_ID_List'].widget.attrs['readonly'] = True
            self.fields['Group_Status'].widget.attrs['readonly'] = True
            self.fields['Upload_Date'].widget.attrs['readonly'] = True
            self.fields['Uploading_User'].widget.attrs['readonly'] = True

    def clean_sku(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.Batch_Group_ID
        else:
            return self.cleaned_data['Batch_Group_ID']

class batch_s1_Spatial_Form(s.ModelForm):
    Prj_ID = s.IntegerField(widget=s.TextInput(attrs={'size': '2'}), required=False, label="ID")
    Project_Name = s.CharField(widget=s.TextInput(attrs={'size': '20'}), max_length=75, label="Effort Name",
                               required=False)
    Project_Status = s.ChoiceField(choices=IMPCHOICES, label="Effort Status", required=False)
    Activity = s.CharField(widget=s.TextInput(attrs={'size': '40'}), max_length=120, required=False, label="Activity")
    SubActivity = s.ModelChoiceField(queryset=subactivity.objects.all(), required=False, label="SubActivity*")
    dtrng = []
    for i in range(0, 100):
        dtrng.append(2020 - i)
    Start_Date = s.DateField(required=False, widget=SelectDateWidget(years=dtrng), label="Start Date*")
    End_Date = s.DateField(required=False, widget=SelectDateWidget(years=dtrng), label="End Date*")

    Metric = s.ModelChoiceField(queryset=metric.objects.all(), required=False, label="Metric Type*")
    Metric_Value = s.FloatField(required=False, widget=s.TextInput(attrs={'size': '9'}), label="Metric Value*")
    GIS_Acres = s.FloatField(required=False, widget=s.TextInput(attrs={'size': '9'}), label="GIS Acres")

    Objectives_Desc = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 100}), initial="", label='Objectives*',
                                  required=False)
    Notes = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 100}), initial="", label='Notes', required=False)

    Implementing_Party = s.CharField(widget=s.TextInput(attrs={'size': '25'}), label="Implementing Party",
                                     required=False)
    Office = s.CharField(widget=s.TextInput(attrs={'size': '20'}), label="Office", required=False)
    Created_By = s.CharField(widget=s.TextInput(attrs={'size': '10'}), label="Created By", required=False)
    Date_Created = s.DateTimeField(widget=s.TextInput(attrs={'size': '15'}), label="Date Created", required=False)
    User_Email = s.CharField(widget=s.TextInput(attrs={'size': '15'}), label="User Email", required=False)
    Last_Updated = s.DateTimeField(widget=s.TextInput(attrs={'size': '15'}), initial=now, label="Last Updated",
                                   required=False)
    Updating_User = s.CharField(widget=s.TextInput(attrs={'size': '10'}), label="Updating User", required=False)
    Approved = s.IntegerField(widget=s.HiddenInput(), initial=0, required=False)
    Approving_Official = s.CharField(max_length=50, label="Approving Official", required=False)
    Date_Approved = s.DateTimeField(required=False, label="Date Approved")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = project_info
        fields = (
        'Prj_ID', 'Project_Name', 'Project_Status', 'Activity', 'SubActivity', 'Start_Date', 'End_Date', 'Metric',
        'Metric_Value', 'GIS_Acres', 'Implementing_Party', 'Office', 'Created_By', 'Date_Created', 'User_Email',
        'Updating_User', 'Last_Updated', 'Approved', 'Approving_Official', 'Date_Approved', 'Objectives_Desc', 'Notes')

    def __init__(self, *args, **kwargs):
        super(batch_s1_Spatial_Form, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance:
            self.fields['Prj_ID'].widget.attrs['readonly'] = True
            self.fields['Project_Name'].widget.attrs['readonly'] = True
            self.fields['Activity'].widget.attrs['readonly'] = True
            self.fields['GIS_Acres'].widget.attrs['readonly'] = True
            self.fields['Implementing_Party'].widget.attrs['readonly'] = True
            self.fields['Office'].widget.attrs['readonly'] = True
            self.fields['Created_By'].widget.attrs['readonly'] = True
            self.fields['User_Email'].widget.attrs['readonly'] = True
            self.fields['Last_Updated'].widget.attrs['readonly'] = True
            self.fields['Updating_User'].widget.attrs['readonly'] = True
            self.fields['Approved'].widget.attrs['readonly'] = True
            self.fields['Approving_Official'].widget.attrs['readonly'] = True
            self.fields['Date_Approved'].widget.attrs['readonly'] = True

    def clean_sku(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.Prj_ID
        else:
            return self.cleaned_data['Prj_ID']

class batch_s2_Spatial_Form(s.ModelForm):
    Prj_ID = s.IntegerField(widget=s.TextInput(attrs={'size': '2'}), required=False, label="ID")
    Project_Name = s.CharField(widget=s.TextInput(attrs={'size': '20'}), max_length=75, label="Effort Name",
                               required=False)
    Threat = s.ModelMultipleChoiceField(queryset=threat_values.objects.all(), widget=s.CheckboxSelectMultiple,
                                        required=False, label='Threats*')
    Ag_Conversion_Explain = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 50}), initial="",
                                        label='Ag Conversion*', required=False)
    Conifer_Encroach_Explain = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 50}), initial="",
                                           label='Conifers*', required=False)
    Oil_Gas_Explain = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 50}), initial="", label='Oil and Gas*',
                                  required=False)
    Feral_Equids_Explain = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 50}), initial="",
                                       label='Feral Equids*', required=False)
    Infrastructure_Explain = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 50}), initial="",
                                         label='Infrastructure*', required=False)
    Mining_Explain = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 50}), initial="", label='Mining*',
                                 required=False)
    Recreation_Explain = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 50}), initial="", label='Recreation*',
                                     required=False)
    Urban_Devel_Explain = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 50}), initial="",
                                      label='Urban Development*', required=False)
    Fire_Explain = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 50}), initial="", label='Fire*',
                               required=False)
    Improper_Grazing_Explain = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 50}), initial="",
                                           label='Improper Grazing*', required=False)
    Isolated_Explain = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 50}), initial="",
                                   label='Isolated Populations*', required=False)
    Invasives_Explained = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 50}), initial="", label='Invasives*',
                                      required=False)
    Sagebrush_Loss_Explain = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 50}), initial="",
                                         label='Sagebrush Loss*', required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = project_info
        fields = (
        'Prj_ID', 'Project_Name', 'Threat', 'Ag_Conversion_Explain', 'Conifer_Encroach_Explain', 'Oil_Gas_Explain',
        'Fire_Explain', 'Feral_Equids_Explain', 'Improper_Grazing_Explain', 'Infrastructure_Explain',
        'Isolated_Explain', 'Mining_Explain', 'Invasives_Explained', 'Recreation_Explain', 'Sagebrush_Loss_Explain',
        'Urban_Devel_Explain')

    def __init__(self, *args, **kwargs):
        super(batch_s2_Spatial_Form, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance:
            self.fields['Prj_ID'].widget.attrs['readonly'] = True
            self.fields['Project_Name'].widget.attrs['readonly'] = True

    def clean_sku(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.Prj_ID
        else:
            return self.cleaned_data['Prj_ID']

class batch_s3_Spatial_Form(s.ModelForm):
    Prj_ID = s.IntegerField(widget=s.TextInput(attrs={'size': '2'}), required=False, label="ID")
    Project_Name = s.CharField(widget=s.TextInput(attrs={'size': '20'}), max_length=75, label="Effort Name",
                               required=False)
    File_Type1 = s.ChoiceField(choices=File_Types, required=False, label="File_Type1")
    Document_Description1 = s.CharField(widget=s.TextInput(attrs={'size': '27'}), max_length=255, required=False,
                                        label="", initial="")
    Document_Name1 = s.CharField(widget=s.TextInput(attrs={'size': '27'}), max_length=255, required=False,
                                 label="Document_Name", initial="")
    File_Type2 = s.ChoiceField(choices=File_Types, required=False, label="File_Type2")
    Document_Description2 = s.CharField(widget=s.TextInput(attrs={'size': '27'}), max_length=255, required=False,
                                        label="", initial="")
    Document_Name2 = s.CharField(widget=s.TextInput(attrs={'size': '27'}), max_length=255, required=False,
                                 label="Document_Name", initial="")
    File_Type3 = s.ChoiceField(choices=File_Types, required=False, label="File_Type3")
    Document_Description3 = s.CharField(widget=s.TextInput(attrs={'size': '27'}), max_length=255, required=False,
                                        label="", initial="")
    Document_Name3 = s.CharField(widget=s.TextInput(attrs={'size': '27'}), max_length=255, required=False,
                                 label="Document_Name", initial="")
    File_Type4 = s.ChoiceField(choices=File_Types, required=False, label="File_Type4")
    Document_Description4 = s.CharField(widget=s.TextInput(attrs={'size': '27'}), max_length=255, required=False,
                                        label="", initial="")
    Document_Name4 = s.CharField(widget=s.TextInput(attrs={'size': '27'}), max_length=255, required=False,
                                 label="Document_Name", initial="")
    File_Type5 = s.ChoiceField(choices=File_Types, required=False, label="File_Type5")
    Document_Description5 = s.CharField(widget=s.TextInput(attrs={'size': '27'}), max_length=255, required=False,
                                        label="", initial="")
    Document_Name5 = s.CharField(widget=s.TextInput(attrs={'size': '27'}), max_length=255, required=False,
                                 label="Document_Name", initial="")
    File_Type6 = s.ChoiceField(choices=File_Types, required=False, label="File_Type6")
    Document_Description6 = s.CharField(widget=s.TextInput(attrs={'size': '27'}), max_length=255, required=False,
                                        label="", initial="")
    Document_Name6 = s.CharField(widget=s.TextInput(attrs={'size': '27'}), max_length=255, required=False,
                                 label="Document_Name", initial="")
    File_Type7 = s.ChoiceField(choices=File_Types, required=False, label="File_Type7")
    Document_Description7 = s.CharField(widget=s.TextInput(attrs={'size': '27'}), max_length=255, required=False,
                                        label="", initial="")
    Document_Name7 = s.CharField(widget=s.TextInput(attrs={'size': '27'}), max_length=255, required=False,
                                 label="Document_Name", initial="")
    File_Type8 = s.ChoiceField(choices=File_Types, required=False, label="File_Type8")
    Document_Description8 = s.CharField(widget=s.TextInput(attrs={'size': '27'}), max_length=255, required=False,
                                        label="", initial="")
    Document_Name8 = s.CharField(widget=s.TextInput(attrs={'size': '27'}), max_length=255, required=False,
                                 label="Document_Name", initial="")
    File_Type9 = s.ChoiceField(choices=File_Types, required=False, label="File_Type9")
    Document_Description9 = s.CharField(widget=s.TextInput(attrs={'size': '27'}), max_length=255, required=False,
                                        label="", initial="")
    Document_Name9 = s.CharField(widget=s.TextInput(attrs={'size': '27'}), max_length=255, required=False,
                                 label="Document_Name", initial="")
    File_Type10 = s.ChoiceField(choices=File_Types, required=False, label="File_Type10")
    Document_Description10 = s.CharField(widget=s.TextInput(attrs={'size': '27'}), max_length=255, required=False,
                                         label="", initial="")
    Document_Name10 = s.CharField(widget=s.TextInput(attrs={'size': '27'}), max_length=255, required=False,
                                  label="Document_Name", initial="")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = project_info
        fields = ('Prj_ID', 'Project_Name', 'File_Type1', 'Document_Description1', 'Document_Name1', 'File_Type2',
                  'Document_Description2', 'Document_Name2', 'File_Type3', 'Document_Description3', 'Document_Name3',
                  'File_Type4', 'Document_Description4', 'Document_Name4', 'File_Type5', 'Document_Description5',
                  'Document_Name5', 'File_Type6', 'Document_Description6', 'Document_Name6', 'File_Type7',
                  'Document_Description7', 'Document_Name7', 'File_Type8', 'Document_Description8', 'Document_Name8',
                  'File_Type9', 'Document_Description9', 'Document_Name9', 'File_Type10', 'Document_Description10',
                  'Document_Name10')

    def __init__(self, *args, **kwargs):
        super(batch_s3_Spatial_Form, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance:
            self.fields['Prj_ID'].widget.attrs['readonly'] = True
            self.fields['Project_Name'].widget.attrs['readonly'] = True

    def clean_sku(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.Prj_ID
        else:
            return self.cleaned_data['Prj_ID']

class batch_s4_Spatial_Form(s.ModelForm):
    Prj_ID = s.IntegerField(widget=s.TextInput(attrs={'size': '2'}), required=False, label="ID")
    Project_Name = s.CharField(widget=s.TextInput(attrs={'size': '20'}), max_length=75, label="Effort Name",
                               required=False)
    wafwa_value = s.ModelMultipleChoiceField(queryset=wafwa_zone_values.objects.all(), widget=s.CheckboxSelectMultiple,
                                             required=False, label="wafwa_value")
    population_value = s.ModelMultipleChoiceField(queryset=population_values.objects.all().order_by('Populations'),
                                                  widget=s.CheckboxSelectMultiple, required=False,
                                                  label="population_value")
    state_value = s.ModelMultipleChoiceField(queryset=state.objects.all(), widget=s.CheckboxSelectMultiple,
                                             required=False, label="state_value")
    county_value = s.ModelMultipleChoiceField(queryset=state_county.objects.all(), widget=s.CheckboxSelectMultiple,
                                              required=False, label="county_value")
    owner_value = s.ModelMultipleChoiceField(queryset=ownership_values.objects.all().order_by('Owners'),
                                             widget=s.CheckboxSelectMultiple, required=False, label="owner_value")
    collab_party = s.ModelMultipleChoiceField(queryset=imp_party_values.objects.all().order_by('Implementation_Party'),
                                              widget=s.CheckboxSelectMultiple, label="Collaborating Party*",
                                              required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = project_info
        fields = (
        'Prj_ID', 'Project_Name', 'wafwa_value', 'population_value', 'state_value', 'county_value', 'owner_value',
        'collab_party')

    def __init__(self, *args, **kwargs):
        super(batch_s4_Spatial_Form, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance:
            self.fields['Prj_ID'].widget.attrs['readonly'] = True
            self.fields['Project_Name'].widget.attrs['readonly'] = True

    def clean_sku(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.Prj_ID
        else:
            return self.cleaned_data['Prj_ID']

class batch_s5_Spatial_Form(s.ModelForm):
    Project_ID = s.IntegerField(required=False)
    Prj_ID = s.IntegerField(widget=s.TextInput(attrs={'size': '2'}), required=False, label="ID")
    Project_Name = s.CharField(widget=s.TextInput(attrs={'size': '20'}), max_length=75, label="Effort Name",
                               required=False)

    Effective_Determined = s.ChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=StatusChoice1,
                                         required=False, label="Effective", initial=0)
    Effective_Explained = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 50}), required=False,
                                      label="Effective_Explained")

    Reas_Certain = s.ChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=YesNoOnly,
                                 required=False, label="Reas_Certain", initial=0)
    Legal_Authority = s.ChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=YesNoOnly,
                                    required=False, label="Legal_Authority", initial=0)
    Staff_Available = s.ChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=YesNoOnly,
                                    required=False, label="Staff_Available", initial=0)
    Regulatory_Mech = s.ChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=YesNoOnly,
                                    required=False, label="Regulatory_Mech", initial=0)
    Compliance = s.ChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=YesNoOnly,
                               required=False, label="Compliance", initial=0)
    Vol_Incentives = s.ChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=YesNo,
                                   required=False, label="Vol_Incentives", initial=0)

    Reduce_Threats = s.ChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=YesNoOnly,
                                   required=False, label="Reduce_Threats", initial=0)
    Incremental_Objectives = s.ChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=YesNoOnly,
                                           required=False, label="Incremental_Objectives", initial=0)
    Quantifiable_Measures = s.ChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=YesNoOnly,
                                          required=False, label="Quantifiable_Measures", initial=0)
    AD_Strategy = s.ChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=YesNoOnly,
                                required=False, label="AD_Strategy", initial=0)
    Imp_and_Effect_Correct = s.ChoiceField(widget=s.RadioSelect(attrs={'display': 'inline-block'}), choices=YesNo,
                                           required=False, label="Imp_and_Effect_Correct", initial=0)
    Imp_and_Effect_Cor_Explan = s.CharField(widget=s.Textarea(attrs={'rows': 2, 'cols': 50}), required=False,
                                            label="Imp_and_Effect_Cor_Explan")

    Date_Entered = s.DateTimeField(required=False)
    User = s.CharField(max_length=50, required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = implementation_info
        fields = (
        'Prj_ID', 'Project_Name', 'Effective_Determined', 'Effective_Explained', 'Reas_Certain', 'Legal_Authority',
        'Staff_Available', 'Regulatory_Mech', 'Compliance', 'Vol_Incentives', 'Reduce_Threats',
        'Incremental_Objectives', 'Quantifiable_Measures', 'AD_Strategy', 'Imp_and_Effect_Correct',
        'Imp_and_Effect_Cor_Explan', 'Date_Entered', 'User')

    def __init__(self, *args, **kwargs):
        super(batch_s5_Spatial_Form, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance:
            self.fields['Prj_ID'].widget.attrs['readonly'] = True
            self.fields['Project_Name'].widget.attrs['readonly'] = True

    def clean_sku(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.Prj_ID
        else:
            return self.cleaned_data['Prj_ID']