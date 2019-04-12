from django.shortcuts import *
from django.http import *
from django.template import RequestContext, loader
from django.forms.models import modelformset_factory
from django_tables2  import RequestConfig
from django.contrib.auth.decorators import login_required
from ced_main.forms import *
from ced_main.tables import *
from ced_main.models import *
from django.contrib.auth.models import User
from accounts.models import userprofile, useredits, elidgbleusers, usergroups
from django.core.mail import send_mail, EmailMessage
import datetime, time
from django.utils import timezone
import os
# import pysb #python 2.7
import sciencebasepy as pysb
from ced_main.OpenFootprintStudioPassProtectWebPage_v1 import *
from ced_main.Clip_Featureservice_v3 import featurecount


import dbf
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm, mm, inch, pica
from reportlab.platypus.doctemplate import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from django.views.decorators.clickjacking import xframe_options_sameorigin
from accounts.views import checkgroup

# import arcpy
# from arcpy.sa import *
# from arcpy.management import *
# from arcpy.analysis import *
# arcpy.env.overwriteOutput = "True"

import xlsxwriter
import MySQLdb
from django.db.models import Max

from django.conf import settings

from ced.settings import STATIC_DIR




sbpass = settings.SBPASS
sbuser = settings.SBUSER
hst = settings.DBHOST
usr = settings.DBUSER
psswrd = settings.DBPASSWORD
dtbs = settings.DBNAME
DEFAULT_FROM_EMAIL = settings.DEFAULT_FROM_EMAIL

now = datetime.datetime.utcnow()
now = now.replace(tzinfo=timezone.utc)

Conservation_Easement_Choices = (('1', 'Effort is already effective'), ('2', 'Effort has a high likelihood of being effective given adequate time'), ('3', 'Effort is uncertain or unlikely to be effective'))

Land_Acquisition_Choices = (('4', 'Effort is already effective'), ('5', 'Effort has a high likelihood of being effective given adequate time'), ('6', 'Effort is uncertain or unlikely to be effective'))

Fuel_Breaks_Choices = (('7', 'Effort is already effective'), ('8', 'Effort has a high likelihood of being effective given adequate time'), ('9', 'Effort is uncertain or unlikely to be effective'))

Conifer_Removal_Choices = (('10', 'Effort is already effective (only applicable for objective 3)'), ('11', 'Effort is already effective'), ('12', 'Effort has a high likelihood of being effective given adequate time'), ('13', 'Effort is uncertain or unlikely to be effective'))

Vegetation_Management_Choices = (('14', 'Effort is already effective'), ('15', 'Effort has a high likelihood of being effective given adequate time'), ('16', 'Effort is uncertain or unlikely to be effective'))

Fuels_Management_Choices = (('17', 'Effort is already effective'), ('18', 'Effort is already effective'), ('19', 'Effort has a high likelihood of being effective given adequate time'), ('20', 'Effort is uncertain or unlikely to be effective'))

Annual_Grass_Choices = (('21', 'Effort is already effective'), ('22', 'Effort has a high likelihood of being effective given adequate time'), ('23', 'Effort is uncertain or unlikely to be effective'))

Noxious_Weed_Choices = (('24', 'Effort is already effective'), ('25', 'Effort has a high likelihood of being effective given adequate time'), ('26', 'Effort is uncertain or unlikely to be effective'))

Riparian_Choices = (('27', 'Effort is already effective'), ('28', 'Effort has a high likelihood of being effective given adequate time'), ('29', 'Effort is uncertain or unlikely to be effective'))

Energy_Development_Choices = (('30', 'Effort is already effective'), ('31', 'Effort has a high likelihood of being effective given adequate time'), ('32', 'Effort is uncertain or unlikely to be effective'))

Area_Closure_Choices = (('33', 'Effort is already effective'), ('34', 'Effort has a high likelihood of being effective given adequate time'), ('35', 'Effort is uncertain or unlikely to be effective'))

Improved_Grazing_Choices = (('36', 'Effort is already effective'), ('37', 'Effort has a high likelihood of being effective given adequate time'), ('38', 'Effort is uncertain or unlikely to be effective'))

Road_Closure_Choices = (('39', 'Effort is already effective'), ('40', 'Effort has a high likelihood of being effective given adequate time'), ('41', 'Effort is uncertain or unlikely to be effective'))

Rerouted_Roads_Choices = (('42', 'Effort is already effective'), ('43', 'Effort has a high likelihood of being effective given adequate time'), ('44', 'Effort is uncertain or unlikely to be effective'))

Powerline_Retrofitting_Choices = (('45', 'Effort is already effective'), ('46', 'Effort has a high likelihood of being effective given adequate time'), ('47', 'Effort is uncertain or unlikely to be effective'))

Powerline_Burial_Choices = (('48', 'Effort is already effective'), ('49', 'Effort has a high likelihood of being effective given adequate time'), ('50', 'Effort is uncertain or unlikely to be effective'))

Structure_Removal_Choices = (('51', 'Effort is already effective'), ('52', 'Effort has a high likelihood of being effective given adequate time'), ('53', 'Effort is uncertain or unlikely to be effective'))

Fence_Marking_Choices = (('54', 'Effort is already effective'), ('55', 'Effort has a high likelihood of being effective given adequate time'), ('56', 'Effort is uncertain or unlikely to be effective'))

Fence_Modification_Choices = (('57', 'Effort is already effective'), ('58', 'Effort has a high likelihood of being effective given adequate time'), ('59', 'Effort is uncertain or unlikely to be effective'))

Fence_Removal = (('60', 'Effort is already effective'), ('61', 'Effort has a high likelihood of being effective given adequate time'), ('62', 'Effort is uncertain or unlikely to be effective'))

Population_Control_Choices = (('63', 'Effort is already effective'), ('64', 'Effort has a high likelihood of being effective given adequate time'), ('65', 'Effort is uncertain or unlikely to be effective'))

Gather_Choices = (('66', 'Effort is already effective'), ('67', 'Effort has a high likelihood of being effective given adequate time'), ('68', 'Effort is uncertain or unlikely to be effective'))

Translocation_Choices = (('69', 'Effort is already effective'), ('70', 'Effort has a high likelihood of being effective given adequate time'), ('71', 'Effort is uncertain or unlikely to be effective'))


def getimpchoices(subact):
    if subact == "Conservation Easement":
        return Conservation_Easement_Choices
    elif subact == "Land Acquisition":
        return Land_Acquisition_Choices
    elif subact == "Fuel Breaks":
        return Fuel_Breaks_Choices
    elif subact == "Conifer Removal (All Phases)":
        return Conifer_Removal_Choices
    elif subact == "Vegetation Management / Habitat Enhancement":
        return Vegetation_Management_Choices
    elif subact == "Fuels Management":
        return Fuels_Management_Choices
    elif subact == "Annual Grass Treatments":
        return Annual_Grass_Choices
    elif subact == "Noxious Weed Treatments":
        return Noxious_Weed_Choices
    elif subact == "Riparian, Wet Meadow or Spring Restoration":
        return Riparian_Choices
    elif subact == "Energy development reclamation with the goal of sagebrush restoration":
        return Energy_Development_Choices
    elif subact == "Area Closure":
        return Area_Closure_Choices
    elif subact == "Improved Grazing Practices (Rest, Rotation, Etc.)":
        return Improved_Grazing_Choices
    elif subact == "Road and Trail closure":
        return Road_Closure_Choices
    elif subact == "Rerouted Roads and/or Trails":
        return Rerouted_Roads_Choices
    elif subact == "Powerline Retrofitting / Modification":
        return Powerline_Retrofitting_Choices
    elif subact == "Powerline Burial":
        return Powerline_Burial_Choices
    elif subact == "Structure Removal":
        return Structure_Removal_Choices
    elif subact == "Fence Marking":
        return Fence_Marking_Choices
    elif subact == "Fence Modification":
        return Fence_Modification_Choices
    elif subact == "Fence Removal":
        return Fence_Removal
    elif subact == "Wild Equid Population Control":
        return Population_Control_Choices
    elif subact == "Wild Equid Gather":
        return Gather_Choices
    elif subact == "Translocation":
        return Translocation_Choices
    else:
        return Fence_Removal

def getcount(cntVal):
    cnt = 0
    for cntV in cntVal:
        cnt = cnt + 1
    if cnt > 0:
        return 0
    else:
        return -1

def gettables():
    threavaltest1 = threats.objects.all()
    activitytest1 = activity.objects.all()
    subactivitytest1 = subactivity.objects.all()
    wafwatest1 = wafwa_info.objects.all()
    return threavaltest1, activitytest1, subactivitytest1, wafwatest1

def gettablesfws(stval):
    stateval11 = state_info.objects.values_list('Project_ID', flat=True).filter(State_Value=stval)
    return stateval11

def gettablesfwswa(waval):
    wafwaval11 = wafwa_info.objects.values_list('Project_ID', flat=True).filter(WAFWA_Value=waval)
    return wafwaval11

def gettablesfwspo(poval):
    popval11 = population_info.objects.values_list('Project_ID', flat=True).filter(Population_Value=poval)
    return popval11

def gettablesfwsth(thval):
    thval11 = threats.objects.values_list('Project_ID', flat=True).filter(Threat=thval)
    return thval11

def gettablesfwsii(impval):
    iival11 = implementation_info.objects.values_list('Project_ID', flat=True).filter(Effective_Determined=impval)
    return iival11

def gettablesfwsprj(prjid12, field):
    prj11 = project_info.objects.values_list(field, flat=True).get(Project_ID=str(prjid12))
    return prj11

def metricget(prjid, met):
    prjid = int(prjid)
    met = str(met)
    try:
        mval = metrics.objects.values_list(met, flat=True).get(Project_ID=prjid)
    except:
        mval = 0
    if mval > 0 and mval < 10000000000000:
        test = 'test'
    else:
        mval = 0
    return mval

def gettext(value):
    if value == 1:
        return "Yes"
    elif value == 2:
        return "No"
    else:
        return ""

def gettext1(value):
    if value == 1:
        return "Yes"
    elif value == 2:
        return "No"
    else:
        return "None"

def getusers(emails, typeem):
    editusersget = User.objects.all()
    editusers = []
    if typeem == 'Group':
        if emails == 'AllUsers':
            for email in editusersget:
                emailuser = User.objects.values_list('email', flat=True).get(username=email)
                editusers.append(emailuser)

        if emails == 'ApprovedUsers':
            for email in editusersget:
                approved = userprofile.objects.values_list('User_Approved', flat=True).get(
                    User_id=User.objects.get(username=email))
                if approved == 1:
                    emailuser = User.objects.values_list('email', flat=True).get(username=email)
                    editusers.append(emailuser)

        if emails == 'Admin':
            for email in editusersget:
                approved = usergroups.objects.values_list('groupid', flat=True).filter(
                    userid=User.objects.get(username=email))
                for app in approved:
                    if app == 3:
                        emailuser = User.objects.values_list('email', flat=True).get(username=email)
                        editusers.append(emailuser)

        if emails == 'Approve':
            for email in editusersget:
                approved = usergroups.objects.values_list('groupid', flat=True).filter(
                    userid=User.objects.get(username=email))
                for app in approved:
                    if app == 1:
                        emailuser = User.objects.values_list('email', flat=True).get(username=email)
                        editusers.append(emailuser)

        if emails == 'DemoUsers':
            for email in editusersget:
                office = userprofile.objects.values_list('Field_Office', flat=True).get(
                    User_id=User.objects.get(username=email))
                if office == 'DEMONSTRATION USER ACCESS ONLY':
                    emailuser = User.objects.values_list('email', flat=True).get(username=email)
                    editusers.append(emailuser)

        if emails == 'IncompleteUsers':
            for email in editusersget:
                approved = userprofile.objects.values_list('User_Approved', flat=True).get(
                    User_id=User.objects.get(username=email))
                if approved == 0:
                    emailuser = User.objects.values_list('email', flat=True).get(username=email)
                    editusers.append(emailuser)

    if typeem == 'Agency':
        for email in editusersget:
            agency = userprofile.objects.values_list('Agency', flat=True).get(User_id=User.objects.get(username=email))
            if agency == emails:
                emailuser = User.objects.values_list('email', flat=True).get(username=email)
                editusers.append(emailuser)

    if typeem == 'Office':
        for email in editusersget:
            office = userprofile.objects.values_list('Field_Office', flat=True).get(
                User_id=User.objects.get(username=email))
            if office == emails:
                emailuser = User.objects.values_list('email', flat=True).get(username=email)
                editusers.append(emailuser)

    return editusers


def checkauthorization(prjid, username):
    ## Ensures that a user is not authorized to edit a project by default
    authorized = "NotAuthorized"
    ## If the user created the project they can edit it
    CreateBy = project_info.objects.values_list('Created_By', flat=True).get(pk=prjid)
    if str(CreateBy) == str(username):
        authorized = "Authorized"
    ## If the user modified the project they can edit it
    AuthorTest = project_info.objects.values_list('Updating_User', flat=True).get(pk=prjid)
    if str(AuthorTest) == str(username):
        authorized = "Authorized"
    ## If the user is an approving official they can edit it
    AppTest = project_info.objects.values_list('Approving_Official', flat=True).get(pk=prjid)
    if str(AppTest) == str(username):
        authorized = "Authorized"
    ## If the user has been selected by user to be able to edit the project
    try:
        icanedit = useredits.objects.values_list('userid', flat=True).filter(
            editinguser=elidgbleusers.objects.get(username=username))
        ican1 = []
        icnt = 1
        for ican in icanedit:
            username = User.objects.get(id=ican)
            prjscrt = project_info.objects.filter(Created_By__exact=username)
            for prjs in prjscrt:
                if str(prjs) == str(prjid):
                    authorized = "Authorized"
    except:
        authorized = "NotAuthorized"
    return authorized


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.setFont("Helvetica", 7)
        self.drawRightString(200 * mm, 20 * mm,
                             "Page %d of %d" % (self._pageNumber, page_count))
        #TODO
        image = os.path.join(STATIC_DIR, 'ced_main/images/ced_main/ErrRptBanner.jpg')
        self.drawImage(image, 0 * inch, 11 * inch, width=8.27 * inch, height=0.75 * inch)


def deletethewholeproject(prid):
    # Delete the documentation
    try:
        documentid = documentation.objects.values_list('id', flat=True).filter(Project_ID=prid)
        for docid in documentid:
            dclcid = documentation.objects.values_list('LCMItem', flat=True).get(id=docid)
            try:  # Delete document from Science Base
                deletefromLCMap(dclcid)
            except:
                print("No document exists in Science Base")

            try:  # Delete document from CED
                documentation.objects.get(id=docid).delete()
            except:
                print("Document cannot be deleted")
    except:
        print("No documents to delete")

    try:  # Delete all threats for the project
        threats.objects.get(Project_ID=prid).delete()
    except:
        print("No threats to delete")

    try:  # Delete all threats for the project
        metrics.objects.get(Project_ID=prid).delete()
    except:
        print("No metrics to delete")

    try:  # Delete all threats for the project
        agreement_protect.objects.get(Project_ID=prid).delete()
    except:
        print("No agreement protections to delete")

    try:  # Delete all wafwa_info for the project
        wafwa_info.objects.get(Project_ID=prid).delete()
    except:
        print("No wafwa_info to delete")

    try:  # Delete all state_info for the project
        state_info.objects.get(Project_ID=prid).delete()
    except:
        print("No state_info to delete")

    try:  # Delete all population_info for the project
        population_info.objects.get(Project_ID=prid).delete()
    except:
        print("No population_info to delete")

    try:  # Delete all county_info for the project
        county_info.objects.get(Project_ID=prid).delete()
    except:
        print("No county_info to delete")

    try:  # Delete all huc12_info for the project
        huc12_info.objects.get(Project_ID=prid).delete()
    except:
        print("No huc12_info to delete")

    try:  # Delete all ownership_info for the project
        ownership_info.objects.get(Project_ID=prid).delete()
    except:
        print("No ownership_info to delete")

    try:  # Delete all implementation_info for the project
        implementation_info.objects.get(Project_ID=prid).delete()
    except:
        print("No implementation_info to delete")

    try:  # Delete all collab_party for the project
        collab_party.objects.get(Project_ID=prid).delete()
    except:
        print("No collab_party to delete")

    # Delete the shapefile
    try:
        spatialid = project_info.objects.values_list('Shapefile', flat=True).get(Project_ID=prid)
        deletefromLCMap(spatialid)
    except:
        print("No Shapefile exists")

    # Delete the project folder
    try:
        prjfoldid = project_info.objects.values_list('LCMItem', flat=True).get(Project_ID=prid)
        deletefromLCMap(prjfoldid)
    except:
        print("No Project folder exists")

    try:  # Delete project from CED
        project_info.objects.get(Project_ID=prid).delete()
    except:
        print("Project cannot be deleted")

    return "Done"


def checkallprojects(prjids, un, useremail, FN, LN):
    date1 = now.strftime("%Y-%m-%d")
    #TODO
    testpdf = "C:/Users/sgce/ced_spatial_data/temp_files/" + un + "_Error_List_" + str(date1) + ".pdf"
    if os.path.isfile(testpdf):
        os.remove(testpdf)

    doc = SimpleDocTemplate(testpdf, leftMargin=0.5 * inch, rightMargin=0.5 * inch, )
    Catalog = []
    styles = getSampleStyleSheet()
    styleh1 = styles['Heading1']
    styleh2 = styles['Heading2']
    styleh3 = styles['Heading3']

    p = Paragraph('Conservation Efforts Error Check Report', styleh1)
    Catalog.append(p)
    p = Paragraph('Error List Prepared For ' + FN + " " + LN, styleh2)
    Catalog.append(p)
    date2 = now.strftime("%Y-%m-%d") + ' at ' + time.strftime("%H:%M")
    p = Paragraph('Prepared on ' + date2, styleh2)
    Catalog.append(p)
    s = Spacer(1, 0.5 * inch)
    Catalog.append(s)
    style = styles['Normal']

    testcnt = 0
    for prjid in prjids:

        uploadfeature = project_info.objects.values_list('Shapefile', flat=True).get(pk=int(prjid))
        Project_Name = project_info.objects.values_list('Project_Name', flat=True).get(pk=int(prjid))
        # Check for missing values

        errorcount, errorsreturned = checkproject(prjid, uploadfeature)

        for errcnts in errorcount:
            errcnt = int(errcnts)

        p = Paragraph('Errors for Project: ' + Project_Name, styleh2)
        Catalog.append(p)
        s = Spacer(1, 0.1 * inch)
        Catalog.append(s)
        errorlist = 1
        if errcnt > 0:
            p = Paragraph('The following ' + str(
                errcnt) + ' errors have been detected within the project ' + Project_Name + ' and must be corrected before it can be submited',
                          styleh3)
            Catalog.append(p)
            s = Spacer(1, 0.1 * inch)
            Catalog.append(s)
            for miss in errorsreturned:
                p = Paragraph('(' + str(errorlist) + ') ' + miss[1], style)
                Catalog.append(p)
                s = Spacer(1, 0.05 * inch)
                Catalog.append(s)
                errorlist = errorlist + 1
        s = Spacer(1, 0.15 * inch)
        Catalog.append(s)
        testcnt = testcnt + 1
        s = Spacer(1, 0.5 * inch)
        Catalog.append(s)

    doc.build(Catalog, canvasmaker=NumberedCanvas)
    message = EmailMessage("Batch Upload Errors",
                           "Please see the attached text file to identify all errors related to your recent error check request in the Conservation Efforts Database",
                           "fw1sagegrouseced@fws.gov", [useremail])
    attachment = open(testpdf, 'rb')
    message.attach(un + "_Error_List_" + str(date1) + ".pdf", attachment.read(), 'application/pdf')
    message.send()
    attachment.close()
    delsuc = 0
    time.sleep(2)
    while delsuc < 1:
        try:
            if os.path.isfile(testpdf):
                os.remove(testpdf)
                delsuc = 1
        except:
            time.sleep(0.25)
            delsuc = 0

    return "Success"


def checkproject(prjid, spatialid):
    errorcnt = 0
    missingdata = []

    ### Activity Information ###

    # Check for a project name
    prjnm = project_info.objects.values_list('Project_Name', flat=True).get(pk=prjid)
    if prjnm == None or prjnm == "":
        missingdata.append(["PrjNmEr", "Activity Information Error: A CED Effort Name is Required", "Activity"])
        errorcnt = errorcnt + 1

    # Check for activity and metric information if applicable
    efttype = "---Select an Effort Type---"
    acttype = "---Select an Activity---"
    subacttype = "---Select a Subactivity---"
    typeact = project_info.objects.values_list('TypeAct', flat=True).get(pk=prjid)
    if typeact == None or typeact == "" or typeact == efttype:
        missingdata.append(["TypeActEr", "Activity Information Error: No Activity Type Listed", "Activity"])
        errorcnt = errorcnt + 1

    activity = project_info.objects.values_list('Activity', flat=True).get(pk=prjid)
    if activity == None or activity == "" or activity == efttype or activity == acttype:
        missingdata.append(["ActivityEr", "Activity Information Error: No Activity Listed", "Activity"])
        errorcnt = errorcnt + 1

    subactivity = project_info.objects.values_list('SubActivity', flat=True).get(pk=prjid)
    if subactivity == None or subactivity == "" or subactivity == efttype or subactivity == acttype or subactivity == subacttype:
        missingdata.append(["SubActivityEr", "Activity Information Error: No SubActivity Listed", "Activity"])
        errorcnt = errorcnt + 1

    if typeact == "Project":
        metricvals = ['BreedingNestingAcres', 'BroodRearingAcres', 'WinterAcres', 'TotalAcres', 'BreedingNestingMiles',
                      'BroodRearingMiles', 'WinterMiles', 'TotalMiles', 'BreedingNestingNumberBirds',
                      'BroodRearingNumberBirds', 'WinterNumberBirds', 'TotalNumberBirds',
                      'BreedingNestingNumberRemoved', 'BroodRearingNumberRemoved', 'WinterNumberRemoved',
                      'TotalNumberRemoved', 'BreedingNestingNumberKilled', 'BroodRearingNumberKilled',
                      'WinterNumberKilled', 'TotalNumberKilled', 'BreedingNestingEquids', 'BroodRearingEquids',
                      'WinterEquids', 'TotalEquids']

        metvalexists = 0

        nonacreval = 0
        nonmileval = 0
        nonnumbirdval = 0
        nonnumbremval = 0
        nonkillval = 0
        nonequidval = 0

        totalacreval = 0
        totalmileval = 0
        totalnumbirdval = 0
        totalnumbremval = 0
        totalkillval = 0
        totalequidval = 0

        for metr in metricvals:
            try:
                metric = metrics.objects.values_list(metr, flat=True).get(Project_ID=prjid)
                if metric > 0:
                    if metr == 'BreedingNestingAcres' or metr == 'BroodRearingAcres' or metr == 'WinterAcres' or metr == 'TotalAcres':
                        if metr != 'TotalAcres':
                            if metric > nonacreval:
                                nonacreval = metric
                        else:
                            totalacreval = metric

                    if metr == 'BreedingNestingMiles' or metr == 'BroodRearingMiles' or metr == 'WinterMiles' or metr == 'TotalMiles':
                        if metr != 'TotalMiles':
                            if metric > nonmileval:
                                nonmileval = metric
                        else:
                            totalmileval = metric

                    if metr == 'BreedingNestingNumberBirds' or metr == 'BroodRearingNumberBirds' or metr == 'WinterNumberBirds' or metr == 'TotalNumberBirds':
                        if metr != 'TotalNumberBirds':
                            if metric > nonnumbirdval:
                                nonnumbirdval = metric
                        else:
                            totalnumbirdval = metric

                    if metr == 'BreedingNestingNumberRemoved' or metr == 'BroodRearingNumberRemoved' or metr == 'WinterNumberRemoved' or metr == 'TotalNumberRemoved':
                        if metr != 'TotalNumberRemoved':
                            if metric > nonnumbremval:
                                nonnumbremval = metric
                        else:
                            totalnumbremval = metric

                    if metr == 'BreedingNestingNumberKilled' or metr == 'BroodRearingNumberKilled' or metr == 'WinterNumberKilled' or metr == 'TotalNumberKilled':
                        if metr != 'TotalNumberKilled':
                            if metric > nonkillval:
                                nonkillval = metric
                        else:
                            totalkillval = metric

                    if metr == 'BreedingNestingEquids' or metr == 'BroodRearingEquids' or metr == 'WinterEquids' or metr == 'TotalEquids':
                        if metr != 'TotalEquids':
                            if metric > nonequidval:
                                nonequidval = metric
                        else:
                            totalequidval = metric
                    metvalexists = 1
            except:
                rec = "rec"

        if metvalexists == 0:
            missingdata.append(
                ["MetricEr", "Activity Information Error: At least one metric value is required", "Activity"])
            errorcnt = errorcnt + 1
        else:
            if nonacreval > 0 and totalacreval == 0:
                missingdata.append(["MetricEr",
                                    "Activity Information Error: The metric 'Total Acres' cannot be 0 if Breeding, Brood-rearing, or Winter acres are greater than 0.",
                                    "Activity"])
                errorcnt = errorcnt + 1

            if (nonacreval > totalacreval) and totalacreval > 0:
                missingdata.append(["MetricEr",
                                    "Activity Information Error: The metric 'Total Acres' cannot be less than the largest value of any one of the following fields Breeding, Brood-rearing, or Winter acres.",
                                    "Activity"])
                errorcnt = errorcnt + 1

            if nonmileval > 0 and totalmileval == 0:
                missingdata.append(["MetricEr",
                                    "Activity Information Error: The metric 'Total Miles' cannot be 0 if Breeding, Brood-rearing, or Winter miles are greater than 0.",
                                    "Activity"])
                errorcnt = errorcnt + 1

            if (nonmileval > totalmileval) and totalmileval > 0:
                missingdata.append(["MetricEr",
                                    "Activity Information Error: The metric 'Total Miles' cannot be less than the largest value of any one of the following fields Breeding, Brood-rearing, or Winter miles.",
                                    "Activity"])
                errorcnt = errorcnt + 1

            if nonnumbirdval > 0 and totalnumbirdval == 0:
                missingdata.append(["MetricEr",
                                    "Activity Information Error: The metric 'Total Number of Birds' cannot be 0 if Breeding, Brood-rearing, or Winter number of birds are greater than 0.",
                                    "Activity"])
                errorcnt = errorcnt + 1

            if (nonnumbirdval > totalnumbirdval) and totalnumbirdval > 0:
                missingdata.append(["MetricEr",
                                    "Activity Information Error: The metric 'Total Number of Birds' cannot be less than the largest value of any one of the following fields Breeding, Brood-rearing, or Winter number of birds.",
                                    "Activity"])
                errorcnt = errorcnt + 1

            if nonnumbremval > 0 and totalnumbremval == 0:
                missingdata.append(["MetricEr",
                                    "Activity Information Error: The metric 'Total Number Removed' cannot be 0 if Breeding, Brood-rearing, or Winter number removed are greater than 0.",
                                    "Activity"])
                errorcnt = errorcnt + 1

            if (nonnumbremval > totalnumbremval) and totalnumbremval > 0:
                missingdata.append(["MetricEr",
                                    "Activity Information Error: The metric 'Total Number Removed' cannot be less than the largest value of any one of the following fields Breeding, Brood-rearing, or Winter number removed.",
                                    "Activity"])
                errorcnt = errorcnt + 1

            if nonkillval > 0 and totalkillval == 0:
                missingdata.append(["MetricEr",
                                    "Activity Information Error: The metric 'Total Number Killed' cannot be 0 if Breeding, Brood-rearing, or Winter number killed are greater than 0.",
                                    "Activity"])
                errorcnt = errorcnt + 1

            if (nonkillval > totalkillval) and totalkillval > 0:
                missingdata.append(["MetricEr",
                                    "Activity Information Error: The metric 'Total Number Killed' cannot be less than the largest value of any one of the following fields Breeding, Brood-rearing, or Winter number killed.",
                                    "Activity"])
                errorcnt = errorcnt + 1

            if nonequidval > 0 and totalequidval == 0:
                missingdata.append(["MetricEr",
                                    "Activity Information Error: The metric 'Total Equids Removed' cannot be 0 if Breeding, Brood-rearing, or Winter equids removed are greater than 0.",
                                    "Activity"])
                errorcnt = errorcnt + 1

            if (nonequidval > totalequidval) and totalequidval > 0:
                missingdata.append(["MetricEr",
                                    "Activity Information Error: The metric 'Total Equids Removed' cannot be less than the largest value of any one of the following fields Breeding, Brood-rearing, or Winter equids removed.",
                                    "Activity"])
                errorcnt = errorcnt + 1

    Sage_Elim = agreement_protect.objects.values_list('Sage_Elim', flat=True).get(Project_ID=prjid)
    if str(Sage_Elim) != "None":
        if Sage_Elim > 100 or Sage_Elim < 0:
            missingdata.append(["AgrProEr",
                                "Activity Information Error: The agreement the activity protects against 'Sagebrush Elimination' must be between 0-100.",
                                "Activity"])
            errorcnt = errorcnt + 1

    Ag_Conv = agreement_protect.objects.values_list('Ag_Conv', flat=True).get(Project_ID=prjid)
    if str(Ag_Conv) != "None":
        if Ag_Conv > 100 or Ag_Conv < 0:
            missingdata.append(["AgrProEr",
                                "Activity Information Error: The agreement the activity protects against 'Agricultural Conversion' must be between 0-100.",
                                "Activity"])
            errorcnt = errorcnt + 1

    Improper_Graze = agreement_protect.objects.values_list('Improper_Graze', flat=True).get(Project_ID=prjid)
    if str(Improper_Graze) != "None":
        if Improper_Graze > 100 or Improper_Graze < 0:
            missingdata.append(["AgrProEr",
                                "Activity Information Error: The agreement the activity protects against 'Improper Grazing' must be between 0-100.",
                                "Activity"])
            errorcnt = errorcnt + 1

    Infastructure = agreement_protect.objects.values_list('Infastructure', flat=True).get(Project_ID=prjid)
    if str(Infastructure) != "None":
        if Infastructure > 100 or Infastructure < 0:
            missingdata.append(["AgrProEr",
                                "Activity Information Error: The agreement the activity protects against 'Infastructure' must be between 0-100.",
                                "Activity"])
            errorcnt = errorcnt + 1

    Ener = agreement_protect.objects.values_list('Energy_Development', flat=True).get(Project_ID=prjid)
    if str(Ener) != "None":
        if Ener > 100 or Ener < 0:
            missingdata.append(["AgrProEr",
                                "Activity Information Error: The agreement the activity protects against 'Renewable Energy Resources' must be between 0-100.",
                                "Activity"])
            errorcnt = errorcnt + 1

    Mining = agreement_protect.objects.values_list('Mining', flat=True).get(Project_ID=prjid)
    if str(Mining) != "None":
        if Mining > 100 or Mining < 0:
            missingdata.append(["AgrProEr",
                                "Activity Information Error: The agreement the activity protects against 'Mining' must be between 0-100.",
                                "Activity"])
            errorcnt = errorcnt + 1

    Recreation = agreement_protect.objects.values_list('Recreation', flat=True).get(Project_ID=prjid)
    if str(Recreation) != "None":
        if Recreation > 100 or Recreation < 0:
            missingdata.append(["AgrProEr",
                                "Activity Information Error: The agreement the activity protects against 'Recreation' must be between 0-100.",
                                "Activity"])
            errorcnt = errorcnt + 1

    Urbanization = agreement_protect.objects.values_list('Urbanization_SubDevel', flat=True).get(Project_ID=prjid)
    if str(Urbanization) != "None":
        if Urbanization > 100 or Urbanization < 0:
            missingdata.append(["AgrProEr",
                                "Activity Information Error: The agreement the activity protects against 'Urbanization_SubDevel' must be between 0-100.",
                                "Activity"])
            errorcnt = errorcnt + 1

    # Threats Addressed
    threatsadd = threats.objects.values_list('Threat', flat=True).filter(Project_ID=prjid)
    thrtscnt = 0
    for thradd in threatsadd:
        thrtscnt = thrtscnt + 1
    if thrtscnt < 1:
        missingdata.append(
            ["ThreatsEr", "Activity Information Error: No threats addressed have been identified", "Activity"])
        errorcnt = errorcnt + 1

    # Documentation
    documentsadd = documentation.objects.values_list('id', flat=True).filter(Project_ID=prjid)
    docscnt = 0
    for docadd in documentsadd:
        filetype = documentation.objects.values_list('File_Type', flat=True).get(id=docadd)

        if filetype == None or filetype == "" or filetype == "---Select/Update File Type---":
            missingdata.append(
                ["FileTypeEr", "Documentation Error: File Type missing for some documentation", "Documentation"])
            errorcnt = errorcnt + 1
        docdesc = documentation.objects.values_list('Document_Description', flat=True).get(id=docadd)

        if docdesc == None or docdesc == "":
            missingdata.append(
                ["DescriptionEr", "Documentation Error: Documentation Description missing for some documentation",
                 "Documentation"])
            errorcnt = errorcnt + 1
        docscnt = docscnt + 1

    ### Location Information ###
    # Check for spatial data
    if spatialid == "" or spatialid == "Null" or spatialid == "None" or spatialid == None:
        missingdata.append(["Spatial", "Spatial Data Error: No Spatial Data", "Spatial"])
        errorcnt = errorcnt + 1
    else:
        featcnt = featurecount(spatialid)
        if featcnt == 0:
            missingdata.append(["Spatial", "Spatial Data Error: No Spatial Data", "Spatial"])
            errorcnt = errorcnt + 1

    # Check for WAFWA Zone
    wafwasadd = wafwa_info.objects.values_list('WAFWA_Value', flat=True).filter(Project_ID=prjid)
    wafwascnt = 0
    wafwalist = []
    for wafwaadd in wafwasadd:
        wafwali = wafwa_zone_values.objects.values_list('WAFWA_Zone', flat=True).get(id=wafwaadd)
        wafwalist.append(wafwali)
        wafwascnt = wafwascnt + 1
    if wafwascnt < 1:
        missingdata.append(["WAFWAEr", "Location Information Error: No WAFWA Zones have been identified"], "Location")
        errorcnt = errorcnt + 1

    # Check for SG Populations Zone
    popsadd = population_info.objects.values_list('Population_Value', flat=True).filter(Project_ID=prjid)
    popscnt = 0
    poplist = []
    for popadd in popsadd:
        popli = population_values.objects.values_list('Populations', flat=True).get(id=popadd)
        poplist.append(popli)
        popscnt = popscnt + 1
    if popscnt < 1:
        missingdata.append(["PopulationsEr",
                            "Location Information Error: No Sage Grouse Populations have been identified. If this location is accurate please contact the CED team to continue with approval for this project.",
                            "Location"])
        errorcnt = errorcnt + 1

    # Check for States
    statesadd = state_info.objects.values_list('State_Value', flat=True).filter(Project_ID=prjid)
    statescnt = 0
    statelist = []
    for stateadd in statesadd:
        stateli = state.objects.values_list('State', flat=True).get(id=stateadd)
        statelist.append(stateli)
        statescnt = statescnt + 1
    if statescnt < 1:
        missingdata.append(["StatesEr", "Location Information Error: No States have been identified", "Location"])
        errorcnt = errorcnt + 1
    stateskip = 0
    if statescnt == 1 and stateli == "AB":
        stateskip = 1
    if stateskip == 0:
        # Check for Counties
        countysadd = county_info.objects.values_list('County_Value', flat=True).filter(Project_ID=prjid)
        countyscnt = 0
        countylist = []
        for countyadd in countysadd:
            countyli = state_county.objects.values_list('Cnty_St', flat=True).get(id=countyadd)
            countylis = countyli.split(",")
            countylist.append(countylis[0])
            countyscnt = countyscnt + 1
        if countyscnt < 1:
            missingdata.append(
                ["CountiesEr", "Location Information Error: No Counties have been identified", "Location"])
            errorcnt = errorcnt + 1

        # Check for HUC 12 Zones
        hucsadd = huc12_info.objects.values_list('HUC12_Value', flat=True).filter(Project_ID=prjid)
        hucscnt = 0
        huclist = []
        for hucadd in hucsadd:
            hucli = state_county_huc12_values.objects.values_list('HUC12_Cnty_State', flat=True).get(id=hucadd)
            huclis = hucli.split(",")
            huclist.append(huclis[0])
            hucscnt = hucscnt + 1
        if hucscnt < 1:
            missingdata.append(
                ["HUC12Er", "Location Information Error: No HUC 12 Zones have been identified", "Location"])
            errorcnt = errorcnt + 1

    # Check for Ownership
    ownersadd = ownership_info.objects.values_list('Owner_Value', flat=True).filter(Project_ID=prjid)
    ownerscnt = 0
    for owneradd in ownersadd:
        ownerscnt = ownerscnt + 1
    if ownerscnt < 1:
        missingdata.append(
            ["OwnershipEr", "Location Information Error: Land Ownership has not been identified", "Location"])
        errorcnt = errorcnt + 1

    ### Implementation Information ###

    # Part 1 #
    Imp_Status = implementation_info.objects.values_list('Imp_Status', flat=True).get(pk=prjid)
    curactmech = Imp_Status
    if Imp_Status < 1:
        missingdata.append(
            ["StatusEr", "Basic Information Error: Implementation Status must be Planned, In Progress, or Implemented",
             "Implementation"])
        errorcnt = errorcnt + 1

    # Check Dates
    strtdate = implementation_info.objects.values_list('Start_Date', flat=True).get(pk=prjid)
    datestr = str(strtdate)

    if datestr == None or datestr == "" or datestr == "None":
        missingdata.append(
            ["StartDateEr", "Basic Information Part 1 Error: Question 2 requires a Start Date", "Implementation"])
        errorcnt = errorcnt + 1
    else:
        dsplit = datestr.split("-")
        cnt = 0
        for y in dsplit:
            if cnt == 0:
                year = int(y)
            if cnt == 1:
                month = int(y)
            if cnt == 2:
                day = int(y)
            cnt = cnt + 1
        try:
            datetime.datetime(year=year, month=month, day=day)
        except:
            missingdata.append(["StartDateEr", "Basic Information Part 1 Error: Question 2 requires a valid Start Date",
                                "Implementation"])
            errorcnt = errorcnt + 1

    try:
        inperp = implementation_info.objects.values_list('In_Perpetuity', flat=True).get(pk=prjid)
        if inperp == 1:
            inperpexists = 1
        else:
            inperpexists = 0

    except:
        inperpexists = 0

    if inperpexists == 0:
        fnshdate = implementation_info.objects.values_list('Finish_Date', flat=True).get(pk=prjid)
        datefnsh = str(fnshdate)
        if datefnsh == None or datefnsh == "" or datefnsh == "None":
            missingdata.append(["FinishDateEr",
                                "Basic Information Part 1 Error: Question 2 requires a Finish Date or In Perpetuity checked",
                                "Implementation"])
            errorcnt = errorcnt + 1
        else:
            dsplit = datestr.split("-")
            cnt = 0
            for y in dsplit:
                if cnt == 0:
                    year = int(y)
                if cnt == 1:
                    month = int(y)
                if cnt == 2:
                    day = int(y)
                cnt = cnt + 1
            try:
                datetime.datetime(year=year, month=month, day=day)
            except:
                missingdata.append(["FinishDateEr",
                                    "Basic Information Part 1 Error: Question 2 requires a valid Finish Date or In Perpetuity checked",
                                    "Implementation"])
                errorcnt = errorcnt + 1

        if datestr != None and datestr != "" and datestr != "None":
            if datefnsh != None and datefnsh != "" and datefnsh != "None":

                if strtdate > fnshdate:
                    missingdata.append(["FinishDateEr",
                                        "Basic Information Part 1 Error: Question 2 Finish Date cannot occur before Start Date",
                                        "Implementation"])
                    errorcnt = errorcnt + 1

    # Question 3
    impeffstat = implementation_info.objects.values_list('Effective_Determined', flat=True).get(pk=prjid)
    if impeffstat < 1:
        missingdata.append(
            ["Q3Er", "Basic Information Part 1 Error: Question 3 requires a Yes or No answer, N/A is not acceptable",
             "Implementation"])
        errorcnt = errorcnt + 1

    if impeffstat == 1:
        highlevel = implementation_info.objects.values_list('Effective_Explained', flat=True).get(pk=prjid)
        if highlevel > "":
            test = "tst"
        else:
            missingdata.append(["Q3aEr",
                                "Implementation Information Part 1 Error: Question 3a. requires a text answer answer if the answer to question 3 is 'Yes'",
                                "Implementation"])
            errorcnt = errorcnt + 1

    # Part 2 
    questions2 = ["Reas_Certain", "Legal_Authority", "Staff_Available"]

    qcnt = 1
    for quest in questions2:
        if qcnt == 1:
            qalpha = 'a'
        if qcnt == 2:
            qalpha = 'b'
        if qcnt == 3:
            qalpha = 'c'

        qvalue = implementation_info.objects.values_list(quest, flat=True).get(pk=prjid)

        if qvalue < 1:

            if curactmech == 3:
                Test = "Test"
            else:
                missingdata.append(["Q2" + str(qalpha) + "Er",
                                    "Implementation Information Part 2 Error: If Part 1 question 'Implementation and Effectiveness Status Confirmed?' is not 'Completed' all questions in Part 2 are required, 'N/A' is not an option for Question Part 2: " + str(
                                        qalpha), "Implementation"])

                errorcnt = errorcnt + 1

        qcnt = qcnt + 1

    # Part 3 
    questions3 = ["Reduce_Threats", "Incremental_Objectives", "Quantifiable_Measures", "AD_Strategy"]

    qcnt = 1
    for quest in questions3:
        if qcnt == 1:
            qalpha = 'a'
        if qcnt == 2:
            qalpha = 'b'
        if qcnt == 3:
            qalpha = 'c'
        if qcnt == 4:
            qalpha = 'd'
        qvalue = implementation_info.objects.values_list(quest, flat=True).get(pk=prjid)

        if qvalue < 1:
            if impeffstat == 1:
                Test = "Test"
            else:
                missingdata.append(["Q3" + str(qalpha) + "Er",
                                    "Implementation Information Part 3 Error: If Part 1 question 'Implementation and Effectiveness Status Confirmed?' is 'No' all questions in Part 3 are required, 'N/A' is not an option for Question Part 3: " + str(
                                        qalpha), "Implementation"])
                errorcnt = errorcnt + 1
        qcnt = qcnt + 1

    # Check for Collaborating Parties
    ColPasadd = collab_party.objects.values_list('Collab_Party', flat=True).filter(Project_ID=prjid)
    ColPascnt = 0
    for ColPaadd in ColPasadd:
        ColPascnt = ColPascnt + 1
    if ColPascnt < 1:
        missingdata.append(["CollabEr",
                            "Contact Information Error: Collaborating Parties have not been identified, select 'None' if there were no collaborating parties",
                            "Contacts"])
        errorcnt = errorcnt + 1

    errorcount = [errorcnt]

    return errorcount, missingdata


def ClipFeates(feature, prid, username):

    Folder = os.path.join(STATIC_DIR, 'ced_main/GIS_Processing')
    # OutGeo = Folder + "/JsonConversion.gdb"
    # BackGeo = Folder + "/CED_GeoProc.gdb"

    # states = []
    # counties = []
    # wafwas = []
    # hucs = []
    # pops = []

    # # arcpy.env.workspace = OutGeo

    # BackClipFeat = []
    # BackClipFeat.append(
    #     (BackGeo + "/COT_SG_Populations_2013", "poplayer" + str(prid), "pop" + str(prid) + ".dbf", 0, 0))
    # BackClipFeat.append((BackGeo + "/sage_mgmt_zones", "wafwalayer" + str(prid), "waf" + str(prid) + ".dbf", 2, 0))
    # BackClipFeat.append(
    #     (BackGeo + "/tl_2012_us_county_clipped", "countylayer" + str(prid), "con" + str(prid) + ".dbf", 4, 19))
    # BackClipFeat.append(
    #     (BackGeo + "/tl_2012_us_state_clipped", "statelayer" + str(prid), "sta" + str(prid) + ".dbf", 5, 0))

    # for backfeat, layer, table, i, j in BackClipFeat:
    #     try:
    #         arcpy.Delete_management(layer)
    #     except:
    #         print("Nothing to delete")

    #     try:
    #         arcpy.Delete_management(Folder + "/" + table)
    #     except:
    #         print("Nothing to delete")

    # try:
    #     arcpy.Delete_management("feature_lyr")
    # except:
    #     print("Nothing to delete")


    # ### Calculate the acres correctly
    # poppi = project_info.objects.get(pk=prid)
    # out_coordinate_system = arcpy.SpatialReference('USA Contiguous Albers Equal Area Conic USGS')
    # outfeat = Folder + "/JsonConversion.gdb/Acres_" + str(prid) + "_Calc"
    # try:
    #     arcpy.Delete_management(outfeat)
    # except:
    #     print("Nothing to delete")
    # arcpy.Project_management(feature, outfeat, out_coordinate_system)

    # arcpy.MakeTableView_management(outfeat, "feature_lyr")
    # try:
    #     arcpy.DeleteField_management("feature_lyr", ["CED_Acres"])
    # except:
    #     a = 1
    # arcpy.AddField_management("feature_lyr", "CED_Acres", "DOUBLE", "", "", "", "CED_Acres", "NULLABLE",
    #                           "NON_REQUIRED")
    # arcpy.CalculateField_management("feature_lyr", "CED_Acres", "!shape.area@acres!", "PYTHON", "")

    # try:
    #     arcpy.Delete_management("feature_lyr")
    # except:
    #     print("Nothing to delete")

    

    # arcpy.MakeTableView_management(outfeat, "feature_lyr")

    # GISAc = 0
    # fields = ["CED_Acres"]
    # with arcpy.da.SearchCursor("feature_lyr", fields) as cursor:
    #     for row in cursor:
    #         GISAc = GISAc + row[0]
    # try:
    #     arcpy.Delete_management("feature_lyr")
    # except:
    #     print("Nothing to delete")

    # try:
    #     arcpy.Delete_management(outfeat)
    # except:
    #     print("Nothing to delete")

    # GISAc = round(GISAc, 1)
    # poppi.GIS_Acres = abs(GISAc)
    # poppi.save()

    # # Attach the attributes
    # # try:
    # # Loop through the background GIS table and clip all background GIS to the feature perimeters
    # for backfeat, layer, table, i, j in BackClipFeat:
    #     # Execute clips of each layer, converting features to polygons if applicable
    #     featcnt = 1
    #     arcpy.MakeFeatureLayer_management(backfeat, layer)
        
    #     try:
    #         for feat in feature:

    #             if featcnt < 4:
    #                 if featcnt == 1:
    #                     poppi.LC_Center_X = float(str(feat))
    #                 if featcnt == 2:
    #                     poppi.LC_Center_Y = float(str(feat))
    #                 if featcnt == 3:
    #                     poppi.LC_Zoom = int(str(feat))

    #             else:
    #                 arcpy.MakeFeatureLayer_management(feat, "feature_lyr")
    #                 if featcnt == 4:
    #                     arcpy.SelectLayerByLocation_management(layer, 'intersect', "feature_lyr")
    #                 else:
    #                     arcpy.SelectLayerByLocation_management(layer, 'intersect', "feature_lyr", "#",
    #                                                            "ADD_TO_SELECTION")

    #                 try:
    #                     arcpy.Delete_management("feature_lyr")
    #                 except:
    #                     print("Nothing to delete")

    #             featcnt = featcnt + 1
    #     except:
    #         arcpy.MakeFeatureLayer_management(feature, "feature_lyr")
    #         arcpy.SelectLayerByLocation_management(layer, 'intersect', "feature_lyr")
    #         try:
    #             arcpy.Delete_management("feature_lyr")
    #         except:
    #             print("Nothing to delete")

        
    #     matchcount = int(arcpy.GetCount_management(layer).getOutput(0))
    #     if matchcount == 0:
    #         print('no features matched spatial and attribute criteria')
    #     else:
    #         arcpy.TableToTable_conversion(layer, Folder, table)

    #         opentable = dbf.Table(Folder + "/" + table)
    #         opentable.open()

    #         for row in opentable:
    #             if table == "pop" + str(prid) + ".dbf":
    #                 pops.append(str(row[i]))
    #             elif table == "huc" + str(prid) + ".dbf":
    #                 hucs.append(str(row[i]))
    #             elif table == "waf" + str(prid) + ".dbf":
    #                 wafwas.append(str(row[i]))
    #             elif table == "con" + str(prid) + ".dbf":
    #                 cntyst = str(row[i]).strip() + ", " + str(row[j]).strip()
    #                 counties.append(cntyst)
    #             elif table == "sta" + str(prid) + ".dbf":
    #                 states.append(str(row[i]))

    #         opentable.close()

    # pid = project_info.objects.get(pk=prid)

    # pcnt = 0
    # try:
    #     pidpop = population_info.objects.values_list('id', flat=True).get(Project_ID=prid)
    #     idpop = population_info.objects.values_list('Population_Value', flat=True).filter(Project_ID=prid)
    #     for idp in idpop:
    #         population_info.objects.filter(Project_ID=prid, Population_Value=idp).delete()
    #     pidpop = population_info.objects.values_list('id', flat=True).get(Project_ID=prid)

    # except:
    #     popc = population_info()
    #     popc.Project_ID = pid
    #     popc.Date_Entered = now
    #     popc.User = str(username)
    #     popc.save()

    #     pidpop = population_info.objects.values_list('id', flat=True).get(Project_ID=prid)

    # popids = []
    # for p in pops:
    #     # print(p)
    #     popids.append(population_values.objects.values_list('id', flat=True).get(Pop_Name=p))

    # popm = population_info.objects.get(pk=pidpop)
    # popm.Project_ID = pid
    # popm.Date_Entered = now
    # popm.Population_Value.set(popids)
    # popm.User = str(username)
    # popm.save()

    # # try:
    # #     pidhuc = huc12_info.objects.values_list('id', flat=True).get(Project_ID=prid)
    # #     idhuc = huc12_info.objects.values_list('HUC12_Value', flat=True).filter(Project_ID=prid)
    # #     for idh in idhuc:
    # #         huc12_info.objects.filter(Project_ID=prid, HUC12_Value=idh).delete()
    # #     pidhuc = huc12_info.objects.values_list('id', flat=True).get(Project_ID=prid)
    # # except:
    # #     hucc = huc12_info()
    # #     hucc.Project_ID = pid
    # #     hucc.Date_Entered = now
    # #     hucc.User = str(username)
    # #     hucc.save()
    # #     pidhuc = huc12_info.objects.values_list('id', flat=True).get(Project_ID=prid)
    # # hucids = []
    # # for h in hucs:
    # #     huc12vals = state_county_huc12_values.objects.values_list('id', flat=True).filter(HUC12=str(h))
    # #     for huc12vas in huc12vals:
    # #         hucids.append(huc12vas)
    # # hucm = huc12_info.objects.get(pk=pidhuc)
    # # hucm.Project_ID = pid
    # # hucm.Date_Entered = now
    # # hucm.HUC12_Value.set(hucids)
    # # hucm.User = str(username)
    # # hucm.save()

    # try:
    #     pidwaf = wafwa_info.objects.values_list('id', flat=True).get(Project_ID=prid)
    #     idwaf = wafwa_info.objects.values_list('WAFWA_Value', flat=True).filter(Project_ID=prid)
    #     for idw in idwaf:
    #         wafwa_info.objects.filter(Project_ID=prid, WAFWA_Value=idw).delete()
    #     pidwaf = wafwa_info.objects.values_list('id', flat=True).get(Project_ID=prid)
    # except:
    #     wafc = wafwa_info()
    #     wafc.Project_ID = pid
    #     wafc.Date_Entered = now
    #     wafc.User = str(username)
    #     wafc.save()
    #     pidwaf = wafwa_info.objects.values_list('id', flat=True).get(Project_ID=prid)
    # wafids = []
    # for w in wafwas:
    #     wafids.append(wafwa_zone_values.objects.values_list('id', flat=True).get(id=w))
    # wafm = wafwa_info.objects.get(pk=pidwaf)
    # wafm.Project_ID = pid
    # wafm.Date_Entered = now
    # wafm.WAFWA_Value.set(wafids)
    # wafm.User = str(username)
    # wafm.save()

    # try:
    #     pidcnty = county_info.objects.values_list('id', flat=True).get(Project_ID=prid)
    #     idcnty = county_info.objects.values_list('County_Value', flat=True).filter(Project_ID=prid)
    #     for idc in idcnty:
    #         county_info.objects.filter(Project_ID=prid, County_Value=idc).delete()
    #     pidcnty = county_info.objects.values_list('id', flat=True).get(Project_ID=prid)
    # except:
    #     cntyc = county_info()
    #     cntyc.Project_ID = pid
    #     cntyc.Date_Entered = now
    #     cntyc.User = str(username)
    #     cntyc.save()
    #     pidcnty = county_info.objects.values_list('id', flat=True).get(Project_ID=prid)
    # cntyids = []
    # for c in counties:
    #     cntyids.append(state_county.objects.values_list('id', flat=True).get(Cnty_St=c))
    # cntym = county_info.objects.get(pk=pidcnty)
    # cntym.Project_ID = pid
    # cntym.Date_Entered = now
    # cntym.County_Value.set(cntyids)
    # cntym.User = str(username)
    # cntym.save()

    # try:
    #     pidstt = state_info.objects.values_list('id', flat=True).get(Project_ID=prid)
    #     idstt = state_info.objects.values_list('State_Value', flat=True).filter(Project_ID=prid)
    #     for ids in idstt:
    #         state_info.objects.filter(Project_ID=prid, State_Value=ids).delete()
    #     pidstt = state_info.objects.values_list('id', flat=True).get(Project_ID=prid)
    # except:
    #     sttc = state_info()
    #     sttc.Project_ID = pid
    #     sttc.Date_Entered = now
    #     sttc.User = str(username)
    #     sttc.save()
    #     pidstt = state_info.objects.values_list('id', flat=True).get(Project_ID=prid)
    # sttids = []
    # for s in states:
    #     sttids.append(state.objects.values_list('id', flat=True).get(State=s))
    # sttm = state_info.objects.get(pk=pidstt)
    # sttm.Project_ID = pid
    # sttm.Date_Entered = now
    # sttm.State_Value.set(sttids)
    # sttm.User = str(username)
    # sttm.save()

    # try:
    #     arcpy.Delete_management("feature_lyr")
    # except:
    #     print("Nothing to delete")

    # try:
    #     arcpy.Delete_management(feature)
    # except:
    #     print("Nothing to delete")

    # for backfeat, layer, table, i, j in BackClipFeat:
    #     try:
    #         arcpy.Delete_management(layer)
    #     except:
    #         print("Nothing to delete")

    #     try:
    #         arcpy.Delete_management(Folder + "/" + table)
    #     except:
    #         print("Nothing to delete")
    # print("Features Clipped")
    return "Done"


def create_sgce_folder(dest):
    sb = pysb.SbSession()
    sb.login(sbuser, sbpass)
    ItemID = '53285f1de4b05e6fc331e8fa'
    newItem = {'title': str(dest),
               'parentId': ItemID,
               'provenance': {'annotation': str(dest)}}  # This text will go in the 'From' SB metadata tab.
    newItem = sb.create_item(newItem)
    item = str(newItem)
    item1 = item.split("https://www.sciencebase.gov/catalog/itemLinks?itemId=")
    item2 = item1[1]
    itemfinal = item2[0:24]
    return itemfinal


def create_spatial_folder(dest, PrJName):
    sb = pysb.SbSession()
    sb.login(sbuser, sbpass)
    ItemID = dest  # '53285f1de4b05e6fc331e8fa'
    newItem = {'title': str(PrJName),
               'parentId': ItemID,
               'provenance': {'annotation': str(PrJName)}}  # This text will go in the 'From' SB metadata tab.
    newItem = sb.create_item(newItem)

    item = str(newItem)
    item1 = item.split("https://www.sciencebase.gov/catalog/itemLinks?itemId=")
    item2 = item1[1]
    itemfinal = item2[0:24]
    return itemfinal


def create_spatial_foldermultifile(dest, shapefilelist):
    sb = pysb.SbSession()
    sb.login(sbuser, sbpass)
    ItemID = dest

    newItem = sb.uploadFilesAndCreateItem(ItemID, shapefilelist)

    item = str(newItem)
    item1 = item.split("https://www.sciencebase.gov/catalog/itemLinks?itemId=")
    item2 = item1[1]
    itemfinal = item2[0:24]
    return itemfinal


def handle_uploaded_file_sgce(f, dest):
    sb = pysb.SbSession()
    sb.login(sbuser, sbpass)
    ItemID = dest
    newItem = {'title': str(f),
               'parentId': dest,
               'provenance': {'annotation': str(f)}}
    newItem = sb.create_item(newItem)

    time.sleep(0.25)

    item = str(newItem)
    item1 = item.split("https://www.sciencebase.gov/catalog/itemLinks?itemId=")
    item2 = item1[1]

    itemfinal = item2[0:24]

    uploadfile = sb.upload_file_to_item(newItem, f)

    if uploadfile == "Upload Failed":
        itemfinal = "Upload Failed"
    else:
        itemfinal = itemfinal
    return itemfinal


def handle_uploaded_file_sgce_batch(f, dest, title):
    sb = pysb.SbSession()
    sb.login(sbuser, sbpass)
    ItemID = dest
    newItem = {'title': str(title),
               'parentId': dest,
               'provenance': {'annotation': str(f)}}
    newItem = sb.create_item(newItem)

    time.sleep(0.25)

    item = str(newItem)
    item1 = item.split("https://www.sciencebase.gov/catalog/itemLinks?itemId=")
    item2 = item1[1]

    itemfinal = item2[0:24]

    uploadfile = sb.upload_file_to_item(newItem, f)

    if uploadfile == "Upload Failed":
        itemfinal = "Upload Failed"
    else:
        itemfinal = itemfinal
    return itemfinal


def handle_uploaded_file_sgce_full_file(f, dest):
    sb = pysb.SbSession()
    sb.login(sbuser, sbpass)
    ItemID = '53285f1de4b05e6fc331e8fa'
    newItem = {'title': str(f),
               'parentId': '53285f1de4b05e6fc331e8fa',
               'provenance': {'annotation': str(f)}}
    newItem = sb.create_item(newItem)
    time.sleep(0.25)

    item = str(newItem)
    item1 = item.split("https://www.sciencebase.gov/catalog/itemLinks?itemId=")
    item2 = item1[1]
    itemfinal = item2[0:24]
    uploadfile = sb.upload_file_to_item1(newItem, f)

    if uploadfile == "Upload Failed":
        itemfinal = "Upload Failed"
    else:
        itemfinal = itemfinal
    return itemfinal


def handle_uploaded_file_sgce1(f, title, dest):
    sb = pysb.SbSession()
    sb.login(sbuser, sbpass)
    ItemID = dest  # '53285f1de4b05e6fc331e8fa'
    newItem = {'title': str(title),
               'parentId': ItemID,
               'provenance': {'annotation': str(title)}}  # This text will go in the 'From' SB metadata tab.
    newItem = sb.create_item(newItem)
    time.sleep(0.25)
    item = str(newItem)
    item1 = item.split("https://www.sciencebase.gov/catalog/itemLinks?itemId=")
    item2 = item1[1]
    itemfinal = item2[0:24]
    sb.upload_file_to_item1(newItem, f)
    return itemfinal


def handle_uploaded_file_sgce2(f, title, dest):
    sb = pysb.SbSession()
    sb.login(sbuser, sbpass)
    ItemID = dest  # '53285f1de4b05e6fc331e8fa'

    ItemJson = sb.getSbItem(ItemID)
    sb.upload_file_to_item1(ItemJson, f)
    return "Succsss"


def downloadallfromLCMap(docid, fname):
    sb = pysb.SbSession()
    sb.login(sbuser, sbpass)
    lcval = project_info.objects.values_list('LCMItem', flat=True).get(Project_ID=docid)
    filepath = "https://www.sciencebase.gov/catalog/file/get/" + lcval + "?children=y"
    saveFile = fname + '.zip'
    sb.download(filepath, saveFile)


def downloadfromLCMap(docid, fname):
    sb = pysb.SbSession()
    sb.login(sbuser, sbpass)
    lcval = documentation.objects.values_list('LCMItem', flat=True).get(id=docid)
    filepath = "https://www.sciencebase.gov/catalog/file/get/" + lcval
    saveFile = fname + '.zip'
    sb.download(filepath, saveFile)


def deletefromLCMap(docid):
    sb = pysb.SbSession()
    sbItemID = []
    sb.login(sbuser, sbpass)
    sbItemID.append(docid)
    #######TODO#####
    delete_items1(sbItemID, 1, False)


def testsb():
    testcon = 'https://www.sciencebase.gov/catalog/item/54ada05de4b00453c5ab7a0f'  # c
    testsb = Login2SBandOpenFootprintStudio(testcon)

    if testsb == 'NoConnection':
        return 'True'
    else:
        return 'False'


def checkenter(appoff):
    try:
        for app in appoff:
            if app == 'Data Entry' or app == 'Bulk Uploaders' or app == 'Approving Officials' or app == 'Administrators':
                if app == 'Data Entry':
                    return 'dataenter'
    except:
        return 'none'
    return 'none'


def checkaccept(appoff):
    try:
        if appoff == 1:
            return 'accepted'
    except:
        return 'none'
    return 'none'


@login_required
def index(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    profile = request.user.username
    sbdown1 = testsb()
    loginfailed = 'loginfailed'
    context_instance = RequestContext(request)
    table = viewprojects_table(
        project_info.objects.filter(Created_By__exact=profile))  # viewallprojects_table(project_info.objects.all())
    RequestConfig(request, paginate={'per_page': 5}).configure(table)

    try:
        icanedit = useredits.objects.values_list('userid', flat=True).filter(
            editinguser=elidgbleusers.objects.get(username=profile))
        ican1 = []
        icnt = 0
        for ican in icanedit:
            username = User.objects.get(id=ican)
            prjscrt = project_info.objects.filter(Created_By__exact=username)
            for prjs in prjscrt:
                ican1.append(str(prjs))
                icnt = icnt + 1
    except:
        ican1 = ""

    table1 = viewprojects_table(
        list(project_info.objects.filter(Project_ID__in=ican1)))  # viewallprojects_table(project_info.objects.all())
    RequestConfig(request, paginate={'per_page': 5}).configure(table1)

    if request.method == 'POST':

        if cont[0] == 'good':
            authen = checkgroup(request.user.groups.values_list('name', flat=True))
            profile = request.user.username
            table = viewprojects_table(project_info.objects.filter(Created_By__exact=profile))
            RequestConfig(request, paginate={'per_page': 5}).configure(table)
            sbdown1 = testsb()
            context = {'authen': authen, 'sbdown1': sbdown1, 'table': table, 'table1': table1}
            return render(request, 'ced_main/index.html', context)
        elif cont[0] == 'redirect':
            return redirect('/sgce/accounts/profile/')
        elif cont[0] == 'weak':
            return redirect('/sgce/accounts/password_change/')

        else:
            authen = checkgroup(request.user.groups.values_list('name', flat=True))
            context = {'authen': 'None', 'loginfailed': cont[0], 'remaining': cont[1]}

            return render(request, 'ced_main/index.html', context)

    else:
        authen = checkgroup(request.user.groups.values_list('name', flat=True))
        context = {'authen': authen, 'sbdown1': sbdown1, 'table': table, 'table1': table1}
        # if request.user.is_authenticated(): Pythoon 2.7
        if request.user.is_authenticated:
            return render(request, 'ced_main/index.html', context)
        else:
            return render(request, 'ced_main/index.html', context)


def registration(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'accounts/register.html', context)
    else:
        return render(request, 'accounts/register.html')


def sbunavailable(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/sbunavailable.html', context)
    else:
        return render(request, 'ced_main/sbunavailable.html')


def none_to_edit(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/none_to_edit.html', context)
    else:
        return render(request, 'ced_main/none_to_edit.html')


def bug_reports(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/bug_reports.html', context)
    else:
        return render(request, 'ced_main/bug_reports.html')


def sgerd(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/sgerd.html', context)
    else:
        return render(request, 'ced_main/sgerd.html')


@xframe_options_sameorigin
def usermenu(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    try:
        userAgency = userprofile.objects.values_list('Agency', flat=True).get(User_id=profile)
    except:
        userAgency = 'NA'
    tablequerydata = project_query.objects.filter(User=str(request.user.username))
    showq = 'None'
    for qr in tablequerydata:
        showq = 'Show'
    try:
        table = viewprojectname_table(tablequerydata)
        RequestConfig(request).configure(table)
    except:
        table = "None"

    if request.method == 'POST':
        if 'clearresult' in request.POST:
            deleteprj = project_query.objects.filter(User=request.user.username).delete()
        context = {'authen': authen, 'userAgency': userAgency, 'queryresults': table, 'showq': 'NoShow'}
        # if request.user.is_authenticated(): Pythoon 2.7
        if request.user.is_authenticated:
            return render(request, 'ced_main/usermenu.html', context)
        else:
            return render(request, 'ced_main/usermenu.html')
    else:
        # if request.user.is_authenticated(): Pythoon 2.7
        if request.user.is_authenticated:
            context = {'authen': authen, 'userAgency': userAgency, 'queryresults': table, 'showq': 'NoShow'}
            return render(request, 'ced_main/usermenu.html', context)
        else:
            return render(request, 'ced_main/usermenu.html')


@login_required
def sgeditmenu(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    sbdown1 = testsb()
    loginfailed = 'loginfailed'

    if request.method == 'POST':
        test = 1
    else:
        authen = checkgroup(request.user.groups.values_list('name', flat=True))
        context = {'authen': authen, 'sbdown1': sbdown1, 'showlogin': 'True'}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/sgeditmenu.html', context)
    else:
        return render(request, 'ced_main/sgeditmenu.html', context)


@login_required
def sgappmenu(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen, 'showlogin': 'True'}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/sgappmenu.html', context)
    else:
        return render(request, 'ced_main/sgappmenu.html')


@login_required
def sgadminmenu(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen, 'showlogin': 'True'}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/sgadminmenu.html', context)
    else:
        return render(request, 'ced_main/sgadminmenu.html', context)


def error_check_projects(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    conoffice = userprofile.objects.values_list('Field_Office', flat=True).get(
        User_id__exact=User.objects.values_list('id', flat=True).get(username__exact=request.user))
    context = {'authen': authen}
    if request.method == 'POST':
        if conoffice == 'Congress':
            return redirect('/sgce/readonly/')

        FN = request.user.first_name
        LN = request.user.last_name
        uem = request.user.email
        un = request.user.username
        if 'cefamp' in request.POST:
            prjids = project_info.objects.values_list('Project_ID', flat=True).filter(Created_By=request.user.username)
            prjlist = []
            for prjid in prjids:
                prjlist.append(int(prjid))

            checkprj = checkallprojects(prjlist, str(un), str(uem), FN, LN)
            return render(request, 'ced_main/error_check_projects_successful.html', context)
        if 'cefpic' in request.POST:
            prjids = project_info.objects.values_list('Project_ID', flat=True).filter(Created_By=request.user.username)
            prjlist = []
            for prjid in prjids:
                prjlist.append(int(prjid))
            checkprj = checkallprojects(prjlist, str(un), str(uem), FN, LN)
            return render(request, 'ced_main/error_check_projects_successful.html', context)
        if 'cefpim' in request.POST:
            prjids = project_info.objects.values_list('Project_ID', flat=True).filter(
                Updating_User=request.user.username)
            prjlist = []
            for prjid in prjids:
                prjlist.append(int(prjid))
            checkprj = checkallprojects(prjlist, str(un), str(uem), FN, LN)
            return render(request, 'ced_main/error_check_projects_successful.html', context)
        if 'cefmdp' in request.POST:
            prjids = project_info.objects.values_list('Project_ID', flat=True).filter(
                Updating_User=request.user.username, Entry_Type=1)
            prjlist = []
            for prjid in prjids:
                prjlist.append(int(prjid))
            checkprj = checkallprojects(prjlist, str(un), str(uem), FN, LN)
            return render(request, 'ced_main/error_check_projects_successful.html', context)
        if 'ceonmpaa' in request.POST:
            prjids = project_info.objects.values_list('Project_ID', flat=True).filter(
                Updating_User=request.user.username, Entry_Type=2)
            prjlist = []
            for prjid in prjids:
                prjlist.append(int(prjid))
            checkprj = checkallprojects(prjlist, str(un), str(uem), FN, LN)
            return render(request, 'ced_main/error_check_projects_successful.html', context)

        if 'ceoapia' in request.POST:
            prjids = project_info.objects.values_list('Project_ID', flat=True).filter(
                Approving_Official=request.user.username)
            prjlist = []
            for prjid in prjids:
                prjlist.append(int(prjid))
            checkprj = checkallprojects(prjlist, str(un), str(uem), FN, LN)
            return render(request, 'ced_main/error_check_projects_successful.html', context)
        if 'ceopama' in request.POST:
            prjids = project_info.objects.values_list('Project_ID', flat=True).filter(
                Approving_Official=request.user.username, Entry_Type=2)
            prjlist = []
            for prjid in prjids:
                prjlist.append(int(prjid))
            checkprj = checkallprojects(prjlist, str(un), str(uem), FN, LN)
            return render(request, 'ced_main/error_check_projects_successful.html', context)
        if 'ceoapitd' in request.POST:
            prjids = project_info.objects.values_list('Project_ID', flat=True).all()
            prjlist = []
            for prjid in prjids:
                prjlist.append(int(prjid))
            checkprj = checkallprojects(prjlist, str(un), str(uem), FN, LN)
            return render(request, 'ced_main/error_check_projects_successful.html', context)

    else:
        # if request.user.is_authenticated(): Pythoon 2.7
        if request.user.is_authenticated:
            return render(request, 'ced_main/error_check_projects.html', context)
        else:
            return render(request, 'ced_main/permission_denied.html')


def error_check_projects_successful(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/error_check_projects_successful.html', context)
    else:
        return render(request, 'ced_main/permission_denied.html')


def menu(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/menu.html', context)
    else:
        return render(request, 'ced_main/menu.html')


@login_required
def batch_upload(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen, 'showlogin': 'True'}
    if request.method == 'POST':
        fn = request.POST.get("batchname", "")
        for afile in request.FILES.getlist('myfile'):
            dest = '58c05eeee4b014cc3a3bf428'
            lcitem = handle_uploaded_file_sgce_batch(afile, dest, fn)
            if lcitem == "Upload Failed":
                DocFailed = "DocFailed"
            else:
                obj = batchupload()
                obj.FolderName = str(fn)
                obj.FileName = str(afile)
                obj.LCMItem = str(lcitem)
                obj.UploadStatus = "Zip File Uploaded"
                obj.Date_Entered = now
                obj.Uploading_User = request.user.username
                obj.save()

        return redirect('/sgce/batch_upload_initial_success/')
    else:
        # if request.user.is_authenticated(): Pythoon 2.7
        if request.user.is_authenticated:
            return render(request, 'ced_main/batch_upload.html', context)
        else:
            return render(request, 'ced_main/permission_denied.html')


@login_required
def batch_upload_available(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen, 'showlogin': 'True'}
    spatialproject = ""
    nonspatialproject = ""
    nonspatialplan = ""
    spatialcnt = 0
    nonspatialcnt = 0
    plancnt = 0

    typelist = ['Spatial Project', 'Non-Spatial Project', 'Non-Spatial Plan']

    SpatialFS = ""
    NonSpatialFS = ""
    PlanFormSet = ""

    spatialcnt = batchupload_groups.objects.filter(Uploading_User=str(request.user.username)).filter(
        Type_Act="Spatial Project").count()
    if spatialcnt > 0:
        spatialproject = "spatialproject"
        SpatialFormSet = modelformset_factory(batchupload_groups, extra=0, form=batch_data_available_Form)
        SpatialFS = SpatialFormSet(
            queryset=batchupload_groups.objects.filter(Uploading_User=str(request.user.username)).filter(
                Type_Act="Spatial Project"))

    nonspatialcnt = batchupload_groups.objects.filter(Uploading_User=str(request.user.username)).filter(
        Type_Act="Non-Spatial Project").count()
    if nonspatialcnt > 0:
        nonspatialproject = "nonspatialproject"
        NonSpatialFormSet = modelformset_factory(batchupload_groups, extra=0, form=batch_data_available_Form)
        NonSpatialFS = NonSpatialFormSet(
            queryset=batchupload_groups.objects.filter(Uploading_User=str(request.user.username)).filter(
                Type_Act="Non-Spatial Project"))

    plancnt = batchupload_groups.objects.filter(Uploading_User=str(request.user.username)).filter(
        Type_Act="Non-Spatial Plan").count()
    if plancnt > 0:
        nonspatialplan = "nonspatialplan"
        PlanFormSet = modelformset_factory(batchupload_groups, extra=0, form=batch_data_available_Form)
        PlanFS = PlanFormSet(
            queryset=batchupload_groups.objects.filter(Uploading_User=str(request.user.username)).filter(
                Type_Act="Non-Spatial Plan"))

    maxids = batchupload_groups.objects.values_list('Batch_Group_ID', flat=True).aggregate(Max('Batch_Group_ID'))
    maxids = str(maxids)
    maxid = maxids.split(": ")
    maxid = maxid[1]
    maxid = maxid.replace("}", "")
    maxid = int(maxid) + 1

    if request.method == 'POST':
        for i in range(maxid):
            goto = "GoToSpatial_" + str(i)
            if goto in request.POST:
                return redirect('/sgce/' + str(i) + '/batch_upload_s1_spatial/')

        for i in range(maxid):
            goto = "GoToNonSpatial_" + str(i)
            if goto in request.POST:
                return render(request, 'ced_main/permission_denied.html')

        for i in range(maxid):
            goto = "GoToPlan_" + str(i)
            if goto in request.POST:
                return render(request, 'ced_main/permission_denied.html')

        context = {'authen': authen, 'spatialproject': spatialproject, 'nonspatialproject': nonspatialproject,
                   'nonspatialplan': nonspatialplan, 'spatialcnt': spatialcnt, 'nonspatialcnt': nonspatialcnt,
                   'plancnt': plancnt, 'SpatialFS': SpatialFS, 'NonSpatialFS': NonSpatialFS, 'PlanFS': PlanFS}

        return render(request, 'ced_main/batch_upload_available.html', context)
    else:
        # if request.user.is_authenticated(): Pythoon 2.7
        if request.user.is_authenticated:
            context = {'authen': authen, 'spatialproject': spatialproject, 'nonspatialproject': nonspatialproject,
                       'nonspatialplan': nonspatialplan, 'spatialcnt': spatialcnt, 'nonspatialcnt': nonspatialcnt,
                       'plancnt': plancnt, 'SpatialFS': SpatialFS, 'NonSpatialFS': NonSpatialFS, 'PlanFS': PlanFS}
            return render(request, 'ced_main/batch_upload_available.html', context)
        else:
            return render(request, 'ced_main/permission_denied.html')


@login_required
def batch_upload_types(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    if request.method == 'POST':
        return redirect('/sgce/batch_upload_initial_success/')
    else:

        batchspatial = project_info.objects.filter(Batch_Upload=1).filter(Created_By=str(request.user.username))
        # if request.user.is_authenticated(): Pythoon 2.7
        if request.user.is_authenticated:
            context = {'authen': authen, 'queryresults': table}
            return render(request, 'ced_main/batch_upload_available.html', context)
        else:
            return render(request, 'ced_main/permission_denied.html')


@login_required
def batch_upload_initial_success(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen, 'showlogin': 'True'}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/batch_upload_initial_success.html', context)
    else:
        return render(request, 'ced_main/permission_denied.html')


def readonly(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/readonly.html', context)
    else:
        return render(request, 'ced_main/readonly.html')


def batch_upload_template(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/batch_upload_template.html', context)
    else:
        return render(request, 'ced_main/batch_upload_template.html')


def under_construction(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/under_construction.html', context)
    else:
        return render(request, 'ced_main/under_construction.html')


@login_required
def newprjsuccess(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/new_project_success.html', context)
    else:
        return render(request, 'ced_main/permission_denied.html')


@login_required
def editprjsuccess(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/edit_project_success.html', context)
    else:
        return render(request, 'ced_main/permission_denied.html')


@login_required
def project_approval_success(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/project_approval_success.html', context)
    else:
        return render(request, 'ced_main/permission_denied.html')


@login_required
def project_approved(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/project_approved.html', context)
    else:
        return render(request, 'ced_main/permission_denied.html')


@login_required
def dataentry_new(request):
    siteurl = request.build_absolute_uri()
    siteurl1 = siteurl.split("/")
    siteurl2 = siteurl1[0] + "//" + siteurl1[2]

    # Get the context from the request.
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    enterdata = checkenter(request.user.groups.values_list('name', flat=True))
    accepted = checkaccept(userprofile.objects.values_list('Waiver_V2_Approved', flat=True).get(
        User_id__exact=User.objects.values_list('id', flat=True).get(username__exact=request.user)))
    conoffice = userprofile.objects.values_list('Field_Office', flat=True).get(
        User_id__exact=User.objects.values_list('id', flat=True).get(username__exact=request.user))

    if request.method == 'POST':
        if conoffice == 'Congress':
            return redirect('/sgce/readonly/')
        form = newprj_Form(request.POST, request.FILES)
        context = {'form': form, 'authen': authen, 'showlogin': 'True'}
        # Have we been provided with a valid form?
        if form.is_valid():

            actval = form.cleaned_data['Activity']
            subactval = str(form.cleaned_data['SubActivity'])

            typeactval = subactivity.objects.values_list('TypeAct', flat=True).get(SubActivity=subactval)
            # Save the new category to the database.
            obj = form.save(commit=False)
            impstat = obj.Project_Status
            obj.Entry_Type = 1
            obj.TypeAct = typeactval
            if subactval == 'Fire Breaks' or subactval == 'Powerline Burial' or subactval == 'Fence Marking' or subactval == 'Fence Removal' or subactval == 'Road and Trail closure':
                obj.Metric = "Miles"
            elif typeactval == "Spatial Project" or subactval == "Improved Grazing Practices (Rest, Rotation, Etc.)":
                obj.Metric = "Acres"
            else:
                obj.Metric = ""
            obj.Approving_Official = userprofile.objects.values_list('Approving_Official', flat=True).get(
                User_id__exact=User.objects.values_list('id', flat=True).get(username__exact=request.user))
            obj.Implementing_Party = userprofile.objects.values_list('Agency', flat=True).get(
                User_id__exact=User.objects.values_list('id', flat=True).get(username__exact=request.user))
            obj.Office = userprofile.objects.values_list('Field_Office', flat=True).get(
                User_id__exact=User.objects.values_list('id', flat=True).get(username__exact=request.user))
            obj.User_Email = User.objects.values_list('email', flat=True).get(username__exact=request.user)
            obj.User_Phone_Number = userprofile.objects.values_list('User_Phone_Number', flat=True).get(
                User_id__exact=User.objects.values_list('id', flat=True).get(username__exact=request.user))

            obj.Last_Updated = datetime.datetime.now()
            obj.Updating_User = request.user.username
            obj.Created_By = request.user.username

            obj.save()

            try:
                obj = form.save(commit=False)
                prjid = str(obj.Project_ID)
                obj.Prj_ID = prjid

                itemID = create_sgce_folder(str(obj.Project_ID))
                spatialdest = itemID
                obj.LCMItem = itemID
                obj.save()

                if typeactval == "Spatial Project":
                    obj = form.save(commit=False)
                    spatiltitle = str(obj.Project_Name) + "_Spatial_Data"
                    itemID = create_spatial_folder(spatialdest, spatiltitle)
                    obj.Shapefile = itemID
                    spatialid = itemID
                    obj.save()
            except:
                context = {'authen': authen, 'showlogin': 'True'}
                return render(request, 'ced_main/lcmap_sb_down.html', context)

            obj = form.save(commit=False)
            prid = obj.Project_ID
            obj.save()

            obj1 = implementation_info()
            obj1.Project_ID = prid
            obj1.Prj_ID = prid
            obj1.Imp_Status = impstat
            obj1.Date_Entered = datetime.datetime.now()
            obj1.User = request.user.username
            obj1.save()

            # Now call the index() view.
            # The user will be shown the homepage.
            context = {'form': form, 'authen': authen}

            if typeactval == "Spatial Project":
                return redirect('/sgce/grsgmap/' + str(prid) + '/footprinteditor?CEDID=' + str(prid))
            else:
                return redirect('/sgce/' + str(prid) + '/editproject?step=Location', context)

        else:
            print(form.errors)
            context = {'form': form, 'authen': authen}
            # The supplied form contained errors - just print them to the terminal.
            return render(request, 'ced_main/dataentrynew.html', context)
    else:
        # If the request was not a POST, display the form to enter details.

        form = newprj_Form(initial={
            'Implementing_Party': imp_party_values.objects.get(
                Implementation_Party=userprofile.objects.values_list('Agency', flat=True).get(User_id=request.user.id)),
            'Office': userprofile.objects.values_list('Field_Office', flat=True).get(User_id=request.user.id),
            'Created_By': request.user,
            'Date_Created': datetime.datetime.now(),
        })
        context = {'form': form, 'authen': authen, 'showlogin': 'True'}
    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).

    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        if authen == 'authenadmin' or authen == 'authenapp':
            if accepted == 'accepted':
                if enterdata == 'dataenter':
                    return render(request, 'ced_main/dataentrynew.html', context)
                else:
                    return render(request, 'ced_main/permission_denied.html', context)
            else:
                return render(request, 'ced_main/accept_user_agreement.html', context)
        else:
            if accepted == 'accepted':
                if enterdata == 'dataenter':
                    return render(request, 'ced_main/dataentrynew.html', context)
                else:
                    return render(request, 'ced_main/permission_denied.html', context)
            else:
                return render(request, 'ced_main/accept_user_agreement.html', context)

    else:
        return render(request, 'ced_main/permission_denied.html', context)


@login_required
def editproject(request, prid):
    # Get the context from the request.

    siteurl = request.build_absolute_uri()
    siteurl1 = siteurl.split("/")
    siteurl2 = siteurl1[0] + "//" + siteurl1[2]

    try:
        pid = project_info.objects.get(pk=prid)
    except:
        return redirect('/sgce/project_not_exists_temp/')

    prjname = project_info.objects.values_list('Project_Name', flat=True).get(pk=prid)
    typeactval = project_info.objects.values_list('TypeAct', flat=True).get(pk=prid)
    Activity = project_info.objects.values_list('Activity', flat=True).get(pk=prid)
    subact = project_info.objects.values_list('SubActivity', flat=True).get(pk=prid)
    batchupload = project_info.objects.values_list('Batch_Upload', flat=True).get(pk=prid)
    conoffice = userprofile.objects.values_list('Field_Office', flat=True).get(
    User_id__exact=User.objects.values_list('id', flat=True).get(username__exact=request.user))
    seedtype = project_info.objects.values_list('seeding_type', flat=True).get(pk=prid)
    approval = project_info.objects.values_list('Entry_Type', flat=True).get(pk=prid)

    db = MySQLdb.connect(host=hst, user=usr, passwd=psswrd, db=dtbs)

    staids = state_info.objects.values_list('id', flat=True).filter(Project_ID=prid)

    stassel = ""
    cnt = 1
    for staid in staids:
        cursor = db.cursor()
        cursor.execute("SELECT state_id FROM ced_main_state_info_state_value WHERE state_info_id = " + str(staid))
        numrows = cursor.rowcount
        if numrows > 0:
            # for x in xrange(0, numrows): #python 2.7
            for x in range(0, numrows):
                rows = cursor.fetchone()

                for row in rows:
                    Stval = state.objects.values_list('StateName', flat=True).get(pk=row)
                    if cnt == 1:
                        stassel = str(Stval)
                        cnt = 2
                    else:
                        stassel = stassel + " | " + str(Stval)

    try:
        del cursor
    except:
        a = 1
    # Counties
    cnt = 1
    cntids = county_info.objects.values_list('id', flat=True).filter(Project_ID=prid)
    cntssel = ""
    for cntid in cntids:
        cursor = db.cursor()
        cursor.execute(
            "SELECT state_county_id FROM ced_main_county_info_county_value WHERE county_info_id = " + str(cntid))
        numrows = cursor.rowcount
        if numrows > 0:
            # for x in xrange(0, numrows): #python 2.7
            for x in range(0, numrows):
                rows = cursor.fetchone()

                for row in rows:
                    Cntyval = state_county.objects.values_list('Cnty_St', flat=True).get(pk=row)
                    if cnt == 1:
                        cntssel = str(Cntyval)
                        cnt = 2
                    else:
                        cntssel = cntssel + " | " + str(Cntyval)

    try:
        del cursor
    except:
        a = 1
    # Ownership
    cnt = 1
    ownids = ownership_info.objects.values_list('id', flat=True).filter(Project_ID=prid)
    ownssel = ""
    for ownid in ownids:
        cursor = db.cursor()
        cursor.execute(
            "SELECT ownership_values_id FROM ced_main_ownership_info_owner_value WHERE ownership_info_id = " + str(ownid)
        )
        numrows = cursor.rowcount
        if numrows > 0:
            # for x in xrange(0, numrows): #python 2.7
            for x in range(0, numrows):
                rows = cursor.fetchone()

                for row in rows:
                    ownership_values
                    Ownval = ownership_values.objects.values_list('Owners', flat=True).get(pk=row)
                    if cnt == 1:
                        ownssel = str(Ownval)
                        cnt = 2
                    else:
                        ownssel = ownssel + " | " + str(Ownval)

    try:
        del cursor
    except:
        a = 1

    # Collaborating Parites
    cnt = 1
    colids = collab_party.objects.values_list('id', flat=True).filter(Project_ID=prid)
    colabssel = ""
    for colid in colids:
        cursor = db.cursor()
        cursor.execute(
            "SELECT imp_party_values_id FROM ced_main_collab_party_collab_party WHERE collab_party_id = " + str(colid))
        numrows = cursor.rowcount
        if numrows > 0:
            # for x in xrange(0, numrows): #python 2.7
            for x in range(0, numrows):
                rows = cursor.fetchone()

                for row in rows:
                    Colval = imp_party_values.objects.values_list('Implementation_Party', flat=True).get(pk=row)
                    if cnt == 1:
                        colabssel = str(Colval)
                        cnt = 2
                    else:
                        colabssel = colabssel + " | " + str(Colval)
    try:
        del cursor
    except:
        a = 1

    # SubActivityObjectives
    cnt = 1
    obids = subactivity_objectives.objects.values_list('id', flat=True).filter(Project_ID=prid)
    obidssel = ""
    for obid in obids:
        cursor = db.cursor()
        cursor.execute(
            "SELECT subactivity_objectives_data_id FROM ced_main_subactivity_objectives_objective WHERE subactivity_objectives_id = " + str(obid))
        numrows = cursor.rowcount
        if numrows > 0:
            # for x in xrange(0, numrows): #python 2.7
            for x in range(0, numrows):
                rows = cursor.fetchone()

                for row in rows:
                    Objval = subactivity_objectives_data.objects.values_list('Objective', flat=True).get(pk=row)
                    if cnt == 1:
                        obidssel = str(Objval)
                        cnt = 2
                    else:
                        obidssel = obidssel + " | " + str(Objval)
    try:
        del cursor
    except:
        a = 1

    # subactivity_methods
    cnt = 1
    mtids = subactivity_methods.objects.values_list('id', flat=True).filter(Project_ID=prid)
    mtidssel = ""
    for mtid in mtids:
        cursor = db.cursor()
        cursor.execute(
            "SELECT subactivity_methods_data_id FROM ced_main_subactivity_methods_method WHERE subactivity_methods_id = " + str(mtid))
        numrows = cursor.rowcount
        if numrows > 0:
            # for x in xrange(0, numrows): #python 2.7
            for x in range(0, numrows):
                rows = cursor.fetchone()

                for row in rows:
                    Mthval = subactivity_methods_data.objects.values_list('Method', flat=True).get(pk=row)
                    if cnt == 1:
                        mtidssel = str(Mthval)
                        cnt = 2
                    else:
                        mtidssel = mtidssel + " | " + str(Mthval)
    try:
        del cursor
    except:
        a = 1

    # subactivity_effective_state
    cnt = 1
    esids = subactivity_effective_state.objects.values_list('id', flat=True).filter(Project_ID=prid)
    esidssel = ""
    for esid in esids:
        cursor = db.cursor()
        cursor.execute(
            "SELECT subactivity_effective_state_data_id FROM ced_main_subactivity_effective_state_effectiveness_statement WHERE subactivity_effective_state_id = " + str(esid))
        numrows = cursor.rowcount
        if numrows > 0:
            # for x in xrange(0, numrows): #python 2.7
            for x in range(0, numrows):
                rows = cursor.fetchone()

                for row in rows:
                    ESval = subactivity_effective_state_data.objects.values_list('Effectiveness_Statement', flat=True).get(pk=row)
                    if cnt == 1:
                        esidssel = str(ESval)
                        cnt = 2
                    else:
                        esidssel = esidssel + " | " + str(ESval)
    try:
        del cursor
    except:
        a = 1

    # Threats
    cnt = 1
    thrids = threats.objects.values_list('id', flat=True).filter(Project_ID=prid)
    thrssel = ""
    for thrid in thrids:
        cursor = db.cursor()
        cursor.execute("SELECT threat_values_id FROM ced_main_threats_threat WHERE threats_id = " + str(thrid))
        numrows = cursor.rowcount
        if numrows > 0:
            # for x in xrange(0, numrows): #python 2.7
            for x in range(0, numrows):
                rows = cursor.fetchone()

                for row in rows:
                    Thrval = threat_values.objects.values_list('Threats', flat=True).get(pk=row)
                    if cnt == 1:
                        thrssel = str(Thrval)
                        cnt = 2
                    else:
                        thrssel = thrssel + " | " + str(Thrval)
    try:
        del cursor
    except:
        a = 1

    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    authuser = checkauthorization(prid, request.user)

    try:
        lcmap = project_info.objects.values_list('LCMItem', flat=True).get(pk=prid)
    except:
        lcmap = ""
    if lcmap == None or lcmap == "":
        try:
            obj = project_info.objects.get(Project_ID=prid)
            itemID = create_sgce_folder(str(prid))
            spatialdest = itemID
            obj.LCMItem = itemID
            obj.save()
        except:
            context = {'authen': authen}
            return render(request, 'ced_main/lcmap_sb_down.html', context)

    if typeactval == "Spatial Project" or typeactval == "Project":
        try:
            spatialid = project_info.objects.values_list('Shapefile', flat=True).get(pk=prid)
        except:
            spatialid = ""

        if spatialid == None or spatialid == "":
            try:
                obj = project_info.objects.get(Project_ID=prid)
                spatiltitle = str(prjname) + "_Spatial_Data"
                itemID = create_spatial_folder(spatialdest, spatiltitle)
                obj.Shapefile = itemID
                obj.save()
            except:
                context = {'authen': authen}
                return render(request, 'ced_main/lcmap_sb_down.html', context)
    else:
        spatialid = ""

    featcnt = featurecount(spatialid)

    if featcnt == "NotPoly":
        NotPoly = "NotPoly"
    else:
        NotPoly = ""

    enterdata = checkenter(request.user.groups.values_list('name', flat=True))
    accepted = checkaccept(userprofile.objects.values_list('Waiver_V2_Approved', flat=True).get(
        User_id__exact=User.objects.values_list('id', flat=True).get(username__exact=request.user)))

    try:
        Loc = project_info.objects.values_list('PageLoc', flat=True).get(pk=prid)
    except:
        Loc = 'None'

    DocumentFormSet = modelformset_factory(documentation, extra=0, form=documentation_Form)
    try:
        pidimp = implementation_info.objects.get(pk=prid)
    except:
        NoImp = "NoImp"

    try:
        pidcol = collab_party.objects.get(Project_ID=prid)
    except:
        NoCol = "NoCol"

    try:
        obcol = subactivity_objectives.objects.get(Project_ID=prid)
    except:
        NoOb = "NoOb"

    try:
        mtcol = subactivity_methods.objects.get(Project_ID=prid)
    except:
        NoMTl = "NoMT"

    try:
        escol = subactivity_effective_state.objects.get(Project_ID=prid)
    except:
        NoES = "NoES"

    try:
        pidthr = threats.objects.get(Project_ID=prid)
    except:
        NoThr = "NoThr"

    try:
        pidst = state_info.objects.get(Project_ID=prid)
    except:
        NoState = "NoState"

    try:
        pidow = ownership_info.objects.get(Project_ID=prid)
    except:
        NoOwn = "NoOwn"

    try:
        pidco = county_info.objects.get(Project_ID=prid)
    except:
        NoState = "NoCounty"

    try:
        subform6 = county_Form(request.POST, instance=pidco)
    except:
        subform6 = county_Form(request.POST)

    try:
        MET = metric.objects.get(Metric=project_info.objects.values_list('Metric', flat=True).get(Project_ID=prid))
    except:
        MET = 0

    form = editprj_Form(initial={
        'Metric': MET
    }, instance=pid)

    try:
        subform1 = documentation_Form(initial={
            'Project_ID': collab_party.objects.get(Project_ID=prid),
            'Threat': collab_party.objects.values_list('Collab_Party', flat=True).filter(Project_ID=prid)
        }, instance=pidthr)
    except:
        subform1 = documentation_Form()

    try:
        subform2 = threats_Form(initial={
            'Project_ID': threats.objects.get(Project_ID=prid),
            'Threat': threats.objects.values_list('Threat', flat=True).filter(Project_ID=prid)
        }, instance=pidthr)
    except:
        subform2 = threats_Form()

    try:
        subform3 = collab_party_Form(initial={
            'Project_ID': collab_party.objects.get(Project_ID=prid),
            'Collab_Party': collab_party.objects.values_list('Collab_Party', flat=True).filter(Project_ID=prid)
        }, instance=pidcol)
    except:
        subform3 = collab_party_Form()


    try:
        subform4 = implementation_info_Form(initial={
            'Project_ID': implementation_info.objects.get(Project_ID=prid),
            'Imp_Status': implementation_info.objects.values_list('Imp_Status', flat=True).get(Project_ID=prid),
        }, instance=pidimp)
        selectedchoices = getimpchoices(subact)
        subform4.fields["Effective_Determined"].choices = selectedchoices
    except:
        subform4 = implementation_info_Form()
        subform4.fields["Effective_Determined"].choices = selectedchoices

    try:
        subform5 = state_Form(initial={
            'Project_ID': state_info.objects.get(Project_ID=prid),
            'State_Value': state_info.objects.values_list('State_Value', flat=True).filter(Project_ID=prid)
        }, instance=pidst)
    except:
        subform5 = state_Form()

    try:
        subform6 = county_Form(initial={
            'Project_ID': county_info.objects.get(Project_ID=prid),
            'County_Value': county_info.objects.values_list('County_Value', flat=True).filter(Project_ID=prid)
        }, instance=pidco)
    except:
        subform6 = county_Form()

    try:
        subform10 = ownership_Form(initial={
            'Project_ID': ownership_info.objects.get(Project_ID=prid),
            'Owner_Value': ownership_info.objects.values_list('Owner_Value', flat=True).filter(Project_ID=prid)
        }, instance=pidow)
    except:
        subform10 = ownership_Form()


    try:
        subform11 = subactivity_objectives_Form(initial={
            'Project_ID': subactivity_objectives.objects.get(Project_ID=prid),
            'Objective': subactivity_objectives.objects.values_list('Objective', flat=True).filter(Project_ID=prid)
        }, instance=obcol)
        subform11.fields["Objective"].queryset = subactivity_objectives_data.objects.filter(SubActivity=subact).order_by("Ordering")
    except:
        subform11 = subactivity_objectives_Form()
        subform11.fields["Objective"].queryset = subactivity_objectives_data.objects.filter(SubActivity=subact).order_by("Ordering")

    try:
        subform12 = subactivity_methods_Form(initial={
            'Project_ID': subactivity_methods.objects.get(Project_ID=prid),
            'Method': subactivity_methods.objects.values_list('Method', flat=True).filter(Project_ID=prid)
        }, instance=mtcol)
        subform12.fields["Method"].queryset = subactivity_methods_data.objects.filter(SubActivity=subact).order_by("Ordering")
    except:
        subform12 = subactivity_methods_Form()
        subform12.fields["Method"].queryset = subactivity_methods_data.objects.filter(SubActivity=subact).order_by("Ordering")

    try:
        subform13 = subactivity_effective_state_Form(initial={
            'Project_ID': subactivity_effective_state.objects.get(Project_ID=prid),
            'Effectiveness_Statement': subactivity_effective_state.objects.values_list('Effectiveness_Statement', flat=True).filter(Project_ID=prid)
        }, instance=escol)
        subform13.fields["Effectiveness_Statement"].queryset = subactivity_effective_state_data.objects.filter(SubActivity=subact).order_by("Ordering")
    except:
        subform13 = subactivity_effective_state_Form()
        subform13.fields["Effectiveness_Statement"].queryset = subactivity_effective_state_data.objects.filter(SubActivity=subact).order_by("Ordering")



    formset = DocumentFormSet(queryset=documentation.objects.filter(Project_ID=prid))

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).

    allfiles = str(project_info.objects.values_list('LCMItem', flat=True).filter(Project_ID=prid))
    allfiles1 = allfiles[3:27]

    logonpysb = 'None'
    logon = 'None'
    josso = "None"
    spatialid = "None"

    Activity = "None"
    Threats = "None"
    Documentation = "None"
    Location = "None"
    WAFWA = "None"
    Populations = "None"
    States = "None"
    Counties = "None"
    Ownership = "None"
    Part1 = "None"
    Part23 = "None"
    Collab = "None"
    Objectives = "None"
    Methods = "None"
    EffectState = "None"

    Activity = project_info.objects.values_list('Activity', flat=True).get(pk=prid)
    # A HTTP POST?
    if request.method == 'POST':

        if 'spatlink' in request.POST:

            return redirect('/sgce/grsgmap/' + prid + '/footprinteditor?CEDID=' + prid)

        if conoffice == 'Congress':
            if 'Spatial' in request.POST:
                return redirect('/sgce/' + prid + '/footprinteditor')
            return redirect('/sgce/readonly/')
        form = editprj_Form(request.POST, request.FILES, instance=pid)

        try:
            subform2 = threats_Form(request.POST, instance=pidthr)
        except:
            subform2 = threats_Form(request.POST)

        try:
            subform3 = collab_party_Form(request.POST, instance=pidcol)
        except:
            subform3 = collab_party_Form(request.POST)

        try:
            subform4 = implementation_info_Form(request.POST, instance=pidimp)
        except:
            subform4 = implementation_info_Form(request.POST)

        try:
            subform5 = state_Form(request.POST, instance=pidst)
        except:
            subform5 = state_Form(request.POST)

        try:
            subform6 = county_Form(request.POST, instance=pidco)
        except:
            subform6 = county_Form(request.POST)

        try:
            subform10 = ownership_Form(request.POST, instance=pidow)
        except:
            subform10 = ownership_Form(request.POST)

        try:
            subform11 = subactivity_objectives_Form(request.POST, instance=obcol)
        except:
            subform11 = subactivity_objectives_Form(request.POST)

        try:
            subform12 = subactivity_methods_Form(request.POST, instance=mtcol)
        except:
            subform12 = subactivity_methods_Form(request.POST)

        try:
            subform13 = subactivity_effective_state_Form(request.POST, instance=escol)
        except:
            subform13 = subactivity_effective_state_Form(request.POST)

        formset = DocumentFormSet(request.POST, request.FILES, queryset=documentation.objects.filter(Project_ID=prid))

        # Have we been provided with a valid form?
        if 'deleteapp' in request.POST:
            if authen == 'authenadmin':
                deleteprj = deletethewholeproject(prid)
                return redirect('/sgce/delete_success/')

        if subform4.is_valid():
            a=1
        else:
            print(subform4.errors)

        if form.is_valid() and subform2.is_valid() and subform3.is_valid() and subform4.is_valid() and subform5.is_valid() and subform6.is_valid() and subform10.is_valid() and subform11.is_valid() and subform12.is_valid() and subform13.is_valid() and formset.is_valid():  # and subform1.is_valid() :

            # Save the new category to the database.
            EmailSent = "None"
            try:
                origvalst = state_info.objects.values_list('State_Value', flat=True).filter(Project_ID=prid)
            except:
                origvalst = ["None"]

            try:
                origvalcn = county_info.objects.values_list('County_Value', flat=True).filter(Project_ID=prid)
            except:
                origvalcn = ["None"]


            try:
                obj = form.save(commit=False)
                # # Save Implementation Information


                obj.Approving_Official = project_info.objects.values_list('Approving_Official', flat=True).get(
                    Project_ID=prid)
                obj.Implementing_Party = project_info.objects.values_list('Implementing_Party', flat=True).get(
                    Project_ID=prid)
                obj.TypeAct = project_info.objects.values_list('TypeAct', flat=True).get(Project_ID=prid)
                obj.Activity = project_info.objects.values_list('Activity', flat=True).get(Project_ID=prid)
                obj.SubActivity = project_info.objects.values_list('SubActivity', flat=True).get(Project_ID=prid)
                obj.Office = project_info.objects.values_list('Office', flat=True).get(Project_ID=prid)
                obj.User_Email = project_info.objects.values_list('User_Email', flat=True).get(Project_ID=prid)
                obj.User_Phone_Number = project_info.objects.values_list('User_Phone_Number', flat=True).get(
                    Project_ID=prid)
                obj.Last_Updated = now
                obj.Updating_User = request.user.username
                obj.Created_By = project_info.objects.values_list('Created_By', flat=True).get(Project_ID=prid)
                obj.Date_Created = project_info.objects.values_list('Date_Created', flat=True).get(Project_ID=prid)
                obj.Entry_Type = project_info.objects.values_list('Entry_Type', flat=True).get(Project_ID=prid)
                obj.Project_Status = project_info.objects.values_list('Project_Status', flat=True).get(Project_ID=prid)



                prjname = obj.Project_Name

                
                try:
                    dest = project_info.objects.values_list('LCMItem', flat=True).get(Project_ID=prid)
                    if dest == "" or dest == None or dest == "None":
                        itemID = create_sgce_folder(str(obj.Project_ID))
                        obj.LCMItem = itemID
                except:
                    itemID = create_sgce_folder(str(obj.Project_ID))
                    obj.LCMItem = itemID

                if (
                        dest == "" or dest == None or dest == "None") and typeactval == "Project" or typeactval == "Spatial Project":
                    try:
                        itemIDhome = itemID
                        dest = project_info.objects.values_list('Shapefile', flat=True).get(Project_ID=prid)
                        spatiltitle = str(obj.Project_Name) + "_Spatial_Data"
                        itemID = create_spatial_folder(itemIDhome, spatiltitle)
                        obj.LCMItem = itemID
                    except:
                        dest = project_info.objects.values_list('Shapefile', flat=True).get(Project_ID=prid)
                        pdest = project_info.objects.values_list('LCMItem', flat=True).get(Project_ID=prid)
                        if dest == "" or dest == None or dest == "None":
                            spatiltitle = str(obj.Project_Name) + "_Spatial_Data"
                            itemID = create_spatial_folder(pdest, spatiltitle)
                            obj.LCMItem = itemID

                obj.save()
            except:
                print("Project Info Saving Failed")

            objprjname = project_info.objects.get(Project_ID=prid)
            objprjname.Project_Name = prjname
            objprjname.save()

            try:
                i = 0
                for form in formset.forms:
                    obj12 = form.save(commit=False)
                    fff = "form-" + str(i) + "-File_Type"
                    fffTest = request.POST.get(fff)
                    if fffTest == '---Select/Update File Type---':
                        NoUpdate = "No Update"
                    else:
                        obj12.File_Type = request.POST.get(fff)
                    doc = documentation.objects.values_list('Document_Name', flat=True).get(id=obj12.id)
                    obj12.Document_Name = doc
                    obj12.save()
                    i = i + 1
            except:
                print("Documentation Saving Failed")

            try:
                thcnt = 0
                for level in request.POST.getlist('Threat'):
                    obj2 = subform2.save(commit=False)
                    obj2.Project_ID = pid
                    obj2.Date_Entered = now
                    obj2.User = request.user.username
                    obj2.save()
                    thcnt = 1
                if thcnt == 1:
                    subform2.save_m2m()
                else:
                    threats.objects.filter(Project_ID=prid).delete()
            except:
                print("Threats Saving Failed")

            try:
                obj4 = subform4.save(commit=False)
                obj4.Project_ID = prid
                obj4.Date_Entered = now
                obj4.User = request.user.username
                obj4.save()
                prjstat = implementation_info.objects.values_list('Imp_Status', flat=True).get(Project_ID=prid)
                objsave = project_info.objects.get(Project_ID=prid)
                obj.Project_Status = prjstat
                obj.save()
            except:
                print("Implementation Saving Failed")
                try:
                    obj4 = subform4.save(commit=False)
                    obj4.Project_ID = prid
                    obj4.Date_Entered = now
                    try:
                        IEC = implementation_info.objects.values_list('Imp_and_Effect_Correct', flat=True).get(
                            Project_ID=prid)
                    except:
                        IEC = 0
                    obj4.Imp_and_Effect_Correct = IEC
                    try:
                        IECE = implementation_info.objects.values_list('Imp_and_Effect_Cor_Explan', flat=True).get(
                            Project_ID=prid)
                    except:
                        IECE = ""
                    obj4.Imp_and_Effect_Cor_Explan = IECE
                    obj4.User = request.user.username
                    obj4.save()
                    prjstat = implementation_info.objects.values_list('Imp_Status', flat=True).get(Project_ID=prid)
                    objsave = project_info.objects.get(Project_ID=prid)
                    objsave.Project_Status = prjstat
                    objsave.save()
                    print("Implementation Saving second try succeeded")
                except:
                    print("Implementation Saving third try attempt")
                    try:
                        obj4 = subform4.save(commit=False)
                        obj4.Project_ID = prid
                        obj4.Date_Entered = now

                        if 'Effective_Determined' in request.POST:
                            print("Effective_Determined")
                        else:
                            obj4.Effective_Determined = 0

                        if 'Reas_Certain' in request.POST:
                            print("Reas_Certain")
                        else:
                            obj4.Reas_Certain = 0

                        if 'Legal_Authority' in request.POST:
                            print("Legal_Authority")
                        else:
                            obj4.Legal_Authority = 0

                        if 'Staff_Available' in request.POST:
                            print("Staff_Available")
                        else:
                            obj4.Staff_Available = 0

                        if 'Regulatory_Mech' in request.POST:
                            print("Regulatory_Mech")
                        else:
                            obj4.Regulatory_Mech = 0

                        if 'Compliance' in request.POST:
                            print("Compliance")
                        else:
                            obj4.Compliance = 0

                        if 'Vol_Incentives' in request.POST:
                            print("Vol_Incentives")
                        else:
                            obj4.Vol_Incentives = 0

                        if 'Reduce_Threats' in request.POST:
                            print("Reduce_Threats")
                        else:
                            obj4.Reduce_Threats = 0

                        if 'Incremental_Objectives' in request.POST:
                            print("Incremental_Objectives")
                        else:
                            obj4.Incremental_Objectives = 0

                        if 'Quantifiable_Measures' in request.POST:
                            print("Quantifiable_Measures")
                        else:
                            obj4.Quantifiable_Measures = 0

                        if 'AD_Strategy' in request.POST:
                            print("AD_Strategy")
                        else:
                            obj4.AD_Strategy = 0

                        try:
                            IEC = implementation_info.objects.values_list('Imp_and_Effect_Correct', flat=True).get(
                                Project_ID=prid)
                        except:
                            IEC = 0
                        obj4.Imp_and_Effect_Correct = IEC
                        try:
                            IECE = implementation_info.objects.values_list('Imp_and_Effect_Cor_Explan', flat=True).get(
                                Project_ID=prid)
                        except:
                            IECE = ""
                        obj4.Imp_and_Effect_Cor_Explan = IECE
                        obj4.User = request.user.username
                        obj4.save()
                        prjstat = implementation_info.objects.values_list('Imp_Status', flat=True).get(Project_ID=prid)
                        objsave = project_info.objects.get(Project_ID=prid)
                        objsave.Project_Status = prjstat
                        objsave.save()
                    except:
                        print("Third try failed")

            try:
                obcnt = 0
                for level in request.POST.getlist('Objective'):
                    obj11 = subform11.save(commit=False)
                    obj11.Project_ID = pid
                    obj11.Date_Entered = now
                    obj11.User = request.user.username
                    obj11.save()
                    obcnt = 1
                if obcnt == 1:
                    subform11.save_m2m()
                else:
                    subactivity_objectives.objects.filter(Project_ID=prid).delete()
            except:
                print("SubActivity Objectives Saving Failed")

            try:
                mtcnt = 0
                for level in request.POST.getlist('Method'):
                    obj12 = subform12.save(commit=False)
                    obj12.Project_ID = pid
                    obj12.Date_Entered = now
                    obj12.User = request.user.username
                    obj12.save()
                    mtcnt = 1
                if mtcnt == 1:
                    subform12.save_m2m()
                else:
                    subactivity_methods.objects.filter(Project_ID=prid).delete()
            except:
                print("SubActivity Methods Saving Failed")

            try:
                escnt = 0
                for level in request.POST.getlist('Effectiveness_Statement'):
                    obj13 = subform13.save(commit=False)
                    obj13.Project_ID = pid
                    obj13.Date_Entered = now
                    obj13.User = request.user.username
                    obj13.save()
                    escnt = 1
                if escnt == 1:
                    subform13.save_m2m()
                else:
                    subactivity_effective_state.objects.filter(Project_ID=prid).delete()
            except:
                print("SubActivity Effectiveness Statement Saving Failed")

            try:
                stcnt = 0
                for level2 in request.POST.getlist('State_Value'):
                    obj5 = subform5.save(commit=False)
                    obj5.Project_ID = pid
                    obj5.Date_Entered = now
                    obj5.User = request.user.username
                    obj5.save()
                    stcnt = 1

                if stcnt == 1:
                    subform5.save_m2m()
            except:
                print("States Saving Failed")

            try:
                colcnt = 0
                for level3 in request.POST.getlist('Collab_Party'):
                    obj3 = subform3.save(commit=False)
                    obj3.Project_ID = pid
                    obj3.Date_Entered = now
                    obj3.User = request.user.username
                    obj3.save()
                    colcnt = 1

                if colcnt == 1:
                    subform3.save_m2m()
                else:
                    collab_party.objects.filter(Project_ID=prid).delete()
            except:
                print("Collab Parties Saving Failed")

            try:
                cntcnt = 0
                for level4 in request.POST.getlist('County_Value'):
                    obj6 = subform6.save(commit=False)
                    obj6.Project_ID = pid
                    obj6.Date_Entered = now
                    obj6.User = request.user.username
                    obj6.save()
                    cntcnt = 1

                if cntcnt == 1:
                    subform6.save_m2m()
                else:
                    county_info.objects.filter(Project_ID=prid).delete()
            except:
                print("Second County Saving Failed")

            try:
                owncnt = 0
                for level8 in request.POST.getlist('Owner_Value'):
                    obj10 = subform10.save(commit=False)
                    obj10.Project_ID = pid
                    obj10.Date_Entered = now
                    obj10.User = request.user.username
                    obj10.save()
                    owncnt = 1
                if owncnt == 1:
                    subform10.save_m2m()
                else:
                    ownership_info.objects.filter(Project_ID=prid).delete()
            except:
                print("Owners Saving Failed")

            try:
                MET = metric.objects.get(
                    Metric=project_info.objects.values_list('Metric', flat=True).get(Project_ID=prid))
            except:
                MET = ""

            # try:
            dest = documentation.objects.values_list('id', flat=True).filter(Project_ID=prid)
            for de in dest:
                dest1 = documentation.objects.values_list('Document_Name', flat=True).get(id=de)
                dedel = "Delete_" + dest1
                if dedel in request.POST:
                    docid = documentation.objects.values_list('LCMItem', flat=True).get(id=de)
                    documentation.objects.filter(id=de).delete()

                    return redirect('/sgce/' + prid + '/editproject/?step=Activity')

            # try:
            for do in dest:
                dest1 = documentation.objects.values_list('Document_Name', flat=True).get(id=do)
                dodown = "Download_" + dest1
                if dodown in request.POST:
                    docid = documentation.objects.values_list('LCMItem', flat=True).get(id=do)
                    url = "https://www.sciencebase.gov/catalog/item/" + str(docid)
                    logonpysbdoc, sbid = Login2SBandOpenFootprintStudio1(url, str(docid))
                    LCJason = "https://www.sciencebase.gov/catalog/file/get/" + str(
                        docid) + "?" + sbid + "&josso=" + str(logonpysbdoc) + "&;"
                    print(LCJason)
                    return redirect('/sgce/' + prid + '/editproject/?step=Activity&LCJason=' + LCJason)

            # try:
            if 'upload' in request.POST:
                DocFailed = ""
                dest = project_info.objects.values_list('LCMItem', flat=True).get(Project_ID=prid)
                for afile in request.FILES.getlist('myfiles'):
                    lcitem = handle_uploaded_file_sgce(afile, dest)
                    time.sleep(0.25)
                    if lcitem == "Upload Failed":
                        DocFailed = "DocFailed"
                    else:
                        obj1 = documentation()
                        obj1.Project_ID = prid
                        obj1.LCMItem = str(lcitem)
                        obj1.Document_Name = str(afile)
                        obj1.Date_Entered = now
                        obj1.User = request.user.username
                        obj1.save()

                return redirect('/sgce/' + prid + '/editproject/?step=Activity')

            # Check for projects marked for deletion
            mfd = project_info.objects.values_list('Mark_For_Deletion', flat=True).get(Project_ID=prid)
            if mfd == True:
                if 'approveapp' in request.POST:
                    Subject = "The approving official " + request.user.first_name + " " + request.user.last_name + " has requested the effort " + str(
                        prid) + "-" + project_info.objects.values_list('Project_Name', flat=True).get(
                        Project_ID=prid) + " be permanently deleted"
                    Message = "The approving official " + request.user.username + " has requested that the effort #" + str(
                        prid) + ", Name:" + project_info.objects.values_list('Project_Name', flat=True).get(
                        Project_ID=prid) + " be permanently deleted from the CED.  Please contact the approving official at " + request.user.email + " if confirmation is needed.  Otherwise this effort should be removed from the CED."
                    From = DEFAULT_FROM_EMAIL

                    qresult = ["jwelty@usgs.gov", "lief_wiechman@fws.gov", "kernt@usgs.gov"]
                    To = ""
                    for rst in qresult:
                        To = To + rst
                    send_mail(Subject, Message, From, qresult, fail_silently=False)

                    objsave = project_info.objects.get(Project_ID=prid)
                    objsave.Entry_Type = 4
                    objsave.save()
                    return redirect('/sgce/permanent_deletion')

                else:
                    qresult = User.objects.values_list('email').get(username=obj.Approving_Official)
                    useremailadd = User.objects.values_list('email').get(username=request.user.username)
                    # Send marked for deletion email if the project indicates it should be deleted
                    if useremailadd != qresult:
                        Subject = "The effort " + str(prid) + "-" + project_info.objects.values_list('Project_Name',
                                                                                                     flat=True).get(
                            Project_ID=prid) + " has been marked for deletion by " + request.user.first_name + " " + request.user.last_name
                        Message = "The user " + request.user.username + " has listed you as their approving official and is requesting that the effort #" + str(
                            prid) + ", Name: " + project_info.objects.values_list('Project_Name', flat=True).get(
                            Project_ID=prid) + " be deleted.  If this is correct, please login to the CED (" + siteurl2 + "/sgce/) and contact a CED administrator to confirm this effort should be removed from the database.  When an effort is flagged for deletion it will not be viewable to anyone except administrators and those with editing rights for the effort.  However, unless the effort is fully deleted, it is still subject to a FOIA request."
                        From = DEFAULT_FROM_EMAIL

                        To = ""
                        for rst in qresult:
                            To = To + rst
                        send_mail(Subject, Message, From, [To], fail_silently=False)

                objsave = project_info.objects.get(Project_ID=prid)
                objsave.Entry_Type = 4
                objsave.save()
                return redirect('/sgce/mark_for_deletion')

            # try:
            # Now call the index() view.
            # The user will be shown the homepage.

            if 'emailapp' in request.POST or 'approveapp' in request.POST:

                if 'approveapp' in request.POST:

                    Subject = "Your effort " + obj.Project_Name + " has been stamped approved by " + request.user.first_name + " " + request.user.last_name
                    Message = "The approving official " + request.user.first_name + " " + request.user.last_name + " (username: " + request.user.username + ") has approved your project " + obj.Project_Name + ". Please login to the CED (" + siteurl2 + "/sgce/) if any further changes are needed."
                    From = DEFAULT_FROM_EMAIL
                    qresult = User.objects.values_list('email').get(username=obj.Created_By)
                    To = ""
                    for rst in qresult:
                        To = To + rst
                    send_mail(Subject, Message, From, [To], fail_silently=False)
                    EmailSent = "EmailApproved"
                    objsave = project_info.objects.get(Project_ID=prid)
                    objsave.Entry_Type = 3
                    objsave.Date_Approved = now
                    objsave.PageLoc = "Top"
                    objsave.save()
                    context = {'form': form, 'authen': authen, 'EmailSent': EmailSent}
                    return redirect('/sgce/project_approved')
                else:

                    Subject = "The effort " + project_info.objects.values_list('Project_Name', flat=True).get(
                        Project_ID=prid) + " has been submitted for approval by " + request.user.first_name + " " + request.user.last_name
                    Message = "The user " + request.user.username + " has listed you as their approving official and is requesting that the project " + project_info.objects.values_list(
                        'Project_Name', flat=True).get(
                        Project_ID=prid) + " be approved.  Please login to the CED (" + siteurl2 + "/sgce/) and view this project."
                    From = DEFAULT_FROM_EMAIL
                    qresult = User.objects.values_list('email').get(username=obj.Approving_Official)
                    To = ''
                    for rst in qresult:
                        To = To + rst
                    To = To + ", fw1sagegrouseced@fws.gov"
                    send_mail(Subject, Message, From, [To], fail_silently=False)

                    EmailSent = "EmailSent"
                    objsave = project_info.objects.get(Project_ID=prid)

                    objsave.Entry_Type = 2

                    objsave.save()
                    context = {'form': form, 'authen': authen, 'EmailSent': EmailSent}
                    return redirect('/sgce/project_approval_success')
            if 'spatlink' in request.POST:
                return redirect('/sgce/' + prid + '/footprinteditor')

            try:
                context = {'authen': authen, 'EmailSent': EmailSent}
                return render(request, 'ced_main/edit_project_success.html', context)
                
            except:
                print("Failed to redirect to project success")

            return redirect('/sgce/' + prid + '/editproject/?step=Location')
    else:
        # if request.user.is_authenticated(): Pythoon 2.7
        if request.user.is_authenticated:

            sbdown1 = testsb()
            if sbdown1 == "True":
                return redirect('/sgce/sbunavailable/')
            if authen == 'authenadmin' or authen == 'authenapp' or authuser == 'Authorized':
                if accepted == 'accepted':
                    if enterdata == 'dataenter':
                        if typeactval == "Spatial Project" or typeactval == "Project":
                            if int(batchupload) != 1:
                                featcnt = featurecount(spatialid)
                            else:
                                featcnt = 0
                        else:
                            featcnt = 'None'
                            spatialid = 'None'
                            # "HUC12":HUC12,
                        if typeactval == 'Spatial Project':
                            context = {'form': form, 'formset': formset, 'subform2': subform2, 'subform3': subform3,
                                       'subform4': subform4, 'subform5': subform5, 'subform6': subform6,
                                       'subform10': subform10, 'subform11': subform11, 'subform12': subform12, 'subform13': subform13, 'authen': authen, 'LocSelect': Loc, 'allfiles': allfiles1,
                                       'spatialid': spatialid, 'prid': prid, "logonpysb": logonpysb, "prjname": prjname,
                                       "typeactval": typeactval, "Activity": Activity, "Threats": Threats,
                                       "Documentation": Documentation, "Location": Location, "WAFWA": WAFWA,
                                       "Populations": Populations, "States": States, "Counties": Counties,
                                       "Ownership": Ownership, "Part1": Part1, "Part23": Part23, "Collab": Collab, "Objectives":Objectives, "Methods":Methods, "EffectState":EffectState,
                                       "Display": 'Location', "logon": logon, "josso": josso, "subact": subact,
                                       "NotPoly": NotPoly, 'stassel': stassel,
                                           'cntssel': cntssel, 'ownssel': ownssel, 'colabssel': colabssel, "obidssel":obidssel, "mtidssel":mtidssel, "esidssel":esidssel,
                                           'thrssel': thrssel}
                        elif typeactval == 'Non-Spatial Project':
                            context = {'form': form, 'formset': formset, 'subform2': subform2, 'subform3': subform3,
                                   'subform4': subform4, 'subform5': subform5, 'subform6': subform6,
                                   'subform10': subform10, 'subform11': subform11, 'subform12': subform12, 'subform13': subform13, 'authen': authen, 'LocSelect': Loc, 'allfiles': allfiles1,
                                   'spatialid': spatialid, 'prid': prid, "logonpysb": logonpysb, "prjname": prjname,
                                   "typeactval": typeactval, "Activity": Activity, "Threats": Threats,
                                   "Documentation": Documentation, "Location": Location, "WAFWA": WAFWA,
                                   "Populations": Populations, "States": States, "Counties": Counties,
                                   "Ownership": Ownership, "Part1": Part1, "Part23": Part23, "Collab": Collab, "Objectives":Objectives, "Methods":Methods, "EffectState":EffectState,
                                   "Display": 'Location', "logon": logon, "josso": josso, "subact": subact,
                                   "NotPoly": NotPoly, 'stassel': stassel,
                                       'cntssel': cntssel, 'ownssel': ownssel, 'colabssel': colabssel, "obidssel":obidssel, "mtidssel":mtidssel, "esidssel":esidssel,
                                       'thrssel': thrssel}
                        elif typeactval == 'Non-Spatial Plan':
                            context = {'form': form, 'formset': formset, 'subform2': subform2, 'subform3': subform3,
                                   'subform4': '', 'subform5': subform5, 'subform6': subform6,
                                   'subform10': subform10, 'subform11': '', 'subform12': '', 'subform13': '', 'authen': authen, 'LocSelect': Loc, 'allfiles': allfiles1,
                                   'spatialid': spatialid, 'prid': prid, "logonpysb": logonpysb, "prjname": prjname,
                                   "typeactval": typeactval, "Activity": Activity, "Threats": Threats,
                                   "Documentation": Documentation, "Location": Location, "WAFWA": WAFWA,
                                   "Populations": Populations, "States": States, "Counties": Counties,
                                   "Ownership": Ownership, "Part1": Part1, "Part23": Part23, "Collab": Collab, "Objectives":'', "Methods":'', "EffectState":'',
                                   "Display": 'Location', "logon": logon, "josso": josso, "subact": subact,
                                   "NotPoly": NotPoly, 'stassel': stassel,
                                       'cntssel': cntssel, 'ownssel': ownssel, 'colabssel': colabssel, "obidssel":'', "mtidssel":'', "esidssel":'',
                                       'thrssel': thrssel}
                        return render(request, 'ced_main/editproject.html', context)


                    else:
                        if int(approval) == 3:
                            context = {'form': form, 'formset': formset, 'subform2': subform2, 'subform3': subform3,
                                       'subform4': subform4, 'subform5': subform5, 'subform6': subform6,
                                       'subform10': subform10, 'subform11': subform11, 'subform12': subform12, 'subform13': subform13, 'authen': authen, 'LocSelect': Loc,
                                       'allfiles': allfiles1, 'spatialid': spatialid, 'prid': prid,
                                       "logonpysb": logonpysb, "prjname": prjname, "typeactval": typeactval,
                                       "Activity": Activity, "Threats": Threats, "Documentation": Documentation,
                                       "Location": Location, "WAFWA": WAFWA, "Populations": Populations,
                                       "States": States, "Counties": Counties, "Ownership": Ownership, "Part1": Part1,
                                       "Part23": Part23, "Collab": Collab, "Objectives":Objectives, "Methods":Methods, "EffectState":EffectState, "Display": 'errorcheckdiv', "logon": logon,
                                       "josso": josso, "subact": subact, "NotPoly": NotPoly, 'stassel': stassel,
                                       'cntssel': cntssel, 'ownssel': ownssel, 'colabssel': colabssel, "obidssel":obidssel, "mtidssel":mtidssel, "esidssel":obidssel,
                                       'thrssel': thrssel}
                            return render(request, 'ced_main/readonly.html', context)
                        else:
                            context = {'form': form, 'authen': authen}
                            return render(request, 'ced_main/permission_denied.html', context)
                else:
                    context = {'form': form, 'authen': authen}
                    return render(request, 'ced_main/accept_user_agreement.html', context)
            else:

                if accepted == 'accepted' and authuser == 'Authorized':
                    if enterdata == 'dataenter':
                        if typeactval == "Project" or typeactval == "Spatial Project":
                            if int(batchupload) != 1:
                                featcnt = featurecount(spatialid)
                            else:
                                featcnt = 0
                        else:
                            featcnt = 'None'
                            spatialid = 'None'

                        context = {'form': form, 'formset': formset, 'subform2': subform2, 'subform3': subform3,
                                   'subform4': subform4, 'subform5': subform5, 'subform6': subform6,
                                   'subform10': subform10, 'subform11': subform11, 'subform12': subform12, 'subform13': subform13, 'authen': authen, 'LocSelect': Loc, 'allfiles': allfiles1,
                                   'spatialid': spatialid, 'prid': prid, "logonpysb": logonpysb, "prjname": prjname,
                                   "typeactval": typeactval, "Activity": Activity, "Threats": Threats,
                                   "Documentation": Documentation, "Location": Location, "WAFWA": WAFWA,
                                   "Populations": Populations, "States": States, "Counties": Counties,
                                   "Ownership": Ownership, "Part1": Part1, "Part23": Part23, "Collab": Collab, "Objectives":Objectives, "Methods":Methods, "EffectState":EffectState,
                                   "Display": 'Location', "logon": logon, "josso": josso, "subact": subact,
                                   "NotPoly": NotPoly, 'stassel': stassel,
                                       'cntssel': cntssel, 'ownssel': ownssel, 'colabssel': colabssel, "obidssel":obidssel, "mtidssel":mtidssel, "esidssel":obidssel,
                                       'thrssel': thrssel}
                        return render(request, 'ced_main/editproject.html', context)

                    else:
                        if int(approval) == 3:
                            context = {'form': form, 'formset': formset, 'subform2': subform2, 'subform3': subform3,
                                       'subform4': subform4, 'subform5': subform5, 'subform6': subform6,
                                       'subform10': subform10, 'subform11': subform11, 'subform12': subform12, 'subform13': subform13, 'authen': authen, 'LocSelect': Loc,
                                       'allfiles': allfiles1, 'spatialid': spatialid, 'prid': prid,
                                       "logonpysb": logonpysb, "prjname": prjname, "typeactval": typeactval,
                                       "Activity": Activity, "Threats": Threats, "Documentation": Documentation,
                                       "Location": Location, "WAFWA": WAFWA, "Populations": Populations,
                                       "States": States, "Counties": Counties, "Ownership": Ownership, "Part1": Part1,
                                       "Part23": Part23, "Collab": Collab, "Objectives":Objectives, "Methods":Methods, "EffectState":EffectState, "Display": 'errorcheckdiv', "logon": logon,
                                       "josso": josso, "subact": subact, "NotPoly": NotPoly, 'stassel': stassel,
                                       'cntssel': cntssel, 'ownssel': ownssel, 'colabssel': colabssel, "obidssel":obidssel, "mtidssel":mtidssel, "esidssel":obidssel,
                                       'thrssel': thrssel}
                            return render(request, 'ced_main/readonly.html', context)
                        else:
                            context = {'form': form, 'authen': authen}
                            return render(request, 'ced_main/permission_denied.html', context)

                else:
                    if accepted == 'accepted' and authuser == 'NotAuthorized':
                        if int(approval) == 3:
                            context = {'form': form, 'formset': formset, 'subform2': subform2, 'subform3': subform3,
                                       'subform4': subform4, 'subform5': subform5, 'subform6': subform6,
                                       'subform10': subform10, 'subform11': subform11, 'subform12': subform12, 'subform13': subform13, 'authen': authen, 'LocSelect': Loc,
                                       'allfiles': allfiles1, 'spatialid': spatialid, 'prid': prid,
                                       "logonpysb": logonpysb, "prjname": prjname, "typeactval": typeactval,
                                       "Activity": Activity, "Threats": Threats, "Documentation": Documentation,
                                       "Location": Location, "WAFWA": WAFWA, "Populations": Populations,
                                       "States": States, "Counties": Counties, "Ownership": Ownership, "Part1": Part1,
                                       "Part23": Part23, "Collab": Collab, "Objectives":Objectives, "Methods":Methods, "EffectState":EffectState, "Display": 'errorcheckdiv', "logon": logon,
                                       "josso": josso, "subact": subact, "NotPoly": NotPoly, 'stassel': stassel,
                                       'cntssel': cntssel, 'ownssel': ownssel, 'colabssel': colabssel, "obidssel":obidssel, "mtidssel":mtidssel, "esidssel":obidssel,
                                       'thrssel': thrssel}
                            return render(request, 'ced_main/readonly.html', context)
                        else:
                            context = {'form': form, 'authen': authen}
                            return render(request, 'ced_main/permission_denied.html', context)
                    else:
                        context = {'form': form, 'authen': authen}
                        return render(request, 'ced_main/accept_user_agreement.html', context)

        else:
            context = {'form': form, 'authen': authen}
            return render(request, 'ced_main/permission_denied.html', context)


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@login_required
def viewprojects(request):
    profile = request.user.username
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    accepted = checkaccept(userprofile.objects.values_list('Waiver_V2_Approved', flat=True).get(
        User_id__exact=User.objects.values_list('id', flat=True).get(username__exact=request.user)))

    table = viewprojects_table(project_info.objects.filter(Created_By__exact=profile))
    tblecnt = project_info.objects.filter(Created_By__exact=profile).count()
    RequestConfig(request).configure(table)
    context = {'viewprojects': table, 'authen': authen, 'count': tblecnt}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        if accepted == 'accepted':
            return render(request, 'ced_main/viewprojects.html', context)
        else:
            return redirect('/sgce/accept_user_agreement/')
    else:
        return render(request, 'ced_main/permission_denied.html')


@login_required
def viewprojectsicanedit(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    accepted = checkaccept(userprofile.objects.values_list('Waiver_V2_Approved', flat=True).get(
        User_id__exact=User.objects.values_list('id', flat=True).get(username__exact=request.user)))
    profile = request.user.username
    try:
        icanedit = useredits.objects.values_list('userid', flat=True).filter(
            editinguser=elidgbleusers.objects.get(username=profile))
    except:
        icanedit = []
    ican1 = []
    icnt = 0
    for ican in icanedit:
        username = User.objects.get(id=ican)
        prjscrt = project_info.objects.filter(Created_By__exact=username)
        for prjs in prjscrt:
            ican1.append(str(prjs))
            icnt = icnt + 1

    table = viewprojects_table(list(project_info.objects.filter(Project_ID__in=ican1)))
    RequestConfig(request).configure(table)
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        if accepted == 'accepted':
            context = {'viewprojects': table, 'authen': authen, 'count': icnt}
            return render(request, 'ced_main/viewprojectsicanedit.html', context)
        else:
            return redirect('/sgce/accept_user_agreement/')
    else:
        return render(request, 'ced_main/permission_denied.html')


@login_required
def viewdraftprojects(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    profile = request.user.username
    accepted = checkaccept(userprofile.objects.values_list('Waiver_V2_Approved', flat=True).get(
        User_id__exact=User.objects.values_list('id', flat=True).get(username__exact=request.user)))
    table = viewdraftprojects_table(project_info.objects.filter(Created_By__exact=profile).filter(Entry_Type=1))
    tblecnt = project_info.objects.filter(Created_By__exact=profile).filter(Entry_Type=1).count()
    RequestConfig(request).configure(table)
    context = {'viewdraftprojects': table, 'authen': authen, 'count': tblecnt}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        if accepted == 'accepted':
            return render(request, 'ced_main/viewdraftprojects.html', context)
        else:
            return redirect('/sgce/accept_user_agreement/')
    else:
        return render(request, 'ced_main/permission_denied.html')


@login_required
def viewawaitingprojects(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    profile = request.user.username
    accepted = checkaccept(userprofile.objects.values_list('Waiver_V2_Approved', flat=True).get(
        User_id__exact=User.objects.values_list('id', flat=True).get(username__exact=request.user)))
    table = viewawaitingprojects_table(project_info.objects.filter(Created_By__exact=profile).filter(Entry_Type=2))
    tblecnt = project_info.objects.filter(Created_By__exact=profile).filter(Entry_Type=2).count()
    RequestConfig(request).configure(table)
    context = {'viewawaitingprojects': table, 'authen': authen, 'count': tblecnt}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        if accepted == 'accepted':
            return render(request, 'ced_main/viewawaitingprojects.html', context)
        else:
            return redirect('/sgce/accept_user_agreement/')
    else:
        return render(request, 'ced_main/permission_denied.html')


@login_required
def viewapprovedprojects(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    accepted = checkaccept(userprofile.objects.values_list('Waiver_V2_Approved', flat=True).get(
        User_id__exact=User.objects.values_list('id', flat=True).get(username__exact=request.user)))
    profile = request.user.username
    table = viewapprovedprojects_table(project_info.objects.filter(Created_By__exact=profile).filter(Entry_Type=3))
    tblecnt = project_info.objects.filter(Created_By__exact=profile).filter(Entry_Type=3).count()
    RequestConfig(request).configure(table)
    context = {'viewapprovedprojects': table, 'authen': authen, 'count': tblecnt}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        if accepted == 'accepted':
            return render(request, 'ced_main/viewapprovedprojects.html', context)
        else:
            return redirect('/sgce/accept_user_agreement/')
    else:
        return render(request, 'ced_main/permission_denied.html')


@login_required
def viewallprojects(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    accepted = checkaccept(userprofile.objects.values_list('Waiver_V2_Approved', flat=True).get(
        User_id__exact=User.objects.values_list('id', flat=True).get(username__exact=request.user)))
    profile = request.user.username

    table = viewallprojects_table(project_info.objects.all())
    RequestConfig(request).configure(table)
    context = {'viewallprojects': table, 'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        if authen == 'authenadmin':
            return render(request, 'ced_main/viewallprojects.html', context)
        else:
            return render(request, 'ced_main/permission_denied.html')
    else:
        return render(request, 'ced_main/permission_denied.html')


@login_required
def viewapprovalprojects(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    accepted = checkaccept(userprofile.objects.values_list('Waiver_V2_Approved', flat=True).get(
        User_id__exact=User.objects.values_list('id', flat=True).get(username__exact=request.user)))
    profile = request.user.username
    table = viewapprovalprojects_table(
        project_info.objects.filter(Approving_Official=request.user.username).filter(Entry_Type=2))
    tblecnt = project_info.objects.filter(Approving_Official=request.user.username).filter(Entry_Type=2).count()
    RequestConfig(request).configure(table)
    context = {'viewapprovalprojects': table, 'authen': authen, 'count': tblecnt}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        if authen == 'authenadmin' or authen == 'authenapp':
            return render(request, 'ced_main/viewapprovalprojects.html', context)
        else:
            return render(request, 'ced_main/permission_denied.html')
    else:
        return render(request, 'ced_main/permission_denied.html')


@login_required
def viewuserprojects(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    accepted = checkaccept(userprofile.objects.values_list('Waiver_V2_Approved', flat=True).get(
        User_id__exact=User.objects.values_list('id', flat=True).get(username__exact=request.user)))
    profile = request.user.username
    table = viewuserprojects_table(project_info.objects.filter(Approving_Official=request.user.username))
    tblecnt = project_info.objects.filter(Approving_Official=request.user.username).count()
    RequestConfig(request).configure(table)
    context = {'viewuserprojects': table, 'authen': authen, 'count': tblecnt}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        if authen == 'authenadmin' or authen == 'authenapp':
            return render(request, 'ced_main/viewuserprojects.html', context)
        else:
            return render(request, 'ced_main/permission_denied.html')
    else:
        return render(request, 'ced_main/permission_denied.html')

def permission_denied(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/permission_denied.html', context)
    else:
        return render(request, 'ced_main/permission_denied.html')


def accept_user_agreement(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/accept_user_agreement.html', context)
    else:
        return render(request, 'ced_main/accept_user_agreement.html')


def lcmap_sb_down(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/lcmap_sb_down.html', context)
    else:
        return render(request, 'ced_main/lcmap_sb_down.html')


def spatialhelp(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/spatialhelp.html', context)
    else:
        return render(request, 'ced_main/spatialhelp.html')

def helpvideo(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/helpvideo.html', context)
    else:
        return render(request, 'ced_main/helpvideo.html')

def delete_success(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/delete_success.html', context)
    else:
        return render(request, 'ced_main/permission_denied.html')

def mark_for_deletion(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/mark_for_deletion.html', context)
    else:
        return render(request, 'ced_main/permission_denied.html')

def permanent_deletion(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/permanent_deletion.html', context)
    else:
        return render(request, 'ced_main/permission_denied.html')

def project_not_exists(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/project_not_exists.html', context)
    else:
        return render(request, 'ced_main/permission_denied.html')

def project_not_exists_temp(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/project_not_exists_temp.html', context)
    else:
        return render(request, 'ced_main/permission_denied.html')

@login_required
def viewbatchapprovalprojects(request):
    siteurl = request.build_absolute_uri()
    siteurl1 = siteurl.split("/")
    siteurl2 = siteurl1[0] + "//" + siteurl1[2]

    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    AppProjectsFormSet = modelformset_factory(project_info, extra=0, form=batch_approve_form)
    alleffortsreturned = project_info.objects.values_list('Project_ID', flat=True).filter(
        Approving_Official=request.user.username).filter(Entry_Type=2)

    eff1 = []
    count = 0

    try:
        for eff in alleffortsreturned:
            eff1.append(eff)
            count = count + 1
            if count == 100:
                break
    except:
        test = "test"

    eff2 = project_info.objects.filter(Project_ID__in=eff1)

    formset = AppProjectsFormSet(queryset=eff2)
    # A HTTP POST?
    if request.method == 'POST':
        i = 0
        prjcntlist = []
        prjcount = project_info.objects.values_list('Project_ID', flat=True).filter(
            Approving_Official=request.user.username).filter(Entry_Type=2)
        for prjc in prjcount:
            prjcntlist.append([i, int(prjc)])
            i = i + 1

        emaillist = []

        for prjclist in prjcntlist:
            appid = 'form-' + str(prjclist[0]) + '-ApprovePrj'
            if appid in request.POST:
                emailadded = 0
                Updating_User = project_info.objects.values_list('Updating_User', flat=True).filter(
                    Project_ID=prjclist[1])
                Updating_User = str(Updating_User)
                Updating_User = Updating_User.split("'")
                Updating_User = Updating_User[1]
                for elist in emaillist:
                    if elist == str(Updating_User):
                        emailadded = 1
                if emailadded == 0:
                    emaillist.append(str(Updating_User))

                Created_By = project_info.objects.values_list('Created_By', flat=True).filter(Project_ID=prjclist[1])
                Created_By = str(Created_By)
                Created_By = Created_By.split("'")
                Created_By = Created_By[1]
                emailadded1 = 0
                for elist1 in emaillist:
                    if elist1 == str(Updating_User):
                        emailadded1 = 1
                if emailadded1 == 0:
                    emaillist.append(str(Created_By))

                objsave = project_info.objects.get(Project_ID=prjclist[1])
                objsave.Entry_Type = 3
                objsave.Date_Approved = now
                objsave.save()

        Subject = "You have had multiple projects that have stamped approved via the batch approval process by " + request.user.first_name + " " + request.user.last_name
        Message = "The approving official " + request.user.first_name + " " + request.user.last_name + " (username: " + request.user.username + ") has approved projects via the batch approval mode. Please login to the CED (" + siteurl2 + " /sgce/) and search for your approved projects to see the full list."

        From = DEFAULT_FROM_EMAIL
        qresult = []

        for elist2 in emaillist:
            qresult.append(User.objects.values_list('email').get(username=elist2))
        j = 0
        To = ""
        for rst in qresult:
            rst = str(rst)[3:]
            rst = str(rst)[:-3]
            if j == 0:
                To = To + str(rst)
                j = 1
            else:
                To = To + ", " + str(rst)
        send_mail(Subject, Message, From, [To], fail_silently=False)
        AppProjectsFormSet = modelformset_factory(project_info, extra=0, form=batch_approve_form)
        alleffortsreturned = project_info.objects.values_list('Project_ID', flat=True).filter(
            Approving_Official=request.user.username).filter(Entry_Type=2)

        eff1 = []
        count = 0

        try:
            for eff in alleffortsreturned:
                eff1.append(eff)
                count = count + 1
                if count == 1000:
                    break
        except:
            test = "test"

        eff2 = project_info.objects.filter(Project_ID__in=eff1)

        formset = AppProjectsFormSet(queryset=eff2)
        context = {'authen': authen, 'formset': formset, 'approved': 'approved'}
        return render(request, 'ced_main/viewbatchapprovalprojects.html', context)
    else:
        # if request.user.is_authenticated(): Pythoon 2.7
        if request.user.is_authenticated:
            if authen == 'authenadmin' or authen == 'authenapp':
                context = {'authen': authen, 'formset': formset}
                return render(request, 'ced_main/viewbatchapprovalprojects.html', context)
            else:
                return render(request, 'ced_main/permission_denied.html')
        else:
            return render(request, 'ced_main/permission_denied.html')


def sgcedsummary(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/sgcedsummary.html', context)
    else:
        return render(request, 'ced_main/permission_denied.html')


def emailcedusers(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    AllUserlist = []
    AppOffUserlist = []
    ApprovedUserlist = []
    AdminUserlist = []
    DemoUserlist = []
    IncompleteUserlist = []
    Agencylistf = []
    Officelistf = []
    conoffice = userprofile.objects.values_list('Field_Office', flat=True).get(
        User_id__exact=User.objects.values_list('id', flat=True).get(username__exact=request.user))
    context = {'authen': authen}
    if request.method == 'POST':
        if conoffice == 'Congress':
            return redirect('/sgce/readonly/')

        form = emailcedusers_Form(request.POST)
        if form.is_valid():
            useremails = []
            for emails in request.POST.getlist('GroupUsers'):

                if emails == 'AllUsers':
                    AllUserlist = getusers(emails, 'Group')

                if emails == 'Admin':
                    AdminUserlist = getusers(emails, 'Group')

                if emails == 'Approve':
                    AppOffUserlist = getusers(emails, 'Group')

                if emails == 'ApprovedUsers':
                    ApprovedUserlist = getusers(emails, 'Group')

                if emails == 'DemoUsers':
                    DemoUserlist = getusers(emails, 'Group')

                if emails == 'IncompleteUsers':
                    IncompleteUserlist = getusers(emails, 'Group')

            for emails in request.POST.getlist('AgencyUsers'):

                Agencylist = getusers(emails, 'Agency')
                try:
                    for agn in Agencylist:
                        Agencylistf.append(agn)
                except:
                    test = "test"

            for emails in request.POST.getlist('OfficeUsers'):
                Officelist = getusers(emails, 'Office')
                try:
                    for off in Officelist:
                        Officelistf.append(off)
                except:
                    test = "test"

            induseremails = []
            for emails in request.POST.getlist('CEDUsers'):
                emailuser = User.objects.values_list('email', flat=True).get(username=emails)
                induseremails.append(emailuser)

            for sub in request.POST.getlist('Subject'):
                subject = sub

            for body in request.POST.getlist('Email_Body'):
                emailbody = body

            From = DEFAULT_FROM_EMAIL

            for aul in AllUserlist:
                eexistscheck = 0
                for ue in useremails:
                    if ue == aul:
                        eexistscheck = 1
                if eexistscheck == 0:
                    useremails.append(aul)

            for adul in AdminUserlist:
                eexistscheck = 0
                for ue in useremails:
                    if ue == adul:
                        eexistscheck = 1
                if eexistscheck == 0:
                    useremails.append(adul)

            for apoul in AppOffUserlist:
                eexistscheck = 0
                for ue in useremails:
                    if ue == apoul:
                        eexistscheck = 1
                if eexistscheck == 0:
                    useremails.append(apoul)

            for apul in ApprovedUserlist:
                eexistscheck = 0
                for ue in useremails:
                    if ue == apul:
                        eexistscheck = 1
                if eexistscheck == 0:
                    useremails.append(apul)

            for dul in DemoUserlist:
                eexistscheck = 0
                for ue in useremails:
                    if ue == dul:
                        eexistscheck = 1
                if eexistscheck == 0:
                    useremails.append(dul)

            for iul in IncompleteUserlist:
                eexistscheck = 0
                for ue in useremails:
                    if ue == iul:
                        eexistscheck = 1
                if eexistscheck == 0:
                    useremails.append(iul)

            for alf in Agencylistf:
                eexistscheck = 0
                for ue in useremails:
                    if ue == alf:
                        eexistscheck = 1
                if eexistscheck == 0:
                    useremails.append(alf)

            for olf in Officelistf:
                eexistscheck = 0
                for ue in useremails:
                    if ue == olf:
                        eexistscheck = 1
                if eexistscheck == 0:
                    useremails.append(olf)

            for iue in induseremails:
                eexistscheck = 0
                for ue in useremails:
                    if ue == iue:
                        eexistscheck = 1
                if eexistscheck == 0:
                    useremails.append(iue)

            send_mail(subject, emailbody, From, useremails, fail_silently=False)

            return render(request, 'ced_main/emailceduserssuccess.html', context)
        else:
            context = {'authen': authen, 'form': form}
            return render(request, 'ced_main/emailcedusers.html', context)
    else:
        form = emailcedusers_Form()
        # if request.user.is_authenticated(): Pythoon 2.7
        if request.user.is_authenticated:
            if authen == 'authenadmin':
                context = {'authen': authen, 'form': form}
                return render(request, 'ced_main/emailcedusers.html', context)
            else:
                return render(request, 'ced_main/permission_denied.html')
        else:
            return render(request, 'ced_main/permission_denied.html')


@login_required
def emailceduserssuccess(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    context = {'authen': authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        if authen == 'authenadmin':
            return render(request, 'ced_main/emailceduserssuccess.html', context)
        else:
            return render(request, 'ced_main/permission_denied.html')
    else:
        return render(request, 'ced_main/permission_denied.html')


@login_required
def fwsquery(request):
    siteurl = request.build_absolute_uri()
    siteurl1 = siteurl.split("/")
    siteurl2 = siteurl1[0] + "//" + siteurl1[2]

    profile = request.user
    userAgency = userprofile.objects.values_list('Agency', flat=True).get(User_id=profile)
    userOffice = userprofile.objects.values_list('Field_Office', flat=True).get(User_id=profile)
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    username1 = request.user.username
    context = {'authen': authen, 'showlogin': 'True'}
    if request.method == 'POST':
        form = fwsquery_Form(request.POST)
        if form.is_valid():

            uq = project_info.objects.all()
            uq = uq.filter(Entry_Type=3)
            uq = uq.filter(TypeAct='Project')
            uq = uq.filter(Project_Status=3)

            impi = []
            impinfo = gettablesfwsii(1)
            for ii in impinfo:
                impi.append(ii)
            uq = uq.filter(Project_ID__in=impi)

            # Get Query Type.
            QuTy = ''
            for QT in request.POST.getlist('QueryType'):
                QuTy = int(QT)

            # Filter by States
            Stat = []
            Statcnt = 0
            statenm = ''
            for Sta in request.POST.getlist('State'):
                if Sta != "":
                    Sta1 = int(Sta)
                    statenm = state.objects.values_list('State', flat=True).get(id=str(Sta1)) + "_"
                    stateval = gettablesfws(Sta1)
                    for St in stateval:
                        Stat.append(St)
                    Statcnt = 1
            if Statcnt == 1:
                uq = uq.filter(Project_ID__in=Stat).order_by('Project_Name')

            # Filter by WAFWA Zones
            WAFW = []
            WAFWcnt = 0
            wafwanm = ''
            fwswafwa = 0
            for WAF in request.POST.getlist('WAFWA_Zone'):
                if WAF != "":
                    WAF1 = int(WAF)
                    fwswafwa = int(WAF)
                    wafwanm = "WAFWA_" + wafwa_zone_values.objects.values_list('WAFWA_Zone', flat=True).get(
                        id=str(WAF1)) + "_"
                    wafwaval = gettablesfwswa(WAF1)
                    for WA in wafwaval:
                        WAFW.append(WA)
                    WAFWcnt = 1

            if WAFWcnt == 1:
                uq = uq.filter(Project_ID__in=WAFW)

            # Filter by Threats
            thrt = []
            thrtcnt = 0
            threatnm = ''
            fwsthreat = ""
            for sagethrt in request.POST.getlist('Threat'):
                if sagethrt != "":
                    sagethrt1 = int(sagethrt)
                    threatnm = "Threat_" + threat_values.objects.values_list('Threats', flat=True).get(
                        id=str(sagethrt1))
                    fwsthreat = threat_values.objects.values_list('Threats', flat=True).get(id=str(sagethrt1))
                    sagethrtval = gettablesfwsth(sagethrt1)
                    for saget in sagethrtval:
                        thrt.append(saget)
                    thrtcnt = 1
            threatnm = threatnm.replace(" / ", "")
            threatnm = threatnm.replace(" / ", "")
            threatnm = threatnm.replace("Noxious Weeds Annual Grasses", "Noxious Weeds")

            # Filter by FWS Response
            uqnew = []
            FWSRcnt = 0
            FWSRnm = ''
            if fwsthreat == "Noxious Weeds /  Annual Grasses":
                fwsthreat1 = "Noxious Weeds / Annual Grasses"
            else:
                fwsthreat1 = fwsthreat
            for FWS in request.POST.getlist('Response'):
                if FWS != "":
                    for fwsuq in uq:
                        FWSRval = fwsreview.objects.values_list('Service_Assessment', flat=True).filter(
                            Project_ID=str(fwsuq)).filter(Threat=str(fwsthreat1))
                        FWcnt = 0
                        for FW in FWSRval:
                            FWSRval = str(FW)[0:1]
                            try:
                                intfw = int(FWSRval)
                            except:
                                intfw = 0

                            if (int(FWS) == 1 or int(FWS) == 3) and intfw == 1:
                                uqnew.append(int(str(fwsuq)))
                                FWSRcnt = 1
                            elif (int(FWS) == 2 or int(FWS) == 3) and intfw == 2:
                                uqnew.append(int(str(fwsuq)))
                                FWSRcnt = 1
                            FWcnt = FWcnt + 1

                        if int(FWS) == 4 and FWcnt == 0:
                            uqnew.append(int(str(fwsuq)))
                            FWSRcnt = 1

                uqnewcnt = 0
                for uqcnt in uqnew:
                    uqnewcnt = uqnewcnt + 1

                if uqnewcnt == 0:
                    FWSRcnt = 1
                    uqnew.append(1)

            if FWSRcnt == 1:
                uq = uq.filter(Project_ID__in=uqnew)

            if thrtcnt == 1:
                uq = uq.filter(Project_ID__in=thrt)

            for SD in request.POST.getlist('First_Date_day'):
                StrtD = SD

            for SM in request.POST.getlist('First_Date_month'):
                StrtM = SM

            for SY in request.POST.getlist('First_Date_year'):
                StrtM = SY

            for FD in request.POST.getlist('Second_Date_day'):
                FnshD = FD

            for FM in request.POST.getlist('Second_Date_month'):
                FnshM = FM

            for FY in request.POST.getlist('Second_Date_year'):
                FnshM = FY

            strtdate = str(SY) + "-" + str(SM) + "-" + str(SD) + " 23:59:59"
            try:
                fnshdate = str(FY) + "-" + str(FM) + "-" + str(FD) + " 23:59:59"
            except:
                test = 'test'

            for DE in request.POST.getlist('DateEqu'):
                if int(DE) == 1:
                    uq = uq.filter(Date_Approved__lte=strtdate)
                if int(DE) == 2:
                    uq = uq.filter(Date_Approved__gte=strtdate)
                if int(DE) == 3:
                    uq = uq.filter(Date_Approved__range=[strtdate, fnshdate])

            cnt = 0
            for u in uq:
                cnt = cnt + 1

            # Sort by the metrics

            metlist = []
            metvals = ['TotalAcres', 'TotalMiles', 'TotalEquids', 'TotalNumberBirds', 'TotalNumberRemoved']
            for uq2 in uq:
                for met1 in metvals:

                    metricvalue = -9999
                    metrictype = ""
                    try:
                        metricvalue = metrics.objects.values_list(str(met1), flat=True).get(Project_ID=str(uq2))
                        if int(metricvalue) > 0:
                            metrictype = met1
                            break
                    except:
                        metricvalue = -9999
                        metrictype = ""
                metlistf = [str(uq2), str(metrictype), float(metricvalue)]
                metlist.append(metlistf)

            metvalssort1 = sorted(metlist, key=lambda metl: metl[1])
            metvalssort = sorted(metvalssort1, key=lambda metl: metl[2], reverse=True)
            uq3 = []

            for metv in metvalssort:
                uq3.append(int(metv[0]))

            uq = uq.order_by('Project_ID')
            table = viewprojectid_table(uq)
            RequestConfig(request).configure(table)

            outputfshort = ""
            DataDown = 'False'

            if 'exportcsv' in request.POST:
                rowmax = 0
                colmax = 0
                now1 = str(now)[0:18]
                now2 = now1.replace(" ", "_")
                nowf = now2.replace(":", "-")
                if QuTy == 2:
                    filenm = username1 + "_" + statenm + wafwanm + threatnm + '_FWS_Refined_Query_' + str(
                        nowf) + '.xlsx'
                else:
                    filenm = username1 + "_" + statenm + wafwanm + threatnm + '_FWS_Phased_Assessment_' + str(
                        nowf) + '.xlsx'
                filenm = filenm.replace(" ", "_")
                #TODO
                filep = 'ced_main/images/created_docs/' + filenm
                outputf = os.path.join(STATIC_DIR, filep)
                outputfshort = siteurl2 + '/static/ced_main/images/created_docs/' + filenm

                workbook = xlsxwriter.Workbook(outputf, {'strings_to_numbers': True})
                if QuTy == 2:
                    worksheet = workbook.add_worksheet('FWS Refined Query')
                else:
                    worksheet = workbook.add_worksheet('FWS Phased Assessment')

                worksheet.freeze_panes(1, 2)

                row = 0
                col = 0

                formatbold = workbook.add_format()
                formatbold.set_bold()

                formatwrapeven = workbook.add_format()
                formatwrapeven.set_text_wrap()
                formatwrapeven.set_align('vcenter')
                formatwrapeven.set_border(1)

                formatwrapodd = workbook.add_format()
                formatwrapodd.set_text_wrap()
                formatwrapodd.set_align('vcenter')
                formatwrapodd.set_bg_color('#D8D8D8')
                formatwrapodd.set_border(1)

                formatwrapevenlink = workbook.add_format()
                formatwrapevenlink.set_text_wrap()
                formatwrapevenlink.set_align('vcenter')
                formatwrapevenlink.set_border(1)
                formatwrapevenlink.set_underline()
                formatwrapevenlink.set_font_color('blue')

                formatwrapoddlink = workbook.add_format()
                formatwrapoddlink.set_text_wrap()
                formatwrapoddlink.set_align('vcenter')
                formatwrapoddlink.set_bg_color('#D8D8D8')
                formatwrapoddlink.set_border(1)
                formatwrapoddlink.set_underline()
                formatwrapoddlink.set_font_color('blue')

                formatread = workbook.add_format()
                formatread.set_bg_color('#81BEF7')
                formatread.set_bold()
                formatread.set_border(1)

                formatwrite = workbook.add_format()
                formatwrite.set_bg_color('#F5A9A9')
                formatwrite.set_bold()
                formatwrite.set_border(1)

                worksheet.set_column(1, 2, 40)
                worksheet.set_column(3, 4, 20)
                worksheet.set_column(5, 7, 40)
                worksheet.set_column(8, 9, 20)
                worksheet.set_column(10, 10, 40)
                worksheet.set_column(11, 12, 20)
                worksheet.set_column(13, 13, 60)
                worksheet.set_column(14, 26, 40)
                worksheet.set_column(27, 28, 70)
                worksheet.set_column(29, 29, 40)

                header = "Effort ID,Effort Name,Effort Link,WAFWA Zone,Threat,Population,Activity,SubActivity,Metric,Metric Value,Objectives,Start Date,Finish Date,Explain Activity Effectiveness,Doc 1 Name,Doc 1 File Type,Doc 1 Description,Doc 2 Name,Doc 2 File Type,Doc 2 Description,Doc 3 Name,Doc 3 File Type,Doc 3 Description,Doc 4 Name,Doc 4 File Type,Doc 4 Description,Additional Docs Available,Does the Service agree with the self-reported effectiveness assessment?,Explain Service Assessment (Required Based on Effectiveness Assessment),Name of Certifier"
                headers = header.split(",")

                for head in headers:
                    if int(col) < 27:
                        worksheet.write(row, col, head, formatread)
                    else:
                        if QuTy == 2:
                            worksheet.write(row, col, head, formatread)
                        else:
                            worksheet.write(row, col, head, formatwrite)
                    col += 1

                if fwswafwa == 0:
                    fwswafwalist = ['1', '2', '3', '4', '5', '6', '7']
                else:
                    fwswafwalist = [str(fwswafwa)]

                if fwsthreat == "":
                    fwsthreatlist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
                else:
                    fwsthreatlist = [str(sagethrt1)]

                for fwswaf in fwswafwalist:
                    for fwsthrt in fwsthreatlist:
                        for uq1 in uq3:
                            Include = 0
                            Includew = 0

                            # Check if wafwa exists for selected effort
                            try:
                                checkvalw = wafwa_info.objects.filter(Project_ID=str(uq1)).filter(
                                    WAFWA_Value=str(fwswaf))
                                checkcntw = 0

                                for chckvw in checkvalw:
                                    checkcntw = 1
                                if checkcntw == 1:
                                    Includew = 1
                                    WAF1 = fwswaf
                                else:
                                    Includew = 0
                            except:
                                Includew = 0

                            # Check if threat exists for selected effort
                            try:
                                checkval = threats.objects.filter(Project_ID=str(uq1)).filter(Threat=str(fwsthrt))
                                checkcnt = 0

                                for chckv in checkval:
                                    checkcnt = 1
                                if checkcnt == 1:
                                    Include = 1
                                    fwsthreat = threat_values.objects.values_list('Threats', flat=True).get(
                                        id=str(fwsthrt))
                                else:
                                    Include = 0
                            except:
                                Include = 0

                            if Include == 1 and Includew == 1:
                                row += 1
                                if row % 2 == 0:
                                    formatwrap = formatwrapeven
                                    formatwraplink = formatwrapevenlink
                                else:
                                    formatwrap = formatwrapodd
                                    formatwraplink = formatwrapoddlink

                                line = ""
                                # Add the effort ID
                                col = 0

                                worksheet.write(row, col, str(uq1), formatwrap)
                                # Add the effort name
                                prjname = project_info.objects.values_list('Project_Name', flat=True).get(
                                    Project_ID=str(uq1))
                                col += 1
                                worksheet.write_url(row, col, str(prjname), formatwrap)
                                # Add the effort link
                                link = siteurl2 + '/sgce/redirectpg/?PRJID=' + str(uq1)
                                col += 1
                                worksheet.write(row, col, str(link), formatwraplink, str(link))
                                # Add WAFWA Zone
                                col += 1
                                worksheet.write(row, col, str(WAF1), formatwrap)
                                # Add Threat
                                col += 1
                                worksheet.write(row, col, str(fwsthreat), formatwrap)
                                # Add Population
                                sagepopvals = population_info.objects.values_list('Population_Value', flat=True).filter(
                                    Project_ID=str(uq1))
                                sagepops = ""
                                scnt = 0

                                for sagep in sagepopvals:
                                    if sagep == None or sagep == "" or sagep == 'None':
                                        sagepops = "None listed"
                                    else:
                                        sagepop = population_values.objects.values_list('Pop_Name', flat=True).get(
                                            id=str(sagep))
                                        if scnt == 0:
                                            sagepops = str(sagepops) + str(sagepop)
                                        else:
                                            sagepops = str(sagepops) + ", " + str(sagepop)
                                    scnt = 1
                                col += 1

                                worksheet.write(row, col, str(sagepops), formatwrap)
                                # Add the activity
                                try:
                                    actvalue = str('Activity')
                                    act = project_info.objects.values_list(actvalue, flat=True).get(Project_ID=str(uq1))
                                except:
                                    act = ""
                                col += 1
                                worksheet.write(row, col, str(act), formatwrap)

                                # Add the subactivity
                                try:
                                    sa = project_info.objects.values_list('SubActivity', flat=True).get(
                                        Project_ID=str(uq1))
                                except:
                                    sa = ""
                                col += 1
                                worksheet.write(row, col, str(sa), formatwrap)

                                # Add the metrics
                                metvals = ['TotalAcres', 'TotalMiles', 'TotalEquids', 'TotalNumberBirds',
                                           'TotalNumberRemoved']
                                for met in metvals:
                                    metricvalue = -9999
                                    metrictype = ""
                                    try:
                                        metricvalue = metrics.objects.values_list(str(met), flat=True).get(
                                            Project_ID=str(uq1))
                                        if metricvalue > 0:
                                            metrictype = met
                                            break
                                    except:
                                        metricvalue = -9999
                                        metrictype = ""
                                col += 1

                                worksheet.write(row, col, str(metrictype), formatwrap)
                                col += 1

                                worksheet.write(row, col, str(metricvalue), formatwrap)

                                # Add the objectives
                                try:
                                    ob1 = project_info.objects.values_list('Objectives_Desc', flat=True).get(
                                        Project_ID=str(uq1))
                                    ob = "%s" % ob1
                                    ob = str(ob)
                                    ob = ob.replace("\r\n", " ")
                                except:
                                    ob = ""
                                col += 1
                                worksheet.write(row, col, str(ob), formatwrap)

                                # Add the start date
                                try:
                                    sd = implementation_info.objects.values_list('Start_Date', flat=True).get(
                                        Project_ID=str(uq1))
                                except:
                                    sd = ""
                                col += 1
                                worksheet.write(row, col, str(sd), formatwrap)

                                # Add the finish date
                                try:
                                    fd = implementation_info.objects.values_list('Finish_Date', flat=True).get(
                                        Project_ID=str(uq1))
                                except:
                                    fd = ""
                                col += 1
                                worksheet.write(row, col, str(fd), formatwrap)

                                # Add Effective_Explained
                                try:
                                    effexp1 = implementation_info.objects.values_list('Effective_Explained',
                                                                                      flat=True).get(
                                        Project_ID=str(uq1))
                                    effexp = "%s" % effexp1
                                    effexp = str(effexp)
                                    effexp = effexp.replace(",", ";")
                                    effexp = effexp.replace("\r\n", " ")
                                except:
                                    effexp = ""
                                col += 1
                                worksheet.write(row, col, str(effexp), formatwrap)

                                ### Add Documentation
                                try:
                                    docs = documentation.objects.values_list('id', flat=True).filter(
                                        Project_ID=str(uq1))
                                except:
                                    docs = []
                                doccnt = 0
                                ft1 = ""
                                fd1 = ""
                                fn1 = ""
                                fsb1 = ""
                                ft2 = ""
                                fd2 = ""
                                fn2 = ""
                                fsb2 = ""
                                ft3 = ""
                                fd3 = ""
                                fn3 = ""
                                fsb3 = ""
                                ft4 = ""
                                fd4 = ""
                                fn4 = ""
                                fsb4 = ""

                                for doc in docs:
                                    doccnt = doccnt + 1
                                    if doccnt == 1:
                                        try:
                                            fd11 = documentation.objects.values_list('Document_Description',
                                                                                     flat=True).get(id=int(doc))
                                            fd1 = "%s" % fd11
                                        except:
                                            fd1 = ""

                                        if fd1 != 'Spatial data from Batch Upload':

                                            try:
                                                fn11 = documentation.objects.values_list('Document_Name',
                                                                                         flat=True).get(id=int(doc))
                                                fn1 = "%s" % fn11
                                            except:
                                                fn1 = ""
                                            col += 1
                                            worksheet.write(row, col, str(fn1), formatwrap)

                                            try:
                                                ft1 = documentation.objects.values_list('File_Type', flat=True).get(
                                                    id=int(doc))
                                            except:
                                                ft1 = ""
                                            col += 1
                                            worksheet.write(row, col, str(ft1), formatwrap)
                                            col += 1
                                            worksheet.write(row, col, str(fd1), formatwrap)
                                        else:
                                            fd1 = ""
                                            doccnt = 0
                                    elif doccnt == 2:
                                        try:
                                            fd21 = documentation.objects.values_list('Document_Description',
                                                                                     flat=True).get(id=int(doc))
                                            fd2 = "%s" % fd21
                                        except:
                                            fd2 = ""

                                        if fd2 != 'Spatial data from Batch Upload':
                                            try:
                                                fn21 = documentation.objects.values_list('Document_Name',
                                                                                         flat=True).get(id=int(doc))
                                                fn2 = "%s" % fn21
                                            except:
                                                fn2 = ""
                                            col += 1
                                            worksheet.write(row, col, str(fn2), formatwrap)
                                            try:
                                                ft2 = documentation.objects.values_list('File_Type', flat=True).get(
                                                    id=int(doc))
                                            except:
                                                ft2 = ""
                                            col += 1
                                            worksheet.write(row, col, str(ft2), formatwrap)
                                            col += 1
                                            worksheet.write(row, col, str(fd2), formatwrap)

                                        else:
                                            fd2 = ""
                                            doccnt = 1
                                    elif doccnt == 3:
                                        try:
                                            fd31 = documentation.objects.values_list('Document_Description',
                                                                                     flat=True).get(id=int(doc))
                                            fd3 = "%s" % fd31
                                        except:
                                            fd3 = ""

                                        if fd3 != 'Spatial data from Batch Upload':
                                            try:
                                                fn31 = documentation.objects.values_list('Document_Name',
                                                                                         flat=True).get(id=int(doc))
                                                fn3 = "%s" % fn31
                                            except:
                                                fn3 = ""
                                            col += 1
                                            worksheet.write(row, col, str(fn3), formatwrap)

                                            try:
                                                ft3 = documentation.objects.values_list('File_Type', flat=True).get(
                                                    id=int(doc))
                                            except:
                                                ft3 = ""
                                            col += 1
                                            worksheet.write(row, col, str(ft3), formatwrap)
                                            col += 1
                                            worksheet.write(row, col, str(fd3), formatwrap)

                                        else:
                                            fd3 = ""
                                            doccnt = 2
                                    elif doccnt == 4:
                                        try:
                                            fd41 = documentation.objects.values_list('Document_Description',
                                                                                     flat=True).get(id=int(doc))
                                            fd4 = "%s" % fd41
                                        except:
                                            fd4 = ""

                                        if fd4 != 'Spatial data from Batch Upload':
                                            try:
                                                fn41 = documentation.objects.values_list('Document_Name',
                                                                                         flat=True).get(id=int(doc))
                                                fn4 = "%s" % fn41
                                            except:
                                                fn4 = ""
                                            col += 1
                                            worksheet.write(row, col, str(fn4), formatwrap)
                                            try:
                                                ft4 = documentation.objects.values_list('File_Type', flat=True).get(
                                                    id=int(doc))
                                            except:
                                                ft4 = ""
                                            col += 1
                                            worksheet.write(row, col, str(ft4), formatwrap)
                                            col += 1
                                            worksheet.write(row, col, str(fd4), formatwrap)

                                        else:
                                            fd4 = ""
                                            doccnt = 3
                                    elif doccnt == 5:
                                        try:
                                            fd4 = documentation.objects.values_list('Document_Description',
                                                                                    flat=True).get(id=int(doc))
                                        except:
                                            fd4 = ""

                                        if fd4 == 'Spatial data from Batch Upload' or fd4 == "":
                                            doccnt = 4

                                    if doccnt > 4:
                                        lclink = project_info.objects.values_list('LCMItem', flat=True).get(
                                            Project_ID=str(uq1))
                                        sblink = "https://www.sciencebase.gov/catalog/folder/" + str(lclink)
                                        col += 1
                                        worksheet.write(row, col, str(sblink), formatwraplink)

                                if doccnt == 0:
                                    col += 1
                                    i = col
                                    i1 = col + 13
                                    for i in range(i, i1):
                                        worksheet.write(row, i, "", formatwrap)
                                    col += 12
                                elif doccnt == 1:
                                    col += 1
                                    i = col
                                    i1 = col + 10
                                    for i in range(i, i1):
                                        worksheet.write(row, i, "", formatwrap)
                                    col += 9
                                elif doccnt == 2:
                                    col += 1
                                    i = col
                                    i1 = col + 7
                                    for i in range(i, i1):
                                        worksheet.write(row, i, "", formatwrap)
                                    col += 6
                                elif doccnt == 3:
                                    col += 1
                                    i = col
                                    i1 = col + 4
                                    for i in range(i, i1):
                                        worksheet.write(row, i, "", formatwrap)
                                    col += 3
                                elif doccnt == 4:
                                    col += 1
                                    i = col
                                    i1 = col + 1
                                    for i in range(i, i1):
                                        worksheet.write(row, i, "", formatwrap)
                                    col += 0

                                col += 1
                                if QuTy == 2:

                                    FWSRval = fwsreview.objects.values_list('Service_Assessment', flat=True).filter(
                                        Project_ID=str(uq1)).filter(Threat=str(fwsthreat))
                                    FSWSA = ''
                                    for FWSRv in FWSRval:
                                        FSWSA = FWSRv

                                    worksheet.write(row, col, str(FSWSA), formatwrap)
                                    FWSRexp = fwsreview.objects.values_list('Service_Assessment_Explained',
                                                                            flat=True).filter(
                                        Project_ID=str(uq1)).filter(Threat=str(fwsthreat))

                                    FSWSAE = str(FWSRexp)
                                    FSWSAE = FSWSAE.replace('/xa0', '')
                                    FSWSAE = FSWSAE.replace("[u'", "")
                                    FSWSAE = FSWSAE.replace("']", "")
                                    col += 1

                                    worksheet.write(row, col, FSWSAE, formatwrap)

                                    FWSRnam = fwsreview.objects.values_list('Certifier_Name', flat=True).filter(
                                        Project_ID=str(uq1)).filter(Threat=str(fwsthreat))
                                    col += 1
                                    FWSNAME = ''
                                    for FWSnm in FWSRnam:
                                        FWSNAME = FWSnm
                                    worksheet.write(row, col, str(FWSNAME), formatwrap)

                                else:
                                    i = col
                                    i1 = col + 3
                                    for i in range(i, i1):
                                        worksheet.write(row, i, "", formatwrap)

                                    rcvals = [['0', 'A'], ['1', 'B'], ['2', 'C'], ['3', 'D'], ['4', 'E'], ['5', 'F'],
                                              ['6', 'G'], ['7', 'H'], ['8', 'I'], ['9', 'J'], ['10', 'K'], ['11', 'L'],
                                              ['12', 'M'], ['13', 'N'], ['14', 'O'], ['15', 'P'], ['16', 'Q'],
                                              ['17', 'R'], ['18', 'S'], ['19', 'T'], ['20', 'U'], ['21', 'V'],
                                              ['22', 'W'], ['23', 'X'], ['24', 'Y'], ['25', 'Z'], ['26', 'AA'],
                                              ['27', 'AB'], ['28', 'AC'], ['29', 'AD'], ['30', 'AE'], ['31', 'AF'],
                                              ['32', 'AG'], ['33', 'AH'], ['34', 'AI'], ['35', 'AJ'], ['36', 'AK'],
                                              ['37', 'AL'], ['38', 'AM'], ['39', 'AN'], ['40', 'AO'], ['41', 'AP'],
                                              ['42', 'AQ'], ['43', 'AR'], ['44', 'AS'], ['45', 'AT'], ['46', 'AU'],
                                              ['47', 'AV'], ['48', 'AW'], ['49', 'AX'], ['50', 'AY'], ['51', 'AZ'],
                                              ['52', 'BA'], ['53', 'BB'], ['54', 'BC'], ['55', 'BD'], ['56', 'BE'],
                                              ['57', 'BF'], ['58', 'BG'], ['59', 'BH'], ['60', 'BI'], ['61', 'BJ'],
                                              ['62', 'BK'], ['63', 'BL'], ['64', 'BM'], ['65', 'BN'], ['66', 'BO'],
                                              ['67', 'BP'], ['68', 'BQ'], ['69', 'BR'], ['70', 'BS'], ['71', 'BT'],
                                              ['72', 'BU'], ['73', 'BV'], ['74', 'BW'], ['75', 'BX'], ['76', 'BY'],
                                              ['77', 'BZ']]

                                    for rcv in rcvals:
                                        if int(rcv[0]) == int(col):
                                            rccol = rcv[1]

                                    rcrow = row + 1
                                    rowcol = str(rccol) + str(rcrow)

                                    worksheet.data_validation(str(rowcol),
                                                              {'validate': 'list', 'source': '=$AG$1:$AG$10'})
                                    if rowmax < row:
                                        rowmax = row
                                    if colmax < col:
                                        colmax = col

                if QuTy == 1:
                    validvals = [
                        '1. Yes - supported by documentation provided by partner/proponent (Cite document and relevant section/pages)',
                        '1. Yes - well supported in the peer-reviewed literature and/or in reports/gray literature(Cite one or two references supporting conclusion)',
                        '1. Yes - well supported in personal communications with expert(s) (Cite person,  date [documentation must be in the record])',
                        '1. Yes - other  (Narrative explanation in text box)',
                        '2. No - protocol untested or not known to be effective',
                        '2. No - effectiveness info provided is absent or inadequate',
                        '2. No - threat not present for MZ specified', '2. No - project does not meet stated objective',
                        '2. No - does not provide a conservation benefit to the species (Explain conclusion ; 1-2 sentences)',
                        '2. No - other (Narrative explanation in text box)']

                    j = 0
                    for validval in validvals:
                        worksheet.write(j, 34, validval)
                        j = j + 1

                worksheet.autofilter(0, 0, rowmax, colmax + 2)
                worksheet.set_column('AE:XFD', None, None, {'hidden': True})

                worksheet1 = workbook.add_worksheet('Metadata')

                formatread1 = workbook.add_format()
                formatread1.set_bg_color('#81BEF7')

                formatwrite1 = workbook.add_format()
                formatwrite1.set_bg_color('#F5A9A9')

                worksheet1.write(0, 0,
                                 'Data contained within this Excel workbook are for U.S. Fish and Wildlife Service use only',
                                 formatbold)

                worksheet1.write(1, 0,
                                 'The FWS evaluation information provided in this file is deliberative, pre-decisional, and not for distribution.',
                                 formatbold)

                worksheet1.write(2, 0,
                                 'Please complete all FWS required fields (field headers highlighted in red) and return all fields/names/responses in the query',
                                 formatbold)

                worksheet1.write(3, 0,
                                 'The list in this report represents projects recorded as "complete" and "effective" by project proponents.',
                                 formatbold)

                worksheet1.write(5, 0, 'Key', formatbold)
                worksheet1.write(6, 0, '', formatread1)
                worksheet1.write(6, 1, 'CED Data, Read Only', formatbold)
                worksheet1.write(7, 0, '', formatwrite1)
                worksheet1.write(7, 1, 'FWS Required fields', formatbold)
                workbook.close()
                DataDown = 'True'
            context = {'authen': authen, 'form': form, 'fwstable': table, 'showq': 'Show', 'Cnt': cnt,
                       'DataDown': DataDown, 'DataCSV': outputfshort, 'showlogin': 'True'}
            # return render(request, 'ced_main/fwsquery.html', context)
            return render(request, 'ced_main/permission_denied.html', context)

    if request.user.is_authenticated() and (userAgency == 'U.S. Fish and Wildlife Service' or userOffice == 'Congress'):
        form = fwsquery_Form()
        if authen == 'authenadmin' or userAgency == 'U.S. Fish and Wildlife Service':
            context = {'authen': authen, 'form': form, 'fwstable': 'None', 'showq': 'None', 'showlogin': 'True'}
            # return render(request, 'ced_main/fwsquery.html', context)
            return render(request, 'ced_main/permission_denied.html', context)
        else:
            return render(request, 'ced_main/permission_denied.html', context)
    else:
        return render(request, 'ced_main/permission_denied.html', context)


@login_required
def sgcedquery(request):
    siteurl = request.build_absolute_uri()
    siteurl1 = siteurl.split("/")
    siteurl2 = siteurl1[0] + "//" + siteurl1[2]

    profile = request.user
    userAgency = userprofile.objects.values_list('Agency', flat=True)
    userOffice = userprofile.objects.values_list('Field_Office', flat=True)
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    username1 = request.user.username

    threavaltest, activitytest, subactivitytest, wafwatest = gettables()
    context = {'authen': authen, 'showlogin': 'True'}
    if request.method == 'GET':
        AgencyVal = "All agencies"
        OfficeVal = "All offices"
        ImpStatVal = 'Approved'
        EffStatVal = "All effectiveness status options"
        StrtYearVal = "All years"
        FinishYearVal = "All years"
        ActTypeVal = "All activity types"
        ActivityVal = "All activities"
        SubActVal = "All subactivities"
        ThreatsVal = "All threats"
        WAFWAVal = "All WAFWA Zones"
        SGPopVal = "All sage-grouse populations"
        StateVal = "All states"
        CountyVal = "All counties"
        EntryVal = "All entry types"

        TAExst = request.GET.get('TA', 'NOTA')
        ETExst = request.GET.get('ET', 'NOET')
        ACTExst = request.GET.get('ACT', 'NOACT')
        IPExst = request.GET.get('IP', 'NOIP')
        STExst = request.GET.get('ST', 'NOST')
        POPExst = request.GET.get('POP', 'NOPOP')
        MUExst = request.GET.get('MU', 'NOMU')
        if TAExst != 'NOTA' or ETExst != 'NOET' or ACTExst != 'NOACT' or IPExst != 'NOIP' or STExst != 'NOST' or POPExst != 'NOPOP' or MUExst != 'NOMU':
            uq = project_info.objects.filter(Entry_Type=3)
            if TAExst != 'NOTA':
                TAVal = typeact.objects.values_list('TypeAct', flat=True).get(id=TAExst)
                uq = uq.filter(TypeAct=TAVal)
                AgencyVal = TAVal
            if ETExst != 'NOET':
                impstat = []
                if ETExst == 'Completed':
                    impsat.append(3)
                    ImpStatVal = 'Completed'
                else:
                    impsat.append(3)
                    impsat.append(2)
                    impsat.append(1)
                uq = uq.filter(Project_Status__in=impsat)
            if ACTExst != 'NOACT':
                ACTVal = activity.objects.values_list('Activity', flat=True).get(id=ACTExst)
                uq = uq.filter(Activity=ACTVal)
                ActTypeVal = ACTVal
            if IPExst != 'NOIP':
                IPVal = imp_party_values.objects.values_list('Implementation_Party', flat=True).get(id=IPExst)
                uq = uq.filter(Implementing_Party=IPVal)
                AgencyVal = IPVal
            if MUExst != 'NOMU':
                WAFW = []
                wafwaval1 = wafwa_zone_values.objects.get(id=MUExst)
                wafwavaltxt = wafwa_zone_values.objects.values_list('WAFWA_Zone', flat=True).get(id=MUExst)
                WAFWval = wafwa_info.objects.values_list('Project_ID', flat=True).filter(WAFWA_Value=wafwaval1)
                WAFWAVal = wafwavaltxt
                for WA in WAFWval:
                    WAFW.append(WA)
                uq = uq.filter(Project_ID__in=WAFW)
            if POPExst != 'NOPOP':
                sagepop = []
                sagepop1 = population_values.objects.get(id=POPExst)
                sagepoptxt = population_values.objects.values_list('Populations', flat=True).get(id=POPExst)
                sagepopval = population_info.objects.values_list('Project_ID', flat=True).filter(
                    Population_Value=sagepop1)
                SGPopVal = sagepoptxt
                for sagep in sagepopval:
                    sagepop.append(sagep)
                uq = uq.filter(Project_ID__in=sagepop)
            if STExst != 'NOST':
                Stat = []
                stateval1 = state.objects.get(id=STExst)
                statevaltxt = state.objects.values_list('State', flat=True).get(id=STExst)
                Statval = state_info.objects.values_list('Project_ID', flat=True).filter(State_Value=stateval1)
                StateVal = statevaltxt
                for St in Statval:
                    Stat.append(St)
                uq = uq.filter(Project_ID__in=Stat)
            FinalCnt = 0
            for u in uq:
                FinalCnt = FinalCnt + 1
                Records = FinalCnt

            table = viewapprovalprojects_table(project_info.objects.filter(Project_ID__in=uq))
            RequestConfig(request).configure(table)
            context = {'viewprojects': table, 'authen': authen, 'AgencyVal': AgencyVal, 'OfficeVal': OfficeVal,
                       'ImpStatVal': ImpStatVal, 'EffStatVal': EffStatVal, 'StartYearVal': StartYearVal,
                       'FinishYearVal': FinishYearVal, 'ActTypeVal': ActTypeVal, 'ActivityVal': ActivityVal,
                       'SubActVal': SubActVal, 'ThreatsVal': ThreatsVal, 'WAFWAVal': WAFWAVal, 'SGPopVal': SGPopVal,
                       'StateVal': StateVal, 'CountyVal': CountyVal, 'EntryVal': EntryVal, 'Records': Records,
                       'userAgency': userAgency, 'userOffice': userOffice, 'showlogin': 'True'}
            # return render(request, 'ced_main/viewqueryresults.html', context)
            return render(request, 'ced_main/permission_denied.html', context)

    if request.method == 'POST':
        form = query_Form(request.POST)
        if form.is_valid():

            AgencyVal = "All agencies"
            Agencycnt = 0
            OfficeVal = "All offices"
            Officecnt = 0
            ImpStatVal = "All implementation status options"
            ImpStatcnt = 0
            EffStatVal = "All effectiveness status options"
            EffStatcnt = 0
            startYearVal = "All years"
            startYearcnt = 0
            endYearVal = "All years"
            finishYearcnt = 0
            ActTypeVal = "All activity types"
            ActTypecnt = 0
            ActivityVal = "All activities"
            Activitycnt = 0
            SubActVal = "All subactivities"
            SubActcnt = 0
            MetricVal = "All Metrics"
            Metriccnt = 0
            ThreatsVal = "All threats"
            Threatscnt = 0
            WAFWAVal = "All WAFWA Zones"
            WAFWAcnt = 0
            SGPopVal = "All sage-grouse populations"
            SGPopcnt = 0
            StateVal = "All states"
            Statecnt = 0
            CountyVal = "All counties"
            Countycnt = 0
            EntryVal = "All entry types"
            Entrycnt = 0
            DocVal = "All document types"
            DocVal = "All document types"
            KeyWordVal = "No key words specified"
            keywordcnt = 0
            Doccnt = 0
            Records = 0

            spatiallist = "?"
            spatialstart = 0

            # Filter by agency
            agcy = []
            agcycnt = 0
            for agncy in request.POST.getlist('Agency'):
                agcyval = imp_party_values.objects.values_list('Implementation_Party', flat=True).get(id=agncy)
                agcy.append(agcyval)
                if Agencycnt == 0:
                    AgencyVal = str(agcyval)
                    spatiallist = spatiallist + "IP=" + str(agncy)
                    spatialstart = 1
                    Agencycnt = 1
                else:
                    AgencyVal = AgencyVal + ", " + str(agcyval)
                    spatiallist = spatiallist + "," + str(agncy)
                agcycnt = 1
            if agcycnt == 1:
                uq = uq.filter(Implementing_Party__in=agcy)

                # Filter by office
            offic = []
            officcnt = 0
            for offi in request.POST.getlist('Field_Office'):
                offic.append(offi)
                if Officecnt == 0:
                    OfficeVal = str(offi)
                    Officecnt = 1
                else:
                    OfficeVal = OfficeVal + ", " + str(offi)
                officcnt = 1
            if officcnt == 1:
                uq = uq.filter(Office__in=offic)

            uq = uq.filter(Entry_Type=3)

            # Filter by implementation status
            impsat = []
            impsatcnt = 0
            for impsa in request.POST.getlist('Imp_Status'):
                impsat.append(impsa)
                impsatcnt = 1
                if int(impsa) == 1:
                    ImpStatvalval = 'Planned'
                elif int(impsa) == 2:
                    ImpStatvalval = 'In Progress'
                elif int(impsa) == 3:
                    ImpStatvalval = 'Completed'

                if ImpStatcnt == 0:
                    ImpStatVal = str(ImpStatvalval)
                    if spatialstart == 0:
                        spatiallist = spatiallist + "ET=" + str(impsa)
                    else:
                        spatiallist = spatiallist + "&ET=" + str(impsa)
                    ImpStatcnt = 1
                else:
                    ImpStatVal = ImpStatVal + ", " + str(ImpStatvalval)
                    spatiallist = spatiallist + "," + str(impsa)
            if impsatcnt == 1:
                uq = uq.filter(Project_Status__in=impsat)

            # Filter by effectiveness status
            effsat = []
            effsatcnt = 0
            for effsa in request.POST.getlist('Effective_Determined'):
                agcyval = implementation_info.objects.values_list('Project_ID', flat=True).filter(
                    Effective_Determined=effsa)
                for av in agcyval:
                    effsat.append(av)
                effsatcnt = 1
                if int(effsa) == 1:
                    EffStatvalval = 'Yes: project is already effective.'
                elif int(effsa) == 2:
                    EffStatvalval = 'Uncertain or Unlikely: project is uncertain or unlikely to be effective based on current information.'
                elif int(effsa) == 3:
                    EffStatvalval = 'Highly Likely: project is reasonably certain to be effective given adequate time.'

                if EffStatcnt == 0:
                    EffStatVal = str(EffStatvalval)
                    EffStatcnt = 1
                else:
                    EffStatVal = EffStatVal + ", " + str(EffStatvalval)
            if effsatcnt == 1:
                uq = uq.filter(Project_ID__in=effsat)

            # Filter by start year
            strtequation = request.POST.getlist('StartSelect')  # get the start year equation
            strtequation = str(strtequation).replace("[u'", "")
            strtequation = strtequation.replace("']", "")

            if strtequation == '----Choose an Equation----' or strtequation == 'Equal To':
                startyears = []
                startYearcnt = 0
                for startyearv in request.POST.getlist('Start_Year'):
                    if startYearcnt == 0:
                        startYearVal = str(startyearv)
                        startYearcnt = 1
                    else:
                        startYearVal = startYearVal + ", " + str(startyearv)

                    startstdt = project_info.objects.filter(Start_Date__year=int(startyearv))
                    for strtdt in startstdt:
                        startyears.append(int(str(strtdt)))
                        startYearcnt = 1

                if startYearcnt == 1:
                    uq = uq.filter(Project_ID__in=startyears)

            elif strtequation == 'Greater Than':
                startyears = []
                startYearcnt = 0
                gty = 0
                for startyearv in request.POST.getlist('Start_Year'):
                    startYearcnt = 1
                    if int(startyearv) < int(gty) or int(gty) == 0:
                        gty = int(startyearv)

                if startYearcnt == 1:
                    startstdt = project_info.objects.filter(Start_Date__year__gte=int(gty))
                    for strtdt in startstdt:
                        startyears.append(int(str(strtdt)))

                    startYearVal = 'Greater than or equal to ' + str(gty)
                    uq = uq.filter(Project_ID__in=startyears)

            elif strtequation == 'Less Than':
                startyears = []
                startYearcnt = 0
                lty = 0
                for startyearv in request.POST.getlist('Start_Year'):
                    startYearcnt = 1
                    if startyearv > lty:
                        lty = startyearv

                if startYearcnt == 1:
                    startstdt = project_info.objects.filter(Start_Date__year__lte=int(lty))
                    for strtdt in startstdt:
                        startyears.append(int(str(strtdt)))

                    startYearVal = 'Less than or equal to ' + str(lty)
                    uq = uq.filter(Project_ID__in=startyears)

            # Filter by end year
            edequation = request.POST.getlist('EndSelect')  # get the end year equation
            edequation = str(edequation).replace("[u'", "")
            edequation = edequation.replace("']", "")

            if edequation == '----Choose an Equation----' or edequation == 'Equal To':

                endyears = []
                endYearcnt = 0
                for endyearv in request.POST.getlist('End_Year'):
                    if endYearcnt == 0:
                        endYearVal = str(endyearv)
                        endYearcnt = 1
                    else:
                        endYearVal = endYearVal + ", " + str(endyearv)

                    endstdt = project_info.objects.filter(End_Date__year=int(endyearv))
                    for eddt in endstdt:
                        endyears.append(int(str(eddt)))
                        endYearcnt = 1

                if endYearcnt == 1:
                    uq = uq.filter(Project_ID__in=endyears)

            elif edequation == 'Greater Than':
                endyears = []
                endYearcnt = 0
                gty = 0
                for endyearv in request.POST.getlist('End_Year'):
                    endYearcnt = 1
                    if int(endyearv) < int(gty) or int(gty) == 0:
                        gty = int(endyearv)

                if endYearcnt == 1:
                    endstdt = project_info.objects.filter(End_Date__year__gte=int(gty))
                    for eddt in endstdt:
                        endyears.append(int(str(eddt)))

                    endYearVal = 'Greater than or equal to ' + str(gty)
                    uq = uq.filter(Project_ID__in=endyears)

            elif edequation == 'Less Than':
                endyears = []
                endYearcnt = 0
                lty = 0
                for endyearv in request.POST.getlist('End_Year'):
                    endYearcnt = 1
                    if endyearv > lty:
                        lty = endyearv

                if endYearcnt == 1:
                    endstdt = project_info.objects.filter(End_Date__year__lte=int(lty))
                    for eddt in endstdt:
                        endyears.append(int(str(eddt)))

                    endYearVal = 'Less than or equal to ' + str(lty)
                    uq = uq.filter(Project_ID__in=endyears)

            # Filter by activity type
            actype = []
            actypecnt = 0
            for actyp in request.POST.getlist('TypeAct'):
                actypval = typeact.objects.values_list('TypeAct', flat=True).get(id=actyp)
                if ActTypecnt == 0:
                    ActTypeVal = str(actypval)
                    if spatialstart == 0:
                        spatiallist = spatiallist + "TA=" + str(actyp)
                    else:
                        spatiallist = spatiallist + "&TA=" + str(actyp)
                    ActTypecnt = 1
                else:
                    ActTypeVal = ActTypeVal + ", " + str(actypval)
                    spatiallist = spatiallist + "," + str(actypval)
                actype.append(actypval)
                actypecnt = 1
            if actypecnt == 1:
                uq = uq.filter(TypeAct__in=actype)

            # Filter by activity
            act = []
            actcnt = 0
            for actv in request.POST.getlist('Activity'):
                actval = str(actv)  # activitytest.values_list('Activity',flat=True).get(id=actv)
                if Activitycnt == 0:
                    ActivityVal = str(actval)
                    if spatialstart == 0:
                        spatiallist = spatiallist + "ACT=" + str(actv)
                    else:
                        spatiallist = spatiallist + "&ACT=" + str(actv)
                    Activitycnt = 1
                else:
                    ActivityVal = ActivityVal + ", " + str(actval)
                    spatiallist = spatiallist + "," + str(actval)
                act.append(actval)
                actcnt = 1
            if actcnt == 1:
                uq = uq.filter(Activity__in=act)

            # Filter by subactivity
            subact = []
            subactcnt = 0
            for subactv in request.POST.getlist('SubActivity'):
                subactval = subactv  # subactivitytest.values_list('SubActivity',flat=True).get(id=subactv)
                if SubActcnt == 0:
                    SubActVal = str(subactval)
                    SubActcnt = 1
                else:
                    SubActVal = SubActVal + ", " + str(subactval)
                subact.append(subactval)
                subactcnt = 1
            if subactcnt == 1:
                uq = uq.filter(SubActivity__in=subact)

            # Filter by metric
            metricv = []
            metriccnt = 0
            fail = 'Success'

            if 'MetType' in request.POST and 'MetEqu' in request.POST and 'MetValue' in request.POST:
                for mettype1 in request.POST.getlist('MetType'):
                    if mettype1 != '----Choose a Metric----':
                        metty = str(mettype1)
                        mettext = metric.objects.values_list('Metric', flat=True).get(Text=metty)
                        for metequ1 in request.POST.getlist('MetEqu'):
                            if metequ1 == "Greater Than":
                                metequ = "Greater Than"
                            elif metequ1 == "Less Than":
                                metequ = "Less Than"
                            elif metequ1 == "Equal To":
                                metequ = "Equal To"
                            else:
                                fail = 'Fail'
                            if fail != 'Fail':
                                for metval1 in request.POST.getlist('MetValue'):
                                    try:
                                        metval = float(metval1)
                                        if metval <= 0:
                                            fail = 'Fail'
                                    except:
                                        fail = 'Fail'
                    else:
                        fail = 'Fail'
                if fail == 'Success':
                    MetricVal = mettext + " is " + metequ1 + " " + str(metval)
                    allmetprjs = metrics.objects.all()
                    for metricprj in allmetprjs:
                        try:
                            prjval = int(str(metricprj))
                            metricvalue = metrics.objects.values_list(metty, flat=True).get(Project_ID=prjval)
                            if metequ == "Greater Than" and (metricvalue != None or metricvalue != 'None'):
                                if float(metricvalue) > float(metval):
                                    metricv.append(prjval)
                            elif metequ == "Less Than" and (metricvalue != None or metricvalue != 'None'):
                                if float(metricvalue) < float(metval):
                                    metricv.append(prjval)
                            elif metequ == "Equal To" and (metricvalue != None or metricvalue != 'None'):
                                if float(metricvalue) == float(metval):
                                    metricv.append(prjval)
                        except:
                            test = "test"

                    uq = uq.filter(Project_ID__in=metricv)

            # Filter by threats
            threa = []
            threacnt = 0
            for thre in request.POST.getlist('Threats'):
                threatval1 = threat_values.objects.values_list('Threats', flat=True).get(id=thre)
                if Threatscnt == 0:
                    ThreatsVal = str(threatval1)
                    Threatscnt = 1
                else:
                    ThreatsVal = ThreatsVal + ", " + str(threatval1)
                threaval = threavaltest.values_list('Project_ID', flat=True).filter(Threat=thre)
                for thr in threaval:
                    threa.append(thr)
                threacnt = 1
            if threacnt == 1:
                uq = uq.filter(Project_ID__in=threa)

            # Filter by WAFWA Zones
            WAFW = []
            WAFWcnt = 0
            for WAF in request.POST.getlist('WAFWA_Zone'):
                wafwaval1 = wafwa_zone_values.objects.values_list('WAFWA_Zone', flat=True).get(id=WAF)
                if WAFWAcnt == 0:
                    WAFWAVal = str(wafwaval1)
                    if spatialstart == 0:
                        spatiallist = spatiallist + "MU=" + str(WAF)
                    else:
                        spatiallist = spatiallist + "&MU=" + str(WAF)
                    WAFWAcnt = 1
                else:
                    WAFWAVal = WAFWAVal + ", " + str(wafwaval1)
                    spatiallist = spatiallist + "," + str(WAF)
                WAFWval = wafwa_info.objects.values_list('Project_ID', flat=True).filter(WAFWA_Value=WAF)
                for WA in WAFWval:
                    WAFW.append(WA)
                WAFWcnt = 1
            if WAFWcnt == 1:
                uq = uq.filter(Project_ID__in=WAFW)

            # Filter by Populations
            sagepop = []
            sagepopcnt = 0
            for sagepo in request.POST.getlist('Sage_Grouse_Population'):
                sagepop1 = population_values.objects.values_list('Populations', flat=True).get(id=sagepo)
                if SGPopcnt == 0:
                    SGPopVal = str(sagepop1)
                    if spatialstart == 0:
                        spatiallist = spatiallist + "POP=" + str(sagepo)
                    else:
                        spatiallist = spatiallist + "&POP=" + str(sagepo)
                    SGPopcnt = 1
                else:
                    SGPopVal = SGPopVal + ", " + str(sagepop1)
                    spatiallist = spatiallist + "," + str(sagepo)
                sagepopval = population_info.objects.values_list('Project_ID', flat=True).filter(
                    Population_Value=sagepo)
                for sagep in sagepopval:
                    sagepop.append(sagep)
                sagepopcnt = 1
            if sagepopcnt == 1:
                uq = uq.filter(Project_ID__in=sagepop)

            # Filter by States
            Stat = []
            Statcnt = 0
            for Sta in request.POST.getlist('State'):
                stateval1 = state.objects.values_list('State', flat=True).get(id=Sta)
                if Statecnt == 0:
                    StateVal = str(stateval1)
                    if spatialstart == 0:
                        spatiallist = spatiallist + "ST=" + str(Sta)
                    else:
                        spatiallist = spatiallist + "&ST=" + str(Sta)
                    Statecnt = 1
                else:
                    StateVal = StateVal + ", " + str(stateval1)
                    spatiallist = spatiallist + "," + str(Sta)
                Statval = state_info.objects.values_list('Project_ID', flat=True).filter(State_Value=Sta)
                for St in Statval:
                    Stat.append(St)
                Statcnt = 1
            if Statcnt == 1:
                uq = uq.filter(Project_ID__in=Stat)

            # Filter by County
            Coun = []
            Councnt = 0
            for Cou in request.POST.getlist('County'):
                countyval1 = state_county.objects.values_list('Cnty_St', flat=True).get(id=Cou)
                if Countycnt == 0:
                    CountyVal = str(countyval1)
                    Countycnt = 1
                else:
                    CountyVal = CountyVal + ", " + str(countyval1)
                Counval = county_info.objects.values_list('Project_ID', flat=True).filter(County_Value=Cou)
                for Co in Counval:
                    Coun.append(Co)
                Councnt = 1
            if Councnt == 1:
                uq = uq.filter(Project_ID__in=Coun)

            # Filter by Documentation
            Docu = []
            Docucnt = 0
            for Doc in request.POST.getlist('File_Type'):
                Docuval = documentation.objects.values_list('Project_ID', flat=True).filter(File_Type=str(Doc))
                for Do in Docuval:
                    Docu.append(Do)
                Docucnt = 1
            if Docucnt == 1:
                uq = uq.filter(Project_ID__in=Docu)

            # Filter by Key Words
            kwprjs = []
            kwcnt = 0
            prjname = "None"
            for KW in request.POST.getlist('Key_Words'):
                KWVal = KW.split(", ")
                for KWV in KWVal:
                    try:
                        if KWV == "" or KWV == " ":
                            test = "test"
                        else:
                            if keywordcnt == 0:
                                KeyWordVal = str(KWV)
                                keywordcnt = 1
                            else:
                                KeyWordVal = KeyWordVal + ", " + str(KWV)
                            # Project Name
                            prjname = project_info.objects.values_list('Project_ID', flat=True).filter(
                                Project_Name__icontains=KWV)
                            for prjv in prjname:
                                kwprjs.append(prjv)
                                kwcnt = 1

                            # Project_Status
                            etval = 0
                            if KWV == 'Completed':
                                etval = 3
                            elif KWV == 'In Progress':
                                etval = 2
                            elif KWV == 'Planned':
                                etval = 1
                            if etval != 0:
                                etype = project_info.objects.values_list('Project_ID', flat=True).filter(
                                    Project_Status=etval)
                                for etv in etype:
                                    kwprjs.append(etv)
                                    kwcnt = 1
                            # TypeAct
                            TAct = project_info.objects.values_list('Project_ID', flat=True).filter(
                                TypeAct__icontains=KWV)
                            for prjv in TAct:
                                kwprjs.append(prjv)
                                kwcnt = 1
                            # Activity
                            activity = project_info.objects.values_list('Project_ID', flat=True).filter(
                                Activity__icontains=KWV)
                            for prjv in activity:
                                kwprjs.append(prjv)
                                kwcnt = 1
                            # SubActivity
                            subactivity = project_info.objects.values_list('Project_ID', flat=True).filter(
                                SubActivity__icontains=KWV)
                            for prjv in subactivity:
                                kwprjs.append(prjv)
                                kwcnt = 1
                            # Objectives Description
                            obdesc = project_info.objects.values_list('Project_ID', flat=True).filter(
                                Objectives_Desc__icontains=KWV)
                            for prjv in obdesc:
                                kwprjs.append(prjv)
                                kwcnt = 1
                            # Implementing Party
                            impart = project_info.objects.values_list('Project_ID', flat=True).filter(
                                Implementing_Party__icontains=KWV)
                            for prjv in impart:
                                kwprjs.append(prjv)
                                kwcnt = 1
                            # Office
                            offi = project_info.objects.values_list('Project_ID', flat=True).filter(
                                Office__icontains=KWV)
                            for prjv in offi:
                                kwprjs.append(prjv)
                                kwcnt = 1
                            # Collaborating Party
                            imptxt = imp_party_values.objects.values_list('id', flat=True).filter(
                                Implementation_Party__icontains=KWV)
                            colli = collab_party.objects.values_list('Project_ID', flat=True).filter(
                                Collab_Party__in=imptxt)
                            for prjv in colli:
                                kwprjs.append(prjv)
                                kwcnt = 1
                            # County
                            coutxt = state_county.objects.values_list('id', flat=True).filter(Cnty_St__icontains=KWV)
                            couni = county_info.objects.values_list('Project_ID', flat=True).filter(
                                County_Value__in=coutxt)
                            for prjv in couni:
                                kwprjs.append(prjv)
                                kwcnt = 1

                            # State
                            sttxt = state.objects.values_list('id', flat=True).filter(State__icontains=KWV)
                            sti = state_info.objects.values_list('Project_ID', flat=True).filter(State_Value__in=sttxt)
                            for prjv in sti:
                                kwprjs.append(prjv)
                                kwcnt = 1

                            sttxt1 = state.objects.values_list('id', flat=True).filter(StateName__icontains=KWV)
                            sti1 = state_info.objects.values_list('Project_ID', flat=True).filter(
                                State_Value__in=sttxt1)
                            for prjv in sti1:
                                kwprjs.append(prjv)
                                kwcnt = 1

                            # HUC12
                            huctxt = state_county_huc12_values.objects.values_list('id', flat=True).filter(
                                HUC12_Cnty_State__icontains=KWV)
                            huci = huc12_info.objects.values_list('Project_ID', flat=True).filter(
                                HUC12_Value__in=huctxt)
                            for prjv in huci:
                                kwprjs.append(prjv)
                                kwcnt = 1

                            # WAFWA
                            waftxt = wafwa_zone_values.objects.values_list('id', flat=True).filter(WAFWA_Zone=KWV)
                            wafi = wafwa_info.objects.values_list('Project_ID', flat=True).filter(
                                WAFWA_Value__in=waftxt)
                            for prjv in wafi:
                                kwprjs.append(prjv)
                                kwcnt = 1

                            try:
                                waftxt1 = wafwa_zone_values.objects.values_list('id', flat=True).filter(id=KWV)
                                wafi1 = wafwa_info.objects.values_list('Project_ID', flat=True).filter(
                                    WAFWA_Value__in=waftxt1)
                                for prjv in wafi1:
                                    kwprjs.append(prjv)
                                    kwcnt = 1
                            except:
                                test = "test"

                            # Sage Grouse Population
                            poptxt = population_values.objects.values_list('id', flat=True).filter(
                                Populations__icontains=KWV)
                            popi = population_info.objects.values_list('Project_ID', flat=True).filter(
                                Population_Value__in=poptxt)
                            for prjv in popi:
                                kwprjs.append(prjv)
                                kwcnt = 1

                            # Ownership
                            owntxt = ownership_values.objects.values_list('id', flat=True).filter(Owners__icontains=KWV)
                            owni = ownership_info.objects.values_list('Project_ID', flat=True).filter(
                                Owner_Value__in=owntxt)
                            for prjv in owni:
                                kwprjs.append(prjv)
                                kwcnt = 1

                            # Threats
                            thrtxt = threat_values.objects.values_list('id', flat=True).filter(Threats=KWV)
                            thri = threats.objects.values_list('Project_ID', flat=True).filter(Threat__in=thrtxt)
                            for prjv in thri:
                                kwprjs.append(prjv)
                                kwcnt = 1

                            # Document File Type
                            fti = documentation.objects.values_list('Project_ID', flat=True).filter(
                                File_Type__icontains=KWV)
                            for prjv in fti:
                                kwprjs.append(prjv)
                                kwcnt = 1

                            # Document Description
                            fti = documentation.objects.values_list('Project_ID', flat=True).filter(
                                Document_Description__icontains=KWV)
                            for prjv in fti:
                                kwprjs.append(prjv)
                                kwcnt = 1

                            # Document Name
                            fti = documentation.objects.values_list('Project_ID', flat=True).filter(
                                Document_Name__icontains=KWV)
                            for prjv in fti:
                                kwprjs.append(prjv)
                                kwcnt = 1

                            # Effectiveness Explained
                            fti = implementation_info.objects.values_list('Project_ID', flat=True).filter(
                                Effective_Explained__icontains=KWV)
                            for prjv in fti:
                                kwprjs.append(prjv)
                                kwcnt = 1
                    except:
                        if kwcnt == 0:
                            kwcnt = 0
            if kwcnt == 1:
                uq = uq.filter(Project_ID__in=kwprjs)
            else:
                KeyWordVal = "No key words selected"

            FinalCnt = 0
            udl = []
            uq = uq.order_by('Project_Name')
            for u in uq:
                udl.append(str(u))
                FinalCnt = FinalCnt + 1
                Records = FinalCnt

            prjnames = project_info.objects.values_list('Project_Name', flat=True).all()

            if FinalCnt > 0 and 'submitmap' in request.POST:
                grsgmap = '/sgce/grsgmap/' + spatiallist
                return redirect(grsgmap)

            if FinalCnt > 0:
                project_query.objects.filter(User=request.user.username).delete()

                for addprj in udl:
                    objaddprj = project_query()
                    objaddprj.Project_ID = addprj
                    objaddprj.Project_Name = str(
                        project_info.objects.values_list('Project_Name', flat=True).get(Project_ID=addprj))
                    objaddprj.User = request.user.username
                    objaddprj.save()

            DataDown = "False"
            outputfshort = ""

            if FinalCnt > 0 and 'summarize' in request.POST:

                DataDown = "True"
                now1 = str(now)[0:18]
                now2 = now1.replace(" ", "_")
                nowf = now2.replace(":", "-")
                #TODO
                filep = 'ced_main/images/created_docs/' + username1 + '_CSV_Summary_Data_' + str(
                    nowf) + '.csv'
                outputf1 = os.path.join(STATIC_DIR, filep)
                outputfshort = siteurl2 + '/static/ced_main/images/created_docs/' + username1 + '_CSV_Summary_Data_' + str(
                    nowf) + '.csv'
                csum1 = open(outputf1, "wb")
                csum1.close()
                csum1 = open(outputf1, "ab")
                csum1.write('State,WAFWA Zone,Threat,Metric Unit,Effort Count,Metric Value\n')

                stat = [["1", "Arizona"], ["183", "California"], ["985", "Colorado"], ["1992", "Idaho"],
                        ["4512", "Montana"], ["9396", "North Dakota"], ["9826", "Nebraksa"], ["9901", "Nevada"],
                        ["12665", "Oregon"], ["14797", "South Dakota"], ["15561", "Utah"], ["18333", "Washington"],
                        ["19432", "Wyoming"], ["19433", "Alberta"]]
                mzn = [["1", "Zone 1"], ["2", "Zone 2"], ["3", "Zone 3"], ["4", "Zone 4"], ["5", "Zone 5"],
                       ["6", "Zone 6"], ["7", "Zone 7"]]
                thr = [["1", "Agricultural Conversion"], ["2", "Conifer Encroachment"], ["3", "Energy Development"],
                       ["4", "Fire"], ["5", "Free Roaming Equids"], ["6", "Grazing / Range Management"],
                       ["7", "Infrastructure"], ["8", "Isolated / Small Population Size"], ["9", "Mining"],
                       ["10", "Noxious Weeds / Annual Grasses"], ["11", "Recreation"], ["12", "Sagebrush Elimination"],
                       ["13", "Urbanization"]]
                metric1 = ["TotalAcres", "TotalMiles", "TotalEquids", "TotalNumberBirds", "TotalNumberRemoved"]

                for st in stat:
                    usum = uq
                    nostate = 0
                    Stat2 = []
                    state1 = st[0]
                    statenm = st[1]
                    try:
                        Statval1 = state_info.objects.values_list('Project_ID', flat=True).filter(
                            State_Value=int(state1))
                    except:
                        nostate = -1
                    getcnt = Statval1.count()
                    if nostate == 0 and getcnt > 0:
                        for St1 in Statval1:
                            Stat2.append(St1)
                        usum1 = usum.filter(Project_ID__in=Stat2)
                        if usum1.count() > 0:
                            for mz in mzn:
                                nowafa = 0
                                WAFW1 = []
                                mz1 = mz[0]
                                mznm = mz[1]
                                try:
                                    WAFWval1 = wafwatest.values_list('Project_ID', flat=True).filter(
                                        WAFWA_Value=int(mz1))
                                except:
                                    nowafa = -1
                                getcnt = WAFWval1.count()
                                if nowafa == 0 and getcnt > 0:
                                    for WA1 in WAFWval1:
                                        WAFW1.append(WA1)
                                    usum2 = usum1.filter(Project_ID__in=WAFW1)

                                    if usum2.count() > 0:
                                        # Process the threats
                                        for th in thr:
                                            nothr = 0
                                            threa1 = []
                                            th1 = th[0]
                                            thnm = th[1]
                                            try:
                                                threaval1 = threavaltest.values_list('Project_ID', flat=True).filter(
                                                    Threat=th1)
                                            except:
                                                nothr = -1
                                            getcnt = threaval1.count()

                                            if nothr == 0 and getcnt > 0:
                                                for thr1 in threaval1:
                                                    threa1.append(thr1)

                                                usum3 = usum2.filter(Project_ID__in=threa1)
                                                if usum3.count() > 0:

                                                    totac = 0
                                                    totmi = 0
                                                    toteq = 0
                                                    totbi = 0
                                                    totnr = 0
                                                    totaccnt = 0
                                                    totmicnt = 0
                                                    toteqcnt = 0
                                                    totbicnt = 0
                                                    totnrcnt = 0

                                                    for uqsum in usum3:
                                                        for me in metric1:
                                                            mv = 0
                                                            try:
                                                                mv = metricget(str(uqsum), str(me))
                                                            except:
                                                                mv = 0

                                                            if me == "TotalAcres":
                                                                totac = totac + mv
                                                                totaccnt = totaccnt + 1
                                                            elif me == "TotalMiles":
                                                                totmi = totmi + mv
                                                                totmicnt = totmicnt + 1
                                                            elif me == "TotalEquids":
                                                                toteq = toteq + mv
                                                                toteqcnt = toteqcnt + 1
                                                            elif me == "TotalNumberBirds":
                                                                totbi = totbi + mv
                                                                totbicnt = totbicnt + 1
                                                            elif me == "TotalNumberRemoved":
                                                                totnr = totnr + mv
                                                                totnrcnt = totnrcnt + 1

                                                    if totac > 0:
                                                        csum1.write(str(statenm) + "," + str(mznm) + "," + str(
                                                            thnm) + ",Total Acres," + str(totaccnt) + "," + str(
                                                            totac) + "\n")
                                                    if totmi > 0:
                                                        csum1.write(str(statenm) + "," + str(mznm) + "," + str(
                                                            thnm) + ",Total Miles," + str(totmicnt) + "," + str(
                                                            totmi) + "\n")
                                                    if toteq > 0:
                                                        csum1.write(str(statenm) + "," + str(mznm) + "," + str(
                                                            thnm) + ",Total Equids Removed," + str(
                                                            toteqcnt) + "," + str(toteq) + "\n")
                                                    if totbi > 0:
                                                        csum1.write(str(statenm) + "," + str(mznm) + "," + str(
                                                            thnm) + ",Total Number Birds," + str(totbicnt) + "," + str(
                                                            totbi) + "\n")
                                                    if totnr > 0:
                                                        csum1.write(str(statenm) + "," + str(mznm) + "," + str(
                                                            thnm) + ",Total Number Removed," + str(
                                                            totnrcnt) + "," + str(totnr) + "\n")
                csum1.close()

            if FinalCnt > 0 and 'exportcsv' in request.POST:
                now1 = str(now)[0:18]
                now2 = now1.replace(" ", "_")
                nowf = now2.replace(":", "-")
                #TODO
                filep = 'ced_main/images/created_docs/' + username1 + '_CSV_Query_Data_' + str(
                    nowf) + '.csv'
                outputf = os.path.join(STATIC_DIR, filep)
                outputfshort = siteurl2 + '/static/ced_main/images/created_docs/' + username1 + '_CSV_Query_Data_' + str(
                    nowf) + '.csv'
                csum = open(outputf, "wb")
                csum.close()
                csum = open(outputf, "ab")
                csum.write(
                    "Management Zone 1,Management Zone 2,Management Zone 3,Management Zone 4,Management Zone 5,Management Zone 6,Management Zone 7,Threat Ag Conversion,Threat Conifer Encroach,Threat Energy Develop,Threat Fire,Threat Free Roaming Equids,Threat Grazing and Range Management,Threat Infrastructure,Threat Small Pops,Threat Mining,Threat Noxious Weeds and Annual Grasses,Threat Recreation,Threat Sagebrush Elimination,Threat Urbanization,Population Baker,Population Bald Hills,Population Belt Mountains,Population Canada,Population Carbon,Population Central,Population Crab Creek,Population Dakotas,Population Eagle-S Routt,Population E Central,Population E Tavaputs Plateau,Population Jackson Hole,Population Klamath,Population Laramie,Population Meeker-White River,Population Middle Park,Population Moses Coulee,Population N Mono Lake,Population North Park,Population Northern Great Basin,Population Northern Montana,Population NW-Interior,Population Panguitch,Population Parachute Piceance Roan,Population Parker Mountain-Emery,Population Pine Nut,Population Powder River Basin,Population Quinn Canyon Range,Population S Mono Lake,Population S White River,Population Sawtooth,Population Sheeprock Mountains,Population Snake Salmon and Beaverhead,Population Southern Great Basin,Population Southwest Montana,Population Strawberry,Population Warm Springs Valley,Population Weiser,Population Western Great Basin,Population White Mountains,Population Wyoming Basin,Population Yakama Indian Nation,Population Yakama Training Center,Population Yellowstone Watershed,Population Anthro Mountain,Population West Tavaputs,BLM,BOR,County,DOD,DOE,NPS,NGO,Private,State,Tribe,USFWS,USFS,Other,BIA,Effort ID,Effort Name,Effort Link,Agency,Office,Plan or Project,Activity,SubActivity,Metric,Metric Value,Objectives,Implementation Status,Start Date,Finish Date,In Perpetuity,Activity Effective,Explain Activity Effectiveness,HLCAI,HLCLA,HLCRA,HLCRPM,HLCC,HLCVP,ANDERT,ANDEIO,ANDEQP,ANDEAM,Doc 1 Name,Doc 1 File Type,Doc 1 Description,Doc 1 Link,Doc 2 Name,Doc 2 File Type,Doc 2 Description,Doc 2 Link,Doc 3 Name,Doc 3 File Type,Doc 3 Description,Doc 3 Link,Doc 4 Name,Doc 4 File Type,Doc 4 Description,Doc 4 Link,Doc 5 Name,Doc 5 File Type,Doc 5 Description,Doc 5 Link,Notes\n")

                for uqtab in udl:
                    # create the line string
                    line = ""
                    try:
                        wafwas = wafwa_info.objects.values_list('WAFWA_Value', flat=True).filter(Project_ID=int(uqtab))
                    except:
                        wafwas = []
                    waf1 = ","
                    waf2 = ","
                    waf3 = ","
                    waf4 = ","
                    waf5 = ","
                    waf6 = ","
                    waf7 = ","
                    for waf in wafwas:
                        if waf == 1:
                            waf1 = "Zone 1,"
                        if waf == 2:
                            waf2 = "Zone 2,"
                        if waf == 3:
                            waf3 = "Zone 3,"
                        if waf == 4:
                            waf4 = "Zone 4,"
                        if waf == 5:
                            waf5 = "Zone 5,"
                        if waf == 6:
                            waf6 = "Zone 6,"
                        if waf == 7:
                            waf7 = "Zone 7,"
                    line = line + waf1 + waf2 + waf3 + waf4 + waf5 + waf6 + waf7

                    try:
                        threats = threavaltest.values_list('Threat', flat=True).filter(Project_ID=int(uqtab))
                    except:
                        threats = []

                    AgCon = ","
                    ConEnc = ","
                    EnDev = ","
                    Fire = ","
                    RoamEq = ","
                    GraRan = ","
                    Infra = ","
                    SmPop = ","
                    Mining = ","
                    NWAG = ","
                    Rec = ","
                    SageElim = ","
                    Urban = ","
                    for thr in threats:
                        if thr == 1:
                            AgCon = "Agricultural Conversion,"
                        if thr == 2:
                            ConEnc = "Conifer Encroachment,"
                        if thr == 3:
                            EnDev = "Energy Development,"
                        if thr == 4:
                            Fire = "Fire,"
                        if thr == 5:
                            RoamEq = "Free Roaming Equids,"
                        if thr == 6:
                            GraRan = "Grazing / Range Management,"
                        if thr == 7:
                            Infra = "Infrastructure,"
                        if thr == 8:
                            SmPop = "Isolated / Small Population Size,"
                        if thr == 9:
                            Mining = "Mining,"
                        if thr == 10:
                            NWAG = "Noxious Weeds / Annual Grasses,"
                        if thr == 11:
                            Rec = "Recreation,"
                        if thr == 12:
                            SageElim = "Sagebrush Elimination,"
                        if thr == 13:
                            Urban = "Urbanization,"

                    line = line + AgCon + ConEnc + EnDev + Fire + RoamEq + GraRan + Infra + SmPop + Mining + NWAG + Rec + SageElim + Urban

                    try:
                        pops = population_info.objects.values_list('Population_Value', flat=True).filter(
                            Project_ID=int(uqtab))
                    except:
                        pops = []

                    Baker = ','
                    BaldHills = ','
                    BeltMountains = ','
                    Canada = ','
                    Carbon = ','
                    Central = ','
                    CrabCreek = ','
                    Dakotas = ','
                    EagleSRoutt = ','
                    ECentral = ','
                    ETavaputsPlateau = ','
                    JacksonHole = ','
                    Klamath = ','
                    Laramie = ','
                    MeekerWhiteRiver = ','
                    MiddlePark = ','
                    MosesCoulee = ','
                    NMonoLake = ','
                    NorthPark = ','
                    NorthernGreatBasin = ','
                    NorthernMontana = ','
                    NWInterior = ','
                    Panguitch = ','
                    ParachutePiceanceRoan = ','
                    ParkerMountainEmery = ','
                    PineNut = ','
                    PowderRiverBasin = ','
                    QuinnCanyonRange = ','
                    SMonoLake = ','
                    SWhiteRiver = ','
                    Sawtooth = ','
                    SheeprockMountains = ','
                    SnakeSalmonandBeaverhead = ','
                    SouthernGreatBasin = ','
                    SouthwestMontana = ','
                    Strawberry = ','
                    WarmSpringsValley = ','
                    Weiser = ','
                    WesternGreatBasin = ','
                    WhiteMountains = ','
                    WyomingBasin = ','
                    YakamaIndianNation = ','
                    YakamaTrainingCenter = ','
                    YellowstoneWatershed = ','
                    AnthroMountain = ','
                    WestTavaputs = ','

                    for pop in pops:
                        if pop == 1:
                            Baker = 'Baker,'
                        if pop == 2:
                            BaldHills = 'Bald Hills,'
                        if pop == 3:
                            BeltMountains = 'Belt Mountains,'
                        if pop == 4:
                            Canada = 'Canada,'
                        if pop == 5:
                            Carbon = 'Carbon,'
                        if pop == 6:
                            Central = 'Central,'
                        if pop == 7:
                            CrabCreek = 'Crab Creek,'
                        if pop == 8:
                            Dakotas = 'Dakotas,'
                        if pop == 9:
                            EagleSRoutt = 'Eagle-S Routt,'
                        if pop == 10:
                            ECentral = 'E Central,'
                        if pop == 11:
                            ETavaputsPlateau = 'E Tavaputs Plateau,'
                        if pop == 12:
                            JacksonHole = 'Jackson Hole,'
                        if pop == 13:
                            Klamath = 'Klamath,'
                        if pop == 15:
                            Laramie = 'Laramie,'
                        if pop == 16:
                            MeekerWhiteRiver = 'Meeker-White River,'
                        if pop == 17:
                            MiddlePark = 'Middle Park,'
                        if pop == 18:
                            MosesCoulee = 'Moses Coulee,'
                        if pop == 19:
                            NMonoLake = 'N Mono Lake,'
                        if pop == 20:
                            NorthPark = 'North Park,'
                        if pop == 21:
                            NorthernGreatBasin = 'Northern Great Basin,'
                        if pop == 22:
                            NorthernMontana = 'Northern Montana,'
                        if pop == 23:
                            NWInterior = 'NW-Interior,'
                        if pop == 24:
                            Panguitch = 'Panguitch,'
                        if pop == 25:
                            ParachutePiceanceRoan = 'Parachute Piceance Roan,'
                        if pop == 26:
                            ParkerMountainEmery = 'Parker Mountain-Emery,'
                        if pop == 27:
                            PineNut = 'Pine Nut,'
                        if pop == 29:
                            PowderRiverBasin = 'Powder River Basin,'
                        if pop == 30:
                            QuinnCanyonRange = 'Quinn Canyon Range,'
                        if pop == 31:
                            SMonoLake = 'S Mono Lake,'
                        if pop == 32:
                            SWhiteRiver = 'S White River,'
                        if pop == 33:
                            Sawtooth = 'Sawtooth,'
                        if pop == 34:
                            SheeprockMountains = 'Sheeprock Mountains,'
                        if pop == 36:
                            SnakeSalmonandBeaverhead = 'Snake Salmon and Beaverhead,'
                        if pop == 37:
                            SouthernGreatBasin = 'Southern Great Basin,'
                        if pop == 38:
                            SouthwestMontana = 'Southwest Montana,'
                        if pop == 39:
                            Strawberry = 'Strawberry,'
                        if pop == 41:
                            WarmSpringsValley = 'Warm Springs Valley,'
                        if pop == 42:
                            Weiser = 'Weiser,'
                        if pop == 43:
                            WesternGreatBasin = 'Western Great Basin,'
                        if pop == 44:
                            WhiteMountains = 'White Mountains,'
                        if pop == 45:
                            WyomingBasin = 'Wyoming Basin,'
                        if pop == 46:
                            YakamaIndianNation = 'Yakama Indian Nation,'
                        if pop == 47:
                            YakamaTrainingCenter = 'Yakama Training Center,'
                        if pop == 48:
                            YellowstoneWatershed = 'Yellowstone Watershed,'
                        if pop == 49:
                            AnthroMountain = 'Anthro Mountain,'
                        if pop == 50:
                            WestTavaputs = 'West Tavaputs,'

                    line = line + Baker + BaldHills + BeltMountains + Canada + Carbon + Central + CrabCreek + Dakotas + EagleSRoutt + ECentral + ETavaputsPlateau + JacksonHole + Klamath + Laramie + MeekerWhiteRiver + MiddlePark + MosesCoulee + NMonoLake + NorthPark + NorthernGreatBasin + NorthernMontana + NWInterior + Panguitch + ParachutePiceanceRoan + ParkerMountainEmery + PineNut + PowderRiverBasin + QuinnCanyonRange + SMonoLake + SWhiteRiver + Sawtooth + SheeprockMountains + SnakeSalmonandBeaverhead + SouthernGreatBasin + SouthwestMontana + Strawberry + WarmSpringsValley + Weiser + WesternGreatBasin + WhiteMountains + WyomingBasin + YakamaIndianNation + YakamaTrainingCenter + YellowstoneWatershed + AnthroMountain + WestTavaputs

                    # Add Ownership Data
                    try:
                        owners = ownership_info.objects.values_list('Owner_Value', flat=True).filter(
                            Project_ID=int(uqtab))
                    except:
                        owners = []

                    BLM = ','
                    BOR = ','
                    County = ','
                    DOD = ','
                    DOE = ','
                    NPS = ','
                    NGO = ','
                    Private = ','
                    State = ','
                    Tribe = ','
                    USFWS = ','
                    USFS = ','
                    Other = ','
                    BIA = ','

                    for own in owners:
                        if own == 1:
                            BLM = 'BLM,'
                        if own == 2:
                            BOR = 'BOR,'
                        if own == 3:
                            County = 'County,'
                        if own == 4:
                            DOD = 'DOD,'
                        if own == 5:
                            DOE = 'DOE,'
                        if own == 6:
                            NPS = 'NPS,'
                        if own == 7:
                            NGO = 'NGO,'
                        if own == 8:
                            Private = 'Private,'
                        if own == 9:
                            State = 'State,'
                        if own == 10:
                            Tribe = 'Tribe,'
                        if own == 11:
                            USFWS = 'USFWS,'
                        if own == 12:
                            USFS = 'USFS,'
                        if own == 13:
                            Other = 'Other,'
                        if own == 14:
                            BIA = 'BIA,'

                    line = line + BLM + BOR + County + DOD + DOE + NPS + NGO + Private + State + Tribe + USFWS + USFS + Other + BIA
                    ### Add the effort data

                    # Add the effort ID
                    line = line + str(uqtab) + ","

                    # Add the effort name
                    prjname = project_info.objects.values_list('Project_Name', flat=True).get(Project_ID=int(uqtab))
                    prjname = prjname.replace(",", ";")
                    line = line + str(prjname) + ","

                    # Add the effort link
                    link = siteurl2 + '/sgce/' + str(uqtab) + '/viewproject/'
                    line = line + str(link) + ","

                    # Add the effort agency
                    agency = project_info.objects.values_list('Implementing_Party', flat=True).get(
                        Project_ID=int(uqtab))
                    line = line + str(agency) + ","

                    # Add the effort office
                    office = project_info.objects.values_list('Office', flat=True).get(Project_ID=int(uqtab))
                    line = line + str(office) + ","

                    # Add the type of activity
                    try:
                        ta = project_info.objects.values_list('TypeAct', flat=True).get(Project_ID=int(uqtab))
                    except:
                        ta = ""
                    line = line + str(ta) + ","

                    # Add the activity
                    try:
                        actvalue = str('Activity')
                        act = project_info.objects.values_list(actvalue, flat=True).get(Project_ID=int(uqtab))
                        act = str(act)
                        act = act.replace(",", ";")
                    except:
                        act = ""
                    line = line + str(act) + ","

                    # Add the subactivity
                    try:
                        sa = project_info.objects.values_list('SubActivity', flat=True).get(Project_ID=int(uqtab))
                        sa = str(sa)
                        sa = sa.replace(",", ";")
                    except:
                        sa = ""
                    line = line + str(sa) + ","

                    # Add the metrics
                    metvals = ['TotalAcres', 'TotalMiles', 'TotalEquids', 'TotalNumberBirds', 'TotalNumberRemoved']
                    for met in metvals:
                        metricvalue = -9999
                        metrictype = ""
                        try:
                            metricvalue = metrics.objects.values_list(str(met), flat=True).get(Project_ID=int(uqtab))
                            if metricvalue > 0:
                                metrictype = met
                                break
                        except:
                            metricvalue = -9999
                            metrictype = ""

                    line = line + str(metrictype) + "," + str(metricvalue) + ","

                    # Add the objectives
                    try:
                        ob = project_info.objects.values_list('Objectives_Desc', flat=True).get(Project_ID=int(uqtab))
                        ob = str(ob)
                        ob = ob.replace(",", ";")
                        ob = ob.replace("\r\n", " ")
                    except:
                        ob = ""
                    line = line + str(ob) + ","

                    # Add the implementation status
                    try:
                        impstat = implementation_info.objects.values_list('Imp_Status', flat=True).get(
                            Project_ID=int(uqtab))
                        if impstat == 1:
                            imps = "Planned"
                        elif impstat == 2:
                            imps = "In Progress"
                        else:
                            imps = "Completed"
                    except:
                        imps = ""

                    line = line + str(imps) + ","

                    # Add the start date
                    try:
                        sd = implementation_info.objects.values_list('Start_Date', flat=True).get(Project_ID=int(uqtab))
                    except:
                        sd = ""
                    line = line + str(sd) + ","

                    # Add the finish date
                    try:
                        fd = implementation_info.objects.values_list('Finish_Date', flat=True).get(
                            Project_ID=int(uqtab))
                    except:
                        fd = ""
                    line = line + str(fd) + ","

                    # Add in perpetuity
                    try:
                        inperp = implementation_info.objects.values_list('In_Perpetuity', flat=True).get(
                            Project_ID=int(uqtab))
                    except:
                        inperp = ""
                    line = line + str(inperp) + ","
                    # Add Effective_Determined
                    try:
                        effder = implementation_info.objects.values_list('Effective_Determined', flat=True).get(
                            Project_ID=int(uqtab))
                        if effder == 1:
                            effde = "Yes"
                        elif effder == 2:
                            effde = "Uncertain or Unlikely"
                        else:
                            effde = "Highly Likely"
                    except:
                        effder = ""
                    line = line + str(effde) + ","

                    # Add Effective_Explained
                    try:
                        effexp = implementation_info.objects.values_list('Effective_Explained', flat=True).get(
                            Project_ID=int(uqtab))
                        effexp = str(effexp)
                        effexp = effexp.replace(",", ";")
                        effexp = effexp.replace("\r\n", " ")

                    except:
                        effexp = ""
                    line = line + str(effexp) + ","

                    # Add Reas_Certain
                    try:
                        HLCAI = implementation_info.objects.values_list('Reas_Certain', flat=True).get(
                            Project_ID=int(uqtab))
                        HLCAI = gettext(HLCAI)
                    except:
                        HLCAI = ""
                    line = line + str(HLCAI) + ","

                    # Add Legal_Authority
                    try:
                        HLCLA = implementation_info.objects.values_list('Legal_Authority', flat=True).get(
                            Project_ID=int(uqtab))
                        HLCLA = gettext(HLCLA)
                    except:
                        HLCLA = ""
                    line = line + str(HLCLA) + ","

                    # Add Staff_Available
                    try:
                        HLCRA = implementation_info.objects.values_list('Staff_Available', flat=True).get(
                            Project_ID=int(uqtab))
                        HLCRA = gettext(HLCRA)
                    except:
                        HLCRA = ""
                    line = line + str(HLCRA) + ","

                    # Add Regulatory_Mech
                    try:
                        HLCRPM = implementation_info.objects.values_list('Regulatory_Mech', flat=True).get(
                            Project_ID=int(uqtab))
                        HLCRPM = gettext(HLCRPM)
                    except:
                        HLCRPM = ""
                    line = line + str(HLCRPM) + ","

                    # Add Compliance
                    try:
                        HLCC = implementation_info.objects.values_list('Compliance', flat=True).get(
                            Project_ID=int(uqtab))
                        HLCC = gettext(HLCC)
                    except:
                        HLCC = ""
                    line = line + str(HLCC) + ","

                    # Add Vol_Incentives
                    try:
                        HLCVP = implementation_info.objects.values_list('Vol_Incentives', flat=True).get(
                            Project_ID=int(uqtab))
                        HLCVP = gettext(HLCVP)
                    except:
                        HLCVP = ""
                    line = line + str(HLCVP) + ","

                    # Add Reduce_Threats
                    try:
                        ANDERT = implementation_info.objects.values_list('Reduce_Threats', flat=True).get(
                            Project_ID=int(uqtab))
                        ANDERT = gettext(ANDERT)
                    except:
                        ANDERT = ""
                    line = line + str(ANDERT) + ","

                    # Add in Incremental_Objectives
                    try:
                        ANDEIO = implementation_info.objects.values_list('Incremental_Objectives', flat=True).get(
                            Project_ID=int(uqtab))
                        ANDEIO = gettext(ANDEIO)
                    except:
                        ANDEIO = ""
                    line = line + str(ANDEIO) + ","

                    # Add Quantifiable_Measures
                    try:
                        ANDEQP = implementation_info.objects.values_list('Quantifiable_Measures', flat=True).get(
                            Project_ID=int(uqtab))
                        ANDEQP = gettext(ANDEQP)
                    except:
                        ANDEQP = ""
                    line = line + str(ANDEQP) + ","

                    # Add in AD_Strategy
                    try:
                        ANDEAM = implementation_info.objects.values_list('AD_Strategy', flat=True).get(
                            Project_ID=int(uqtab))
                        ANDEAM = gettext(ANDEAM)
                    except:
                        ANDEAM = ""
                    line = line + str(ANDEAM) + ","

                    ### Add Documentation
                    try:
                        docs = documentation.objects.values_list('id', flat=True).filter(Project_ID=int(uqtab))
                    except:
                        docs = []
                    doccnt = 0
                    ft1 = ""
                    fd1 = ""
                    fn1 = ""
                    fsb1 = ""
                    flk1 = ""
                    ft2 = ""
                    fd2 = ""
                    fn2 = ""
                    fsb2 = ""
                    flk2 = ""
                    ft3 = ""
                    fd3 = ""
                    fn3 = ""
                    fsb3 = ""
                    flk3 = ""
                    ft4 = ""
                    fd4 = ""
                    fn4 = ""
                    fsb4 = ""
                    flk4 = ""
                    ft5 = ""
                    fd5 = ""
                    fn5 = ""
                    fsb5 = ""
                    flk5 = ""
                    for doc in docs:

                        doccnt = doccnt + 1
                        if doccnt == 1:

                            try:
                                fd1 = documentation.objects.values_list('Document_Description', flat=True).get(
                                    id=int(doc))
                                fd1 = fd1.replace(",", ";")
                            except:
                                fd1 = ""

                            if fd1 != 'Spatial data from Batch Upload':

                                try:
                                    ft1 = documentation.objects.values_list('File_Type', flat=True).get(id=int(doc))
                                except:
                                    ft1 = ""
                                try:
                                    fn1 = documentation.objects.values_list('Document_Name', flat=True).get(id=int(doc))
                                    fn1 = fn1.replace(",", ";")
                                except:
                                    fn1 = ""
                                try:
                                    fsb1 = documentation.objects.values_list('LCMItem', flat=True).get(id=int(doc))
                                    flk1 = 'https://www.sciencebase.gov/catalog/file/get/' + str(fsb1)
                                except:
                                    fsb1 = ""
                            else:
                                fd1 = ""
                        elif doccnt == 2:
                            try:
                                fd2 = documentation.objects.values_list('Document_Description', flat=True).get(
                                    id=int(doc))
                                fd2 = fd2.replace(",", ";")
                            except:
                                fd2 = ""

                            if fd2 != 'Spatial data from Batch Upload':

                                try:
                                    ft2 = documentation.objects.values_list('File_Type', flat=True).get(id=int(doc))
                                except:
                                    ft2 = ""
                                try:
                                    fn2 = documentation.objects.values_list('Document_Name', flat=True).get(id=int(doc))
                                    fn2 = fn2.replace(",", ";")
                                except:
                                    fn2 = ""
                                try:
                                    fsb2 = documentation.objects.values_list('LCMItem', flat=True).get(id=int(doc))
                                    flk2 = 'https://www.sciencebase.gov/catalog/file/get/' + str(fsb2)
                                except:
                                    fsb2 = ""
                            else:
                                fd2 = ""
                        elif doccnt == 3:
                            try:
                                fd3 = documentation.objects.values_list('Document_Description', flat=True).get(
                                    id=int(doc))
                                fd3 = fd3.replace(",", ";")
                            except:
                                fd3 = ""

                            if fd3 != 'Spatial data from Batch Upload':

                                try:
                                    ft3 = documentation.objects.values_list('File_Type', flat=True).get(id=int(doc))
                                except:
                                    ft3 = ""
                                try:
                                    fn3 = documentation.objects.values_list('Document_Name', flat=True).get(id=int(doc))
                                    fn3 = fn3.replace(",", ";")
                                except:
                                    fn3 = ""
                                try:
                                    fsb3 = documentation.objects.values_list('LCMItem', flat=True).get(id=int(doc))
                                    flk3 = 'https://www.sciencebase.gov/catalog/file/get/' + str(fsb3)
                                except:
                                    fsb3 = ""
                            else:
                                fd3 = ""
                        elif doccnt == 4:
                            try:
                                fd4 = documentation.objects.values_list('Document_Description', flat=True).get(
                                    id=int(doc))
                                fd4 = fd4.replace(",", ";")
                            except:
                                fd4 = ""

                            if fd4 != 'Spatial data from Batch Upload':

                                try:
                                    ft4 = documentation.objects.values_list('File_Type', flat=True).get(id=int(doc))
                                except:
                                    ft4 = ""
                                try:
                                    fn4 = documentation.objects.values_list('Document_Name', flat=True).get(id=int(doc))
                                    fn4 = fn4.replace(",", ";")
                                except:
                                    fn4 = ""
                                try:
                                    fsb4 = documentation.objects.values_list('LCMItem', flat=True).get(id=int(doc))
                                    flk4 = 'https://www.sciencebase.gov/catalog/file/get/' + str(fsb4)
                                except:
                                    fsb4 = ""
                            else:
                                fd4 = ""
                        elif doccnt == 5:
                            try:
                                fd5 = documentation.objects.values_list('Document_Description', flat=True).get(
                                    id=int(doc))
                                fd5 = fd5.replace(",", ";")
                            except:
                                fd5 = ""

                            if fd5 != 'Spatial data from Batch Upload':

                                try:
                                    ft5 = documentation.objects.values_list('File_Type', flat=True).get(id=int(doc))
                                except:
                                    ft5 = ""
                                try:
                                    fn5 = documentation.objects.values_list('Document_Name', flat=True).get(id=int(doc))
                                    fn5 = fn5.replace(",", ";")
                                except:
                                    fn5 = ""
                                try:
                                    fsb5 = documentation.objects.values_list('LCMItem', flat=True).get(id=int(doc))
                                    flk5 = 'https://www.sciencebase.gov/catalog/file/get/' + str(fsb5)
                                except:
                                    fsb5 = ""
                            else:
                                fd5 = ""

                    line = line + str(fn1) + "," + str(ft1) + "," + str(fd1) + "," + str(flk1) + "," + str(
                        fn2) + "," + str(ft2) + "," + str(fd2) + "," + str(flk2) + "," + str(fn3) + "," + str(
                        ft3) + "," + str(fd3) + "," + str(flk3) + "," + str(fn4) + "," + str(ft4) + "," + str(
                        fd4) + "," + str(flk4) + "," + str(fn5) + "," + str(ft5) + "," + str(fd5) + "," + str(
                        flk5) + ","

                    # Add the objectives
                    try:
                        note = project_info.objects.values_list('Notes', flat=True).get(Project_ID=int(uqtab))
                        note = str(note)
                        note = note.replace(",", ";")
                        note = note.replace("\r\n", " ")
                    except:
                        note = ""
                    line = line + str(note) + "\n"

                    csum.write(line)

                csum.close()
                DataDown = "True"

            table = viewproject_table(project_info.objects.filter(Project_ID__in=uq))
            RequestConfig(request).configure(table)
            context = {'viewprojects': table, 'authen': authen, 'AgencyVal': AgencyVal, 'OfficeVal': OfficeVal,
                       'ImpStatVal': ImpStatVal, 'EffStatVal': EffStatVal, 'startYearVal': startYearVal,
                       'endYearVal': endYearVal, 'ActTypeVal': ActTypeVal, 'ActivityVal': ActivityVal,
                       'SubActVal': SubActVal, 'MetricVal': MetricVal, 'ThreatsVal': ThreatsVal, 'WAFWAVal': WAFWAVal,
                       'SGPopVal': SGPopVal, 'StateVal': StateVal, 'CountyVal': CountyVal, 'EntryVal': EntryVal,
                       'KeyWordVal': KeyWordVal, 'Records': Records, 'userAgency': userAgency, 'userOffice': userOffice,
                       'DataDown': DataDown, 'DataCSV': outputfshort, 'showlogin': 'True'}
            return render(request, 'ced_main/permission_denied.html', context)
        else:
            print(form.errors)
    else:
        form = query_Form()
        # if request.user.is_authenticated(): Pythoon 2.7
        if request.user.is_authenticated:
            context = {'authen': authen, 'form': form, 'showlogin': 'True'}
            return render(request, 'ced_main/permission_denied.html', context)
        else:
            return render(request, 'ced_main/permission_denied.html, context')

@login_required
def sgceddocumentation(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    DocumentFormSet = modelformset_factory(documentation, extra=0, form=documentation_display_Form)
    formset = DocumentFormSet(queryset=documentation.objects.all())
    context = {'authen': authen, 'formset': formset}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'ced_main/sgceddocumentation.html', context)
    else:
        return render(request, 'ced_main/permission_denied.html')


@login_required
def sgcedqueryresponse(request):
    authen = checkgroup(request.user.groups.values_list('name', flat=True))
    table = viewapprovalprojects_table(project_info.objects.all)
    RequestConfig(request).configure(table)
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        if authen == 'authenadmin' or authen == 'authenapp':
            context = {'viewprojects': table, 'authen': authen}
            return render(request, 'ced_main/viewqueryresults.html', context)
        else:
            return render(request, 'ced_main/permission_denied.html')
    else:
        return render(request, 'ced_main/permission_denied.html')


@login_required
def viewproject(request, prid):
    userAgency = userprofile.objects.values_list('Agency', flat=True).get(User_id=profile)
    userOffice = userprofile.objects.values_list('Field_Office', flat=True).get(User_id=profile)
    try:
        pid = project_info.objects.get(pk=prid)
    except:
        return redirect('/sgce/project_not_exists_temp/')
    authen = checkgroup(request.user.groups.values_list('name', flat=True))

    prjid = int(prid)
    prjname = project_info.objects.values_list('Project_Name', flat=True).get(Project_ID=prjid)
    officeval = project_info.objects.values_list('Office', flat=True).get(Project_ID=prjid)
    agencyval = project_info.objects.values_list('Implementing_Party', flat=True).get(Project_ID=prjid)
    typact = project_info.objects.values_list('TypeAct', flat=True).get(Project_ID=prjid)
    activity = project_info.objects.values_list('Activity', flat=True).get(Project_ID=prjid)
    subactivity = project_info.objects.values_list('SubActivity', flat=True).get(Project_ID=prjid)

    entrystat = 'None'
    entrytypes = [[1, 'Draft Record'], [2, 'Awaiting Approval'], [3, 'Approved'], [4, 'Marked for Deletion']]
    entryval = project_info.objects.values_list('Entry_Type', flat=True).get(Project_ID=prjid)
    for entryst, entryty in entrytypes:
        if int(entryval) == int(entryst):
            entrystat = entryty

    metric = "None"
    metrictxt = "None"
    metricvals = [['TotalAcres', 'Total Acres'], ['TotalMiles', 'Total Miles'],
                  ['TotalNumberBirds', 'Total Number of Birds'], ['TotalNumberRemoved', 'Total Number Removed'],
                  ['TotalEquids', 'Total Number of Equids']]

    for metr, metr1 in metricvals:
        try:
            metric = metrics.objects.values_list(metr, flat=True).get(Project_ID=prjid)
            metrictxt = metr1
            if metric > 0:
                break
            else:
                metric = "None"
        except:
            metric = "None"

    metric = str(metric)

    threatsf = "None"
    thrtxtfcnt = 0
    thri = threats.objects.values_list('Threat', flat=True).filter(Project_ID=prjid)
    for thr in thri:
        thrtxt = threat_values.objects.values_list('Threats', flat=True).get(id=thr)
        if thrtxtfcnt == 0:
            threatsf = str(thrtxt)
            thrtxtfcnt = 1
        else:
            threatsf = threatsf + ", " + str(thrtxt)

    wafwaz = "None"
    wafwazcnt = 0
    thri = wafwa_info.objects.values_list('WAFWA_Value', flat=True).filter(Project_ID=prjid)
    for thr in thri:
        thrtxt = wafwa_zone_values.objects.values_list('WAFWA_Zone', flat=True).get(id=thr)
        if wafwazcnt == 0:
            wafwaz = "Zone " + str(thrtxt)
            wafwazcnt = 1
        else:
            wafwaz = wafwaz + ", Zone " + str(thrtxt)

    sgpops = "None"
    sgpopscnt = 0
    thri = population_info.objects.values_list('Population_Value', flat=True).filter(Project_ID=prjid)
    for thr in thri:
        thrtxt = population_values.objects.values_list('Populations', flat=True).get(id=thr)
        if sgpopscnt == 0:
            sgpops = str(thrtxt)
            sgpopscnt = 1
        else:
            sgpops = sgpops + ", " + str(thrtxt)

    states1 = "None"
    states1cnt = 0
    thri = state_info.objects.values_list('State_Value', flat=True).filter(Project_ID=prjid)
    for thr in thri:
        thrtxt = state.objects.values_list('StateName', flat=True).get(id=thr)
        if states1cnt == 0:
            states1 = str(thrtxt)
            states1cnt = 1
        else:
            states1 = states1 + ", " + str(thrtxt)

    counties1 = "None"
    counties1cnt = 0
    thri = county_info.objects.values_list('County_Value', flat=True).filter(Project_ID=prjid)
    for thr in thri:
        thrtxt = state_county.objects.values_list('Cnty_St', flat=True).get(id=thr)
        if counties1cnt == 0:
            counties1 = str(thrtxt)
            counties1cnt = 1
        else:
            counties1 = counties1 + ", " + str(thrtxt)

    ownership1 = "None"
    ownership1cnt = 0
    thri = ownership_info.objects.values_list('Owner_Value', flat=True).filter(Project_ID=prjid)
    for thr in thri:
        thrtxt = ownership_values.objects.values_list('Owners', flat=True).get(id=thr)
        if ownership1cnt == 0:
            ownership1 = str(thrtxt)
            ownership1cnt = 1
        else:
            ownership1 = ownership1 + ", " + str(thrtxt)

    effortstat = 'None'
    statustypes = [[1, 'Planned'], [2, 'In Progress'], [3, 'Completed']]
    statval = implementation_info.objects.values_list('Imp_Status', flat=True).get(Project_ID=prjid)
    for statust, statusty in statustypes:
        if int(statval) == int(statust):
            effortstat = statusty

    strtdate = 'None'
    try:
        strtdate = implementation_info.objects.values_list('Start_Date', flat=True).get(Project_ID=prjid)
    except:
        strtdate = 'None'

    fnshdate = 'None'
    try:
        fnshdate = implementation_info.objects.values_list('Finish_Date', flat=True).get(Project_ID=prjid)
    except:
        fnshdate = 'None'

    inperp = 'None'
    try:
        inperp = str(implementation_info.objects.values_list('In_Perpetuity', flat=True).get(Project_ID=prjid))
    except:
        inperp = 'None'

    actdeemeff = 'None'
    try:
        actdeemeff = implementation_info.objects.values_list('Effective_Determined', flat=True).get(Project_ID=prjid)
        if actdeemeff == 1:
            actdeemeff = 'Yes: project plan or project is already effective.'
        elif actdeemeff == 3:
            actdeemeff = 'Highly Likely: project or plan is reasonably certain to be effective given adequate time.'
        else:
            actdeemeff = 'Uncertain or Unlikely: project or plan is uncertain or unlikely to be effective based on current information.'
    except:
        actdeemeff = 'None'

    objsexp = 'None'
    try:
        objsexp1 = project_info.objects.values_list('Objectives_Desc', flat=True).get(Project_ID=prjid)
        objsexp = "%s" % objsexp1
    except:
        objsexp = 'None'

    expleff = 'None'
    try:
        expleff1 = implementation_info.objects.values_list('Effective_Explained', flat=True).get(Project_ID=str(prjid))
        expleff = "%s" % expleff1

    except:
        expleff = 'None'

    docus = ""
    doccnt = 0
    docusv = documentation.objects.values_list('id', flat=True).filter(Project_ID=prjid)
    for docs in docusv:
        dft = documentation.objects.values_list('File_Type', flat=True).get(id=docs)
        dd1 = documentation.objects.values_list('Document_Description', flat=True).get(id=docs)
        dd = "%s" % dd1
        dn1 = documentation.objects.values_list('Document_Name', flat=True).get(id=docs)
        dn = "%s" % dn1
        if doccnt == 0:
            docus = str(dft) + ";,;" + str(dd) + ";,;" + str(dn) + ";,;" + str(docs)
        else:
            docus = docus + ",;," + str(dft) + ";,;" + str(dd) + ";,;" + str(dn) + ";,;" + str(docs)
        doccnt = 1

    if doccnt == 0:
        docus = 'None'

    cuser = 'None'
    try:
        cuser = project_info.objects.values_list('Created_By', flat=True).get(Project_ID=prjid)
    except:
        cuser = 'None'

    cuseremail = 'None'
    try:
        cuseremail = project_info.objects.values_list('User_Email', flat=True).get(Project_ID=prjid)
    except:
        cuseremail = 'None'

    upuser = 'None'
    try:
        upuser = project_info.objects.values_list('Updating_User', flat=True).get(Project_ID=prjid)
    except:
        upuser = 'None'

    upuseremail = 'None'
    try:
        upuseremail = User.objects.values_list('email').get(username=upuser)
        for upus in upuseremail:
            upuse1 = upus
        upuseremail = upuse1
    except:
        upuseremail = 'None'

    approvoff = 'None'
    try:
        approvoff = project_info.objects.values_list('Approving_Official', flat=True).get(Project_ID=prjid)
    except:
        approvoff = 'None'

    approvoffemail = 'None'
    try:
        approvoffemail = User.objects.values_list('email').get(username=approvoff)
        for upus in approvoffemail:
            upuse1 = upus
        approvoffemail = upuse1
    except:
        approvoffemail = 'None'

    notes2 = 'None'
    try:
        notes21 = project_info.objects.values_list('Notes', flat=True).get(Project_ID=prjid)
        notes2 = "%s" % notes21
    except:
        notes2 = 'None'

    LENCHOI = [[0, 'N/A'], [1, '0-4 Years'], [2, '5-9 Years'], [3, '10-14 Years'], [4, '15-19 Years'],
               [5, '20-24 Years'], [6, '25-29 Years'], [7, '>30 Years'], [8, 'In Perpetuity']]
    agreelength = 'None'
    try:
        agreelength = project_info.objects.values_list('Agreement_Length', flat=True).get(Project_ID=prjid)
        if int(agreelength) != 0:
            for LC in LENCHOI:
                if int(LC[0]) == int(agreelength):
                    agreelength = str(LC[1])
                    break
        else:
            agreelength = 'None'
    except:
        agreelength = 'None'

    earlyterm = 'None'
    try:
        earlyterm = project_info.objects.values_list('Agreement_Penalty', flat=True).get(Project_ID=prjid)
        if int(earlyterm) == 1:
            earlyterm = 'Yes'
        elif int(earlyterm) == 2:
            earlyterm = 'No'
        else:
            earlyterm = 'None'
    except:
        earlyterm = 'None'

    agreepro = [['Sage_Elim', 'Sagebrush Elimination'], ['Ag_Conv', 'Agricultural Conversion'],
                ['Improper_Graze', 'Improper Grazing'], ['Infastructure', 'Infrastructure'],
                ['Energy_Development', 'Energy Development'], ['Mining', 'Mining'], ['Recreation', 'Recreation'],
                ['Urbanization_SubDevel', 'Urbanization/Subdivision Development']]

    agpcnt = 0
    for agp in agreepro:
        try:
            value = agreement_protect.objects.values_list(str(agp[0]), flat=True).get(Project_ID=prjid)
        except:
            value = -1
        if value > 0 and value < 101:
            if agpcnt == 0:
                agproval = str(agp[1]) + " = " + str(value)
                agpcnt = 1
            else:
                agproval = agproval + ", " + str(agp[1]) + " = " + str(value)
    if agpcnt == 0:
        agproval = 'None'

    reascert = 'None'
    try:
        reascert = implementation_info.objects.values_list('Reas_Certain', flat=True).get(Project_ID=prjid)
        reascert = gettext1(reascert)
    except:
        reascert = 'None'

    legauth = 'None'
    try:
        legauth = implementation_info.objects.values_list('Legal_Authority', flat=True).get(Project_ID=prjid)
        legauth = gettext1(legauth)
    except:
        legauth = 'None'

    staffav = 'None'
    try:
        staffav = implementation_info.objects.values_list('Staff_Available', flat=True).get(Project_ID=prjid)
        staffav = gettext1(staffav)
    except:
        staffav = 'None'

    regmech = 'None'
    try:
        regmech = implementation_info.objects.values_list('Regulatory_Mech', flat=True).get(Project_ID=prjid)
        regmech = gettext1(regmech)
    except:
        regmech = 'None'

    comp = 'None'
    try:
        comp = implementation_info.objects.values_list('Compliance', flat=True).get(Project_ID=prjid)
        comp = gettext1(comp)
    except:
        comp = 'None'

    volinc = 'None'
    try:
        volinc = implementation_info.objects.values_list('Vol_Incentives', flat=True).get(Project_ID=prjid)
        volinc = gettext1(volinc)
    except:
        volinc = 'None'

    redthr = 'None'
    try:
        redthr = implementation_info.objects.values_list('Reduce_Threats', flat=True).get(Project_ID=prjid)
        redthr = gettext1(redthr)
    except:
        redthr = 'None'

    incobj = 'None'
    try:
        incobj = implementation_info.objects.values_list('Incremental_Objectives', flat=True).get(Project_ID=prjid)
        incobj = gettext1(incobj)
    except:
        incobj = 'None'

    quantmea = 'None'
    try:
        quantmea = implementation_info.objects.values_list('Quantifiable_Measures', flat=True).get(Project_ID=prjid)
        quantmea = gettext1(quantmea)
    except:
        quantmea = 'None'

    adst = 'None'
    try:
        adst = implementation_info.objects.values_list('AD_Strategy', flat=True).get(Project_ID=prjid)
        adst = gettext1(adst)
    except:
        adst = 'None'

    formset = ""
    FWSReviewFormSet = modelformset_factory(fwsreview, extra=0, form=fwsreview_display_Form)
    fwsqueryform = fwsreview.objects.filter(Project_ID=prjid)
    formset = FWSReviewFormSet(queryset=fwsqueryform)

    Authorize = 'False'

    if userAgency == 'U.S. Fish and Wildlife Service' or authen == 'authenadmin':
        Authorize = 'True'
    else:
        if userAgency == 'Bureau of Indian Affairs' or userAgency == 'Bureau of Land Management' or userAgency == 'U.S. Geological Survey' or userAgency == 'Natural Resource Conservation Service' or userAgency == 'U.S. Forest Service':
            if agencyval == userAgency:
                Authorize = 'True'
        else:
            if userOffice == officeval:
                Authorize = 'True'

    if Authorize == 'False':
        return render(request, 'ced_main/permission_denied.html')
    else:
        if request.method == 'POST':

            try:

                i = 1
                while i < 200000:
                    try:
                        dodown = "Download_" + str(i)
                        if dodown in request.POST:
                            docid = documentation.objects.values_list('LCMItem', flat=True).get(id=i)
                            url = "https://www.sciencebase.gov/catalog/item/" + str(docid)
                            logonpysbdoc, sbid = Login2SBandOpenFootprintStudio1(url, str(docid))
                            LCJason = "https://www.sciencebase.gov/catalog/file/get/" + str(
                                docid) + "?" + sbid + "&josso=" + str(logonpysbdoc) + "&;"
                            break
                        i = i + 1
                    except:
                        i = i + 1
            except:
                test = 'test'

            form = query_Form(request.POST)
            if form.is_valid():
                # if request.user.is_authenticated(): Pythoon 2.7
                if request.user.is_authenticated:
                    context = {'prjid': prjid, 'userAgency': userAgency, 'formset': formset, 'prjname': prjname,
                               'entrystat': entrystat, 'typact': typact, 'activity': activity,
                               'subactivity': subactivity, 'metric': metric, 'metrictxt': metrictxt,
                               'threatsf': threatsf, 'wafwaz': wafwaz, 'sgpops': sgpops, 'states1': states1,
                               'counties1': counties1, 'ownership1': ownership1, 'effortstat': effortstat,
                               'strtdate': strtdate, 'fnshdate': fnshdate, 'inperp': inperp, 'actdeemeff': actdeemeff,
                               'objsexp': objsexp, 'expleff': expleff, 'docus': docus, 'cuser': cuser,
                               'cuseremail': cuseremail, 'upuser': upuser, 'upuseremail': upuseremail,
                               'approvoff': approvoff, 'approvoffemail': approvoffemail, 'agreelength': agreelength,
                               'earlyterm': earlyterm, 'notes2': notes2, 'agproval': agproval, 'LCJason': LCJason,
                               'LCJasonDown': 'True', 'reascert': reascert, 'legauth': legauth, 'staffav': staffav,
                               'regmech': regmech, 'comp': comp, 'volinc': volinc, 'redthr': redthr, 'incobj': incobj,
                               'quantmea': quantmea, 'adst': adst}
                    return render(request, 'ced_main/viewproject.html', context)

                else:
                    return render(request, 'ced_main/permission_denied.html')

        else:
            # if request.user.is_authenticated(): Pythoon 2.7
            if request.user.is_authenticated:
                context = {'prjid': prjid, 'userAgency': userAgency, 'formset': formset, 'prjname': prjname,
                           'entrystat': entrystat, 'typact': typact, 'activity': activity, 'subactivity': subactivity,
                           'metric': metric, 'metrictxt': metrictxt, 'threatsf': threatsf, 'wafwaz': wafwaz,
                           'sgpops': sgpops, 'states1': states1, 'counties1': counties1, 'ownership1': ownership1,
                           'effortstat': effortstat, 'strtdate': strtdate, 'fnshdate': fnshdate, 'inperp': inperp,
                           'actdeemeff': actdeemeff, 'objsexp': objsexp, 'expleff': expleff, 'docus': docus,
                           'cuser': cuser, 'cuseremail': cuseremail, 'upuser': upuser, 'upuseremail': upuseremail,
                           'approvoff': approvoff, 'approvoffemail': approvoffemail, 'agreelength': agreelength,
                           'earlyterm': earlyterm, 'notes2': notes2, 'agproval': agproval, 'reascert': reascert,
                           'legauth': legauth, 'staffav': staffav, 'regmech': regmech, 'comp': comp, 'volinc': volinc,
                           'redthr': redthr, 'incobj': incobj, 'quantmea': quantmea, 'adst': adst}
                return render(request, 'ced_main/viewproject.html', context)

            else:
                return render(request, 'ced_main/permission_denied.html')


@login_required
def viewonlyproject(request, prid):
    userAgency = userprofile.objects.values_list('Agency', flat=True).get(User_id=profile)
    userOffice = userprofile.objects.values_list('Field_Office', flat=True).get(User_id=profile)
    try:
        pid = project_info.objects.get(pk=prid)
    except:
        return redirect('/sgce/project_not_exists_temp/')
    authen = checkgroup(request.user.groups.values_list('name', flat=True))

    prjid = int(prid)
    prjname = project_info.objects.values_list('Project_Name', flat=True).get(Project_ID=prjid)
    officeval = project_info.objects.values_list('Office', flat=True).get(Project_ID=prjid)
    agencyval = project_info.objects.values_list('Implementing_Party', flat=True).get(Project_ID=prjid)
    typact = project_info.objects.values_list('TypeAct', flat=True).get(Project_ID=prjid)
    activity = project_info.objects.values_list('Activity', flat=True).get(Project_ID=prjid)
    subactivity = project_info.objects.values_list('SubActivity', flat=True).get(Project_ID=prjid)

    entrystat = 'None'
    entrytypes = [[1, 'Draft Record'], [2, 'Awaiting Approval'], [3, 'Approved'], [4, 'Marked for Deletion']]
    entryval = project_info.objects.values_list('Entry_Type', flat=True).get(Project_ID=prjid)
    for entryst, entryty in entrytypes:
        if int(entryval) == int(entryst):
            entrystat = entryty

    metric = "None"
    metrictxt = "None"
    metricvals = [['TotalAcres', 'Total Acres'], ['TotalMiles', 'Total Miles'],
                  ['TotalNumberBirds', 'Total Number of Birds'], ['TotalNumberRemoved', 'Total Number Removed'],
                  ['TotalEquids', 'Total Number of Equids']]

    for metr, metr1 in metricvals:
        try:
            metric = metrics.objects.values_list(metr, flat=True).get(Project_ID=prjid)
            metrictxt = metr1
            if metric > 0:
                break
            else:
                metric = "None"
        except:
            metric = "None"

    metric = str(metric)

    threatsf = "None"
    thrtxtfcnt = 0
    thri = threats.objects.values_list('Threat', flat=True).filter(Project_ID=prjid)
    for thr in thri:
        thrtxt = threat_values.objects.values_list('Threats', flat=True).get(id=thr)
        if thrtxtfcnt == 0:
            threatsf = str(thrtxt)
            thrtxtfcnt = 1
        else:
            threatsf = threatsf + ", " + str(thrtxt)

    wafwaz = "None"
    wafwazcnt = 0
    thri = wafwa_info.objects.values_list('WAFWA_Value', flat=True).filter(Project_ID=prjid)
    for thr in thri:
        thrtxt = wafwa_zone_values.objects.values_list('WAFWA_Zone', flat=True).get(id=thr)
        if wafwazcnt == 0:
            wafwaz = "Zone " + str(thrtxt)
            wafwazcnt = 1
        else:
            wafwaz = wafwaz + ", Zone " + str(thrtxt)

    sgpops = "None"
    sgpopscnt = 0
    thri = population_info.objects.values_list('Population_Value', flat=True).filter(Project_ID=prjid)
    for thr in thri:
        thrtxt = population_values.objects.values_list('Populations', flat=True).get(id=thr)
        if sgpopscnt == 0:
            sgpops = str(thrtxt)
            sgpopscnt = 1
        else:
            sgpops = sgpops + ", " + str(thrtxt)

    states1 = "None"
    states1cnt = 0
    thri = state_info.objects.values_list('State_Value', flat=True).filter(Project_ID=prjid)
    for thr in thri:
        thrtxt = state.objects.values_list('StateName', flat=True).get(id=thr)
        if states1cnt == 0:
            states1 = str(thrtxt)
            states1cnt = 1
        else:
            states1 = states1 + ", " + str(thrtxt)

    counties1 = "None"
    counties1cnt = 0
    thri = county_info.objects.values_list('County_Value', flat=True).filter(Project_ID=prjid)
    for thr in thri:
        thrtxt = state_county.objects.values_list('Cnty_St', flat=True).get(id=thr)
        if counties1cnt == 0:
            counties1 = str(thrtxt)
            counties1cnt = 1
        else:
            counties1 = counties1 + ", " + str(thrtxt)

    ownership1 = "None"
    ownership1cnt = 0
    thri = ownership_info.objects.values_list('Owner_Value', flat=True).filter(Project_ID=prjid)
    for thr in thri:
        thrtxt = ownership_values.objects.values_list('Owners', flat=True).get(id=thr)
        if ownership1cnt == 0:
            ownership1 = str(thrtxt)
            ownership1cnt = 1
        else:
            ownership1 = ownership1 + ", " + str(thrtxt)

    effortstat = 'None'
    statustypes = [[1, 'Planned'], [2, 'In Progress'], [3, 'Completed']]
    statval = implementation_info.objects.values_list('Imp_Status', flat=True).get(Project_ID=prjid)
    for statust, statusty in statustypes:
        if int(statval) == int(statust):
            effortstat = statusty

    strtdate = 'None'
    try:
        strtdate = implementation_info.objects.values_list('Start_Date', flat=True).get(Project_ID=prjid)
    except:
        strtdate = 'None'

    fnshdate = 'None'
    try:
        fnshdate = implementation_info.objects.values_list('Finish_Date', flat=True).get(Project_ID=prjid)
    except:
        fnshdate = 'None'

    inperp = 'None'
    try:
        inperp = str(implementation_info.objects.values_list('In_Perpetuity', flat=True).get(Project_ID=prjid))
    except:
        inperp = 'None'

    actdeemeff = 'None'
    try:
        actdeemeff = implementation_info.objects.values_list('Effective_Determined', flat=True).get(Project_ID=prjid)
        if actdeemeff == 1:
            actdeemeff = 'Yes: project plan or project is already effective.'
        elif actdeemeff == 3:
            actdeemeff = 'Highly Likely: project or plan is reasonably certain to be effective given adequate time.'
        else:
            actdeemeff = 'Uncertain or Unlikely: project or plan is uncertain or unlikely to be effective based on current information.'
    except:
        actdeemeff = 'None'

    objsexp = 'None'
    try:
        objsexp1 = project_info.objects.values_list('Objectives_Desc', flat=True).get(Project_ID=prjid)
        objsexp = "%s" % objsexp1
    except:
        objsexp = 'None'

    expleff = 'None'
    try:
        expleff1 = implementation_info.objects.values_list('Effective_Explained', flat=True).get(Project_ID=str(prjid))
        expleff = "%s" % expleff1

    except:
        expleff = 'None'

    docus = ""
    doccnt = 0
    docusv = documentation.objects.values_list('id', flat=True).filter(Project_ID=prjid)
    for docs in docusv:
        dft = documentation.objects.values_list('File_Type', flat=True).get(id=docs)
        dd1 = documentation.objects.values_list('Document_Description', flat=True).get(id=docs)
        dd = "%s" % dd1
        dn1 = documentation.objects.values_list('Document_Name', flat=True).get(id=docs)
        dn = "%s" % dn1
        if doccnt == 0:
            docus = str(dft) + "," + str(dd) + "," + str(dn) + "," + str(docs)
        else:
            docus = docus + ",," + str(dft) + "," + str(dd) + "," + str(dn) + "," + str(docs)
        doccnt = 1

    if doccnt == 0:
        docus = 'None'

    cuser = 'None'
    try:
        cuser = project_info.objects.values_list('Created_By', flat=True).get(Project_ID=prjid)
    except:
        cuser = 'None'

    cuseremail = 'None'
    try:
        cuseremail = project_info.objects.values_list('User_Email', flat=True).get(Project_ID=prjid)
    except:
        cuseremail = 'None'

    upuser = 'None'
    try:
        upuser = project_info.objects.values_list('Updating_User', flat=True).get(Project_ID=prjid)
    except:
        upuser = 'None'

    upuseremail = 'None'
    try:
        upuseremail = User.objects.values_list('email').get(username=upuser)
        for upus in upuseremail:
            upuse1 = upus
        upuseremail = upuse1
    except:
        upuseremail = 'None'

    approvoff = 'None'
    try:
        approvoff = project_info.objects.values_list('Approving_Official', flat=True).get(Project_ID=prjid)
    except:
        approvoff = 'None'

    approvoffemail = 'None'
    try:
        approvoffemail = User.objects.values_list('email').get(username=approvoff)
        for upus in approvoffemail:
            upuse1 = upus
        approvoffemail = upuse1
    except:
        approvoffemail = 'None'

    notes2 = 'None'
    try:
        notes21 = project_info.objects.values_list('Notes', flat=True).get(Project_ID=prjid)
        notes2 = "%s" % notes21
    except:
        notes2 = 'None'

    LENCHOI = [[0, 'N/A'], [1, '0-4 Years'], [2, '5-9 Years'], [3, '10-14 Years'], [4, '15-19 Years'],
               [5, '20-24 Years'], [6, '25-29 Years'], [7, '>30 Years'], [8, 'In Perpetuity']]
    agreelength = 'None'
    try:
        agreelength = project_info.objects.values_list('Agreement_Length', flat=True).get(Project_ID=prjid)
        if int(agreelength) != 0:
            for LC in LENCHOI:
                if int(LC[0]) == int(agreelength):
                    agreelength = str(LC[1])
                    break
        else:
            agreelength = 'None'
    except:
        agreelength = 'None'

    earlyterm = 'None'
    try:
        earlyterm = project_info.objects.values_list('Agreement_Penalty', flat=True).get(Project_ID=prjid)
        if int(earlyterm) == 1:
            earlyterm = 'Yes'
        elif int(earlyterm) == 2:
            earlyterm = 'No'
        else:
            earlyterm = 'None'
    except:
        earlyterm = 'None'

    agreepro = [['Sage_Elim', 'Sagebrush Elimination'], ['Ag_Conv', 'Agricultural Conversion'],
                ['Improper_Graze', 'Improper Grazing'], ['Infastructure', 'Infrastructure'],
                ['Energy_Development', 'Energy Development'], ['Mining', 'Mining'], ['Recreation', 'Recreation'],
                ['Urbanization_SubDevel', 'Urbanization/Subdivision Development']]

    agpcnt = 0
    for agp in agreepro:
        try:
            value = agreement_protect.objects.values_list(str(agp[0]), flat=True).get(Project_ID=prjid)
        except:
            value = -1
        if value > 0 and value < 101:
            if agpcnt == 0:
                agproval = str(agp[1]) + " = " + str(value)
                agpcnt = 1
            else:
                agproval = agproval + ", " + str(agp[1]) + " = " + str(value)
    if agpcnt == 0:
        agproval = 'None'

    reascert = 'None'
    try:
        reascert = implementation_info.objects.values_list('Reas_Certain', flat=True).get(Project_ID=prjid)
        reascert = gettext1(reascert)
    except:
        reascert = 'None'

    legauth = 'None'
    try:
        legauth = implementation_info.objects.values_list('Legal_Authority', flat=True).get(Project_ID=prjid)
        legauth = gettext1(legauth)
    except:
        legauth = 'None'

    staffav = 'None'
    try:
        staffav = implementation_info.objects.values_list('Staff_Available', flat=True).get(Project_ID=prjid)
        staffav = gettext1(staffav)
    except:
        staffav = 'None'

    regmech = 'None'
    try:
        regmech = implementation_info.objects.values_list('Regulatory_Mech', flat=True).get(Project_ID=prjid)
        regmech = gettext1(regmech)
    except:
        regmech = 'None'

    comp = 'None'
    try:
        comp = implementation_info.objects.values_list('Compliance', flat=True).get(Project_ID=prjid)
        comp = gettext1(comp)
    except:
        comp = 'None'

    volinc = 'None'
    try:
        volinc = implementation_info.objects.values_list('Vol_Incentives', flat=True).get(Project_ID=prjid)
        volinc = gettext1(volinc)
    except:
        volinc = 'None'

    redthr = 'None'
    try:
        redthr = implementation_info.objects.values_list('Reduce_Threats', flat=True).get(Project_ID=prjid)
        redthr = gettext1(redthr)
    except:
        redthr = 'None'

    incobj = 'None'
    try:
        incobj = implementation_info.objects.values_list('Incremental_Objectives', flat=True).get(Project_ID=prjid)
        incobj = gettext1(incobj)
    except:
        incobj = 'None'

    quantmea = 'None'
    try:
        quantmea = implementation_info.objects.values_list('Quantifiable_Measures', flat=True).get(Project_ID=prjid)
        quantmea = gettext1(quantmea)
    except:
        quantmea = 'None'

    adst = 'None'
    try:
        adst = implementation_info.objects.values_list('AD_Strategy', flat=True).get(Project_ID=prjid)
        adst = gettext1(adst)
    except:
        adst = 'None'

    Authorize = 'True'

    if userAgency != 'U.S. Fish and Wildlife Service' or authen != 'authenadmin':
        if userAgency != agencyval:
            Authorize = 'False'

    if userAgency == 'Bureau of Indian Affairs' or userAgency == 'Bureau of Land Management' or userAgency == 'U.S. Geological Survey' or userAgency == 'Natural Resource Conservation Service' or userAgency == 'U.S. Forest Service' or userAgency == 'U.S. Fish and Wildlife Service' or authen != 'authenadmin':
        test = "test"
    else:
        if userOffice != officeval:
            Authorize = 'False'

    formset = ""
    FWSReviewFormSet = modelformset_factory(fwsreview, extra=0, form=fwsreview_display_Form)
    fwsqueryform = fwsreview.objects.filter(Project_ID=prjid)
    formset = FWSReviewFormSet(queryset=fwsqueryform)

    if Authorize == 'False':
        return render(request, 'ced_main/permission_denied.html')
    else:
        if request.method == 'POST':

            try:

                i = 1
                while i < 200000:
                    try:
                        # dest1 = documentation.objects.values_list('id', flat=True).get(id=i)
                        dodown = "Download_" + str(i)

                        if dodown in request.POST:
                            docid = documentation.objects.values_list('LCMItem', flat=True).get(id=i)
                            url = "https://www.sciencebase.gov/catalog/item/" + str(docid)
                            logonpysbdoc, sbid = Login2SBandOpenFootprintStudio1(url, str(docid))
                            LCJason = "https://www.sciencebase.gov/catalog/file/get/" + str(
                                docid) + "?" + sbid + "&josso=" + str(logonpysbdoc) + "&;"
                            break
                        i = i + 1
                    except:
                        i = i + 1
            except:
                test = 'test'

            form = query_Form(request.POST)
            if form.is_valid():
                # if request.user.is_authenticated(): Pythoon 2.7
                if request.user.is_authenticated:
                    context = {'prjid': prjid, 'formset': formset, 'userAgency': userAgency, 'prjname': prjname,
                               'entrystat': entrystat, 'typact': typact, 'activity': activity,
                               'subactivity': subactivity, 'metric': metric, 'metrictxt': metrictxt,
                               'threatsf': threatsf, 'wafwaz': wafwaz, 'sgpops': sgpops, 'states1': states1,
                               'counties1': counties1, 'ownership1': ownership1, 'effortstat': effortstat,
                               'strtdate': strtdate, 'fnshdate': fnshdate, 'inperp': inperp, 'actdeemeff': actdeemeff,
                               'objsexp': objsexp, 'expleff': expleff, 'docus': docus, 'cuser': cuser,
                               'cuseremail': cuseremail, 'upuser': upuser, 'upuseremail': upuseremail,
                               'approvoff': approvoff, 'approvoffemail': approvoffemail, 'agreelength': agreelength,
                               'earlyterm': earlyterm, 'notes2': notes2, 'agproval': agproval, 'LCJason': LCJason,
                               'LCJasonDown': 'True', 'reascert': reascert, 'legauth': legauth, 'staffav': staffav,
                               'regmech': regmech, 'comp': comp, 'volinc': volinc, 'redthr': redthr, 'incobj': incobj,
                               'quantmea': quantmea, 'adst': adst}
                    return render(request, 'ced_main/viewonlyproject.html', context)

                else:
                    return render(request, 'ced_main/permission_denied.html')

        else:
            # if request.user.is_authenticated(): Pythoon 2.7
            if request.user.is_authenticated:
                context = {'prjid': prjid, 'formset': formset, 'userAgency': userAgency, 'prjname': prjname,
                           'entrystat': entrystat, 'typact': typact, 'activity': activity, 'subactivity': subactivity,
                           'metric': metric, 'metrictxt': metrictxt, 'threatsf': threatsf, 'wafwaz': wafwaz,
                           'sgpops': sgpops, 'states1': states1, 'counties1': counties1, 'ownership1': ownership1,
                           'effortstat': effortstat, 'strtdate': strtdate, 'fnshdate': fnshdate, 'inperp': inperp,
                           'actdeemeff': actdeemeff, 'objsexp': objsexp, 'expleff': expleff, 'docus': docus,
                           'cuser': cuser, 'cuseremail': cuseremail, 'upuser': upuser, 'upuseremail': upuseremail,
                           'approvoff': approvoff, 'approvoffemail': approvoffemail, 'agreelength': agreelength,
                           'earlyterm': earlyterm, 'notes2': notes2, 'agproval': agproval, 'reascert': reascert,
                           'legauth': legauth, 'staffav': staffav, 'regmech': regmech, 'comp': comp, 'volinc': volinc,
                           'redthr': redthr, 'incobj': incobj, 'quantmea': quantmea, 'adst': adst}
                return render(request, 'ced_main/viewonlyproject.html', context)

            else:
                return render(request, 'ced_main/permission_denied.html')


def redirectpg(request):
    return render(request, 'ced_main/redirectpg.html')
