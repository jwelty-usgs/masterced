# Description: Test to authentication and transfering cookies
# Created By:  Matt Heller
# Date:        4/22/2014

import sys,getopt
# import pysb #python 2.7
import sciencebasepy as pysb
import urllib

from django.conf import settings

sbpass = settings.SBPASS
sbuser = settings.SBUSER

strUsername = ''
strPwd = ''

try:
  opts, args = getopt.getopt(sys.argv[1:],"hu:p:",["username=","pwd="])
except getopt.GetoptError:
  print('-u <username> -p <pwd>')
  sys.exit(2)
for opt, arg in opts:
  if opt == '-h':
     print('QueryLCMAP_SB_WFS_Footprint_AndUpdate_AGS_Featureservice_v3.py -u <username> -p <pwd>')
     sys.exit()
  elif opt in ("-u", "--username"):
     strUsername = arg
  elif opt in ("-p", "--pwd"):
     strPwd = arg

def Login2SBandOpenFootprintStudioFPE(strURL, itemid, prjid, returnurl): #(strUserName, strPassword, strURL):
    try:
      sbid = ''
      sb = pysb.SbSession()# Create the ScienceBase session

      sb.login(sbuser, sbpass)# log in to ScienceBase (you don't need to login to do certain things).

      url = "https://www.sciencebase.gov/footprinter/?josso=" + str(sb._jossosessionid) + "#/?"
      # url = 'https://www.sciencebase.gov/catalog/item/' + itemid + "?"

      sbid = str(sb._jossosessionid)

      params = {
          'itemId': str(itemid),
          'returnTo': returnurl + '/sgce/' + str(prjid) + '/spatialentry' 
      }

      strSessionID = url + urllib.urlencode(params)

      strResults = strSessionID + "," + str(sb._jossosessionid)
      return strResults
    except:
      return "NoConnection"

def Login2SBandOpenFootprintStudio(strURL): #(strUserName, strPassword, strURL):
    # try:
    sb = pysb.SbSession()# Create the ScienceBase session
    sb.login(sbuser, sbpass)# log in to ScienceBase (you don't need to login to do certain things).
    strResponseJSON = sb.get_json(strURL) #get the data
    strSessionID = sb._session.cookies['JOSSO_SESSIONID']
    # pResults = requests.get(strURL, cookies = sb._session.cookies, verify = False)
    pResults = sb._session.get(strURL)
    if(pResults.status_code == 200): 
      return strSessionID
    else:
      return "NoConnection"
    # except:
    #   return "NoConnection"

def Login2SBandOpenFootprintStudio1(strURL, sbid): #(strUserName, strPassword, strURL):
    try:
      sb = pysb.SbSession()# Create the ScienceBase session
      sb.login(sbuser, sbpass)# log in to ScienceBase (you don't need to login to do certain things).
      strResponseJSON = sb.get_json(strURL) #get the data
      strSessionID = sb._session.cookies['JOSSO_SESSIONID']
      sbid = sbid + "?"
      fileloc = str(strResponseJSON)
      fileloc0 = fileloc.split(sbid)
      fileloc1 = str(fileloc0[1])
      fileloc2 = fileloc1.split("',")
      fileloc3 = str(fileloc2[0])

      pResults = sb._session.get(strURL)

      # pResults = requests.get(strURL, cookies = sb._session.cookies, verify = False)
      pResults = sb._session.get(strURL)

      if(pResults.status_code == 200): 
        return strSessionID, fileloc3
      else:
        return "NoConnection"
    except:
      return "NoConnection"

    


# strURL = r"https://www.sciencebase.gov/catalog/item/5345b303e4b0169f5005bcad"

# Login2SBandOpenFootprintStudio(strUsername, strPwd, strURL)
