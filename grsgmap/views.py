from django.shortcuts import *
from django.http import *
from accounts.views import checkgroup
from ced_main.views import checkauthorization, ClipFeates
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.contrib.auth.decorators import login_required
# from django.core.urlresolvers import resolve python 2.7
from django.urls import resolve

### Import packages for footprint editor
import json
import os
import datetime
import arcpy
import urllib
# import urllib2
import codecs
#from django.conf import settings

def QueryESRIFeatureServiceReturnFeatureSet(strAGS_URL, strToken, strWhere, strFields):
  try:
    strBaseURL= strAGS_URL + "/query"
    strQuery = "?where={}&outFields={}&returnGeometry=true&f=json&token={}".format(strWhere, strFields, strToken)
    strFsURL = strBaseURL + strQuery
    fs = arcpy.FeatureSet()
    fs.load(strFsURL)

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
    basedir = os.path.dirname(os.path.dirname(__file__))
    with open(basedir + '\config\sgceConfig.json', 'r') as f:
        config = json.load(f)
        strAGOLUsername = config['DEFAULT']['AGOLUsername']
        strAGOLPassword = config['DEFAULT']['AGOLPassword']

    if request.method == 'POST':
        DT_Start = datetime.datetime.now()

        strProjectID = str(prid)
        strQuery = "Project_ID=" + strProjectID
        current_url = resolve(request.path_info).url_name
     
        if current_url == 'conservationeffforts.org':
            strAGS_URL = "https://services.arcgis.com/QVENGdaPbd4LUkLV/arcgis/rest/services/NA_SRC_v2/FeatureServer/5" # Production
        else:
            strAGS_URL = "https://services.arcgis.com/QVENGdaPbd4LUkLV/arcgis/rest/services/Development_Src_v2/FeatureServer/0" # Development
        
        strToken = GenerateTokenFromAGOL("https://usgs.maps.arcgis.com/sharing/rest/generateToken", strAGOLUsername, strAGOLPassword, "https://usgs.maps.arcgis.com") #"https://fws.maps.arcgis.com"
        pFS_Result = QueryESRIFeatureServiceReturnFeatureSet(strAGS_URL, strToken, strQuery, "Project_ID")

        clipf = ClipFeates(pFS_Result, strProjectID, request.user.username)

        DT_End = datetime.datetime.now()
        DT_Diff = DT_End - DT_Start
        strNotes = "Elapsed Time (Minutes)= " + str((DT_Diff.seconds) / 60)

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
