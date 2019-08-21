from django.shortcuts import *
from django.http import *
from accounts.views import checkgroup
from ced_main.views import checkauthorization, ClipFeates
from ced_main.models import state_info, county_info, wafwa_info, population_info, project_info, state, state_county, wafwa_zone_values, population_values
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.contrib.auth.decorators import login_required
# from django.core.urlresolvers import resolve python 2.7
from django.urls import resolve
from django.utils import timezone

### Import packages for footprint editor
import json
import os
import datetime
# import arcpy
import urllib
# import urllib2
import codecs

now = datetime.datetime.utcnow()
now = now.replace(tzinfo=timezone.utc)

def getsruname(sruid):
    srulist = (('1', 'OR: Trout Creeks'), ('2', 'OR: Beatys'), ('3', 'OR: Louse - Soldier'), ('4', 'OR: Steens - Pueblos'), ('5', 'OR: Warners - Tucker'), ('6', 'OR: Picture Rock'), ('7', 'OR: Dry Valley'), ('8', 'OR: Alvord - Folly'), ('9', 'OR: Cow Lakes'), ('10', 'OR: Crowley'), ('11', 'OR: Brothers'), ('12', 'OR: Burns'), ('13', 'OR: Drewsey'), ('14', 'OR: Paulina'), ('15', 'OR: Prineville'), ('16', 'OR: Bully - Cow Valley'), ('17', 'OR: Baker'), ('18', 'ID: Bear Lake'), ('19', 'ID: Bennett Hills'), ('20', 'ID: Timmerman Hills'), ('21', 'ID: Craters of the Moon'), ('22', 'ID: Big Desert'), ('23', 'ID: Antelope Flats_Big Lost'), ('24', 'ID: Little Lost_Pahsimeroi'), ('25', 'ID: Hat Creek_Morgan Creek'), ('26', 'ID: Lemhi River'), ('27', 'ID: Inside Desert'), ('28', 'ID: Goose Creek'), ('29', 'ID: Upper Raft River Valley'), ('30', 'ID: Greater Curlew'), ('31', 'ID: Weiser'), ('9', 'ID: Cow Lakes'), ('33', 'ID: Muldoon'), ('34', 'ID: Browns Bench'), ('35', 'ID: East Idaho Upland'), ('36', 'ID: Antelope Ridge'), ('37', 'ID: Owyhee Canyonlands'), ('38', 'ID: Owyhee Desert'), ('3', 'ID: Soldier Creek'), ('3', 'ID: Louse Canyon'), ('41', 'ID: Sand Creek'), ('42', 'ID: Medicine Lodge'), ('43', 'ID: Twin Buttes'))

    for sru in srulist:
        sruexists = 0
        if str(sruid) == str(sru[0]):
            sruexists = 1
            return(str(sru[1]))

    if sruexists == 0:
        return('No Name Found')

def QueryESRIFeatureServiceReturnFeatureSet(strAGS_URL, strToken, strWhere, strFields):
  try:
    strBaseURL= strAGS_URL + "/query"
    strQuery = "?where={}&outFields={}&returnGeometry=true&f=json&token={}".format(strWhere, strFields, strToken)
    strFsURL = strBaseURL + strQuery
    # fs = arcpy.FeatureSet()
    # fs.load(strFsURL)

    return fs
  except Exception as e:
      import traceback, sys# If an error occurred, print line number and error message
      tb = sys.exc_info()[2]
      print("QueryESRIFeatureServiceReturnFeatureSet: Line %i" % tb.tb_lineno)
      print(e.message)
      return "error"

def GenerateTokenFromAGOL(gtUrl, strUsername, strPassword, strRefer):
    try:
        print("getting AGOL Token")
        gtValues = {'username' : strUsername,
        'password' : strPassword,
        'referer' : strRefer,
        'f' : 'json' }

        gtData = urllib.parse.urlencode(gtValues).encode("utf-8")
        gtRequest = urllib.request.Request(gtUrl, gtData)
        gtResponse = urllib.request.urlopen(gtRequest)#.read().decode('UTF-8')
        reader = codecs.getreader("utf-8")
        gtJson = json.load(reader(gtResponse))
        # print(gtJson)

        if (gtJson == None):
            print("no json generated")

        if "token" not in gtJson:
            print(gtJson['messages'])
            exit()
        else:
            print("AGS token acquired")
            return gtJson['token']        # Return the token to the function which called for it
    except Exception as e:
          import traceback, sys# If an error occurred, print(line number and error message
          tb = sys.exc_info()[2]
          print("GenerateTokenFromAGOL: Line %i" % tb.tb_lineno)
          print(e.message)

@xframe_options_sameorigin
def index(request):
    return render(request, 'grsgmap/index.html')

@xframe_options_sameorigin
def CEDPSummary(request):
    return render(request, 'grsgmap/CEDPSummary.html')

@xframe_options_sameorigin
def proxy(request):
    return render(request, 'grsgmap/proxy.jsp')

@xframe_options_sameorigin
def Tindex(request):
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    context = {'authen':authen}
    # if request.user.is_authenticated(): Pythoon 2.7
    if request.user.is_authenticated:
        return render(request, 'grsgmap/Tindex.html', context)
    else:
        return render(request, 'ced_main/permission_denied.html')

@xframe_options_sameorigin
@login_required
def footprinteditor(request, prid):
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    authuser = checkauthorization(prid, request.user)

    if request.method == 'POST':
        # DT_Start = datetime.datetime.now()

        username = request.user.username
        pid = project_info.objects.get(pk=prid)
        
        counties1 = request.POST.get("countyvals")
        if len(str(counties1)) > 0:
            try:
                pidcnty = county_info.objects.values_list('id', flat=True).get(Project_ID=prid)
                idcnty = county_info.objects.values_list('county_value', flat=True).filter(Project_ID=prid)
                for idc in idcnty:
                    county_info.objects.filter(Project_ID=prid, county_value=idc).delete()
                pidcnty = county_info.objects.values_list('id', flat=True).get(Project_ID=prid)
            except:
                cntyc = county_info()
                cntyc.Project_ID = pid
                cntyc.Date_Entered = now
                cntyc.User = str(username)
                cntyc.save()
                pidcnty = county_info.objects.values_list('id', flat=True).get(Project_ID=prid)
            
            cntyids = []
            counties = counties1.split(",")
            for c in counties:
                csplit = c.split(":")
                cnty = csplit[0]
                stat = csplit[1]

                statlist = [['AZ', 'Arizona'], ['CA', 'California'], ['CO', 'Colorado'], ['ID', 'Idaho'], ['MT', 'Montana'], ['ND', 'North Dakota'], ['NE', 'Nebraksa'], ['NV', 'Nevada'], ['OR', 'Oregon'], ['SD', 'South Dakota'], ['UT', 'Utah'], ['WA', 'Washington'], ['WY', 'Wyoming'], ['AB', 'Alberta'], ['SK', 'Saskatchewan']]

                for sl in statlist:
                    if sl[1] == stat:
                        cntval = cnty + ", " + sl[0]
                        break
                try:
                    cntyids.append(state_county.objects.values_list('id', flat=True).get(Cnty_St=cntval))
                except:
                    a=1
            
            cntym = county_info.objects.get(pk=pidcnty)
            cntym.Project_ID = pid
            cntym.Date_Entered = now
            cntym.county_value.set(cntyids)
            cntym.User = str(username)
            cntym.save()

        states = request.POST.get("statevals")
        if len(str(states)) > 0:
            try:
                pidstt = state_info.objects.values_list('id', flat=True).get(Project_ID=prid)
                idstt = state_info.objects.values_list('state_value', flat=True).filter(Project_ID=prid)
                for ids in idstt:
                    state_info.objects.filter(Project_ID=prid, state_value=ids).delete()
                pidstt = state_info.objects.values_list('id', flat=True).get(Project_ID=prid)
            except:
                sttc = state_info()
                sttc.Project_ID = pid
                sttc.Date_Entered = now
                sttc.User = str(username)
                sttc.save()
                pidstt = state_info.objects.values_list('id', flat=True).get(Project_ID=prid)
            sttids = []
            states1 = states.split(",")
            for s in states1:
                try:
                    sttids.append(state.objects.values_list('id', flat=True).get(StateName=s))
                except:
                    a=1
            sttm = state_info.objects.get(pk=pidstt)
            sttm.Project_ID = pid
            sttm.Date_Entered = now
            sttm.state_value.set(sttids)
            sttm.User = str(username)
            sttm.save()

        mzs = request.POST.get("mzvals")
        if len(str(mzs)) > 0:
            try:
                pidwaf = wafwa_info.objects.values_list('id', flat=True).get(Project_ID=prid)
                idwaf = wafwa_info.objects.values_list('wafwa_value', flat=True).filter(Project_ID=prid)
                for idw in idwaf:
                    wafwa_info.objects.filter(Project_ID=prid, wafwa_value=idw).delete()
                pidwaf = wafwa_info.objects.values_list('id', flat=True).get(Project_ID=prid)
            except:
                wafc = wafwa_info()
                wafc.Project_ID = pid
                wafc.Date_Entered = now
                wafc.User = str(username)
                wafc.save()
                pidwaf = wafwa_info.objects.values_list('id', flat=True).get(Project_ID=prid)
            
            wafids = []
            wafwas = mzs.split(",")
            for w in wafwas:
                w1 = w.replace("MZ ", "")
                wafids.append(wafwa_zone_values.objects.values_list('id', flat=True).get(WAFWA_Zone=w1))
            
            wafm = wafwa_info.objects.get(pk=pidwaf)
            wafm.Project_ID = pid
            wafm.Date_Entered = now
            wafm.wafwa_value.set(wafids)
            wafm.User = str(username)
            wafm.save()

        grsg = request.POST.get("grsgpopvals")
        if len(str(grsg)) > 0:
            pcnt = 0
            try:
                pidpop = population_info.objects.values_list('id', flat=True).get(Project_ID=prid)
                idpop = population_info.objects.values_list('population_value', flat=True).filter(Project_ID=prid)
                for idp in idpop:
                    population_info.objects.filter(Project_ID=prid, population_value=idp).delete()
                pidpop = population_info.objects.values_list('id', flat=True).get(Project_ID=prid)

            except:
                popc = population_info()
                popc.Project_ID = pid
                popc.Date_Entered = now
                popc.User = str(username)
                popc.save()

                pidpop = population_info.objects.values_list('id', flat=True).get(Project_ID=prid)

            popids = []
            pops = grsg.split(";")
            for p in pops:
                popids.append(population_values.objects.values_list('id', flat=True).get(Pop_Name=p))

            popm = population_info.objects.get(pk=pidpop)
            popm.Project_ID = pid
            popm.Date_Entered = now
            popm.population_value.set(popids)
            popm.User = str(username)
            popm.save()

        area = request.POST.get("areavals")
        if len(str(area)) > 0:
            poppi = project_info.objects.get(pk=prid)
            poppi.GIS_Acres = abs(float(area))
            poppi.save()

        return redirect('/sgce/' + prid + '/editproject/?step=Location')
    else:
        fullpath = str(request.get_full_path)
        splitpath = fullpath.split('/')
        prjidcnt = 0
        for sp in splitpath:
            spcheck = sp.split('=')
            if spcheck[0] == '?CEDID':
                sp1 = spcheck[1]
                sp1 = sp1[0:5]
                try:
                    int(sp1)
                except:
                    sp1 = sp1[0:4]
                    try:
                        int(sp1)
                    except:
                        sp1 = sp1[0:3]
                        try:
                            int(sp1)
                        except:
                            sp1 = sp1[0:2]
            else:
                sp1 = sp

            if str(sp1) == str(prid):
                prjidcnt = prjidcnt + 1

        if authen == 'authenadmin' or authen == 'authenapp' or authuser == 'Authorized':
            if prjidcnt == 2:
                context = {'authen':authen}
                return render(request, 'grsgmap/footprinteditor.html', context)
            else:
                context = {'authen':authen}
                return render(request, 'ced_main/permission_denied.html', context)
        else:
            context = {'authen':authen}
            return render(request, 'ced_main/permission_denied.html', context)


@xframe_options_sameorigin
@login_required
def SRUEditor(request, prid):
    authen = checkgroup(request.user.groups.values_list('name',flat=True))
    authuser = checkauthorization(prid, request.user)

    if request.method == 'POST':
        # DT_Start = datetime.datetime.now()

        username = request.user.username
        pid = project_info.objects.get(pk=prid)

        sru = project_info.objects.get(pk=prid)

        sruid = request.POST.get("sruid")

        sru.SRU_ID = sruid
        sruname = getsruname(str(sruid))
        sru.SRU_Name = sruname
        sru.save()

        return redirect('/sgce/' + prid + '/editproject/?step=Location')
    else:

        if authen == 'authenadmin' or authen == 'authenapp' or authuser == 'Authorized':
            context = {'authen':authen}
            return render(request, 'grsgmap/SRUEditor.html', context)
        else:
            context = {'authen':authen}
            return render(request, 'ced_main/permission_denied.html', context)