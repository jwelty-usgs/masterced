# Description: Gets WFS footprint data from LC MAP/SB and updates LC MAP/SB's a AGS FeatureService layer
# Created By:  Matt Heller
# Date:        4/9/2014
# Updated By:  Justin Welty
# Date:        4/10/2014

import urllib
# import urllib2 python 2.7
import collections
import sys,getopt
# import pysb #python 2.7
import sciencebasepy as pysb
import time

import os
import json

from django.conf import settings

from ced.settings import STATIC_DIR

# import arcpy


hst = settings.DBHOST
usr = settings.DBUSER
psswrd = settings.DBPASSWORD
dtbs = settings.DBNAME
strPwd = settings.SBPASS
strUsername = settings.SBUSER

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

def ConvertJsontoFeature(JsonFeatures):
    a=1
  #   #TODO
  # arcpy.env.workspace = "C:\\Users\\jwelty\\Documents\\CED\\ced_spatial_data\\temp_files"
  # arcpy.JSONToFeatures_conversion(JsonFeatures, "ClipTest.shp")

def ExecuteApplyEditsAdds(arrayParamFeatures, strURL):
   dAddFeatureOperationParam = {'adds' : arrayParamFeatures, 'f':'json', 'rollbackOnFailure':'true'}   
   dAddFeatureOperationParamPass = urllib.urlencode(dAddFeatureOperationParam)
   strResponseApplyEdit = urllib.urlopen(strURL, dAddFeatureOperationParamPass)#submit adds operation and get response
   strResponseJSONApplyEdit = json.loads(strResponseApplyEdit.read())

def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

def ConvertWMSandReturnFeatures(SciBaseID):
    overallcount = 0
    ## List the locations were data will be stored
    #TODO
    # testspace = os.path.join(STATIC_DIR, 'ced_main/GIS_Processing')

    # json_filePoly = testspace + "\\A_Poly_" + SciBaseID + ".json"
    # json_fileLine = testspace + "\\A_Line_" + SciBaseID + ".json"
    # json_fileLine1 = testspace + "\\A1_Line_" + SciBaseID + ".json"
    # json_fileLineTest = testspace + "\\A_LineTest_" + SciBaseID + ".json"
    # json_filePoint = testspace + "\\A_Point_" + SciBaseID + ".json"

    # arcpy.env.workspace = testspace + "\\JsonConversion.gdb"

    # fcPoly = testspace + "\\A_Poly_" + SciBaseID + ".shp"
    # fc1Poly = testspace + "\\A_Poly_" + SciBaseID + "_Project.shp"
    # fcLine = testspace + "\\A_Line_" + SciBaseID + ".shp"
    # fc1Line = testspace + "\\A_Line_" + SciBaseID + "_Project.shp"
    # fcPoint = testspace + "\\A_Point_" + SciBaseID + ".shp"
    # fc1Point = testspace + "\\A_Point_" + SciBaseID + "_Project.shp"

    # if os.path.isfile(json_filePoly):
    #     os.remove(json_filePoly)
    # if os.path.isfile(json_fileLine):
    #     os.remove(json_fileLine)
    # if os.path.isfile(json_fileLine1):
    #     os.remove(json_fileLine1)
    # if os.path.isfile(json_filePoint):
    #     os.remove(json_filePoint)

    # try:
    #     arcpy.Delete_management(fcPoly)
    # except:
    #     print("Nothing to delete")
    # try:
    #     arcpy.Delete_management(fc1Poly)
    # except:
    #     print("Nothing to delete")
    # try:
    #     arcpy.Delete_management(fcLine)
    # except:
    #     print("Nothing to delete")
    # try:
    #     arcpy.Delete_management(fc1Line)
    # except:
    #     print("Nothing to delete")
    # try:
    #     arcpy.Delete_management(fcPoint)
    # except:
    #     print("Nothing to delete")
    # try:
    #     arcpy.Delete_management(fc1Point)
    # except:
    #     print("Nothing to delete")

    # str_wfs_serverVal1 = "https://www.sciencebase.gov/catalogMaps/mapping/ows"
    # strUsername1 = strUsername
    # strPassword = strPwd
    # str_wfs_server = str_wfs_serverVal1 + "/" + SciBaseID
    # req = 'GetFeature' # request
    # version = '1.0.0'
    # service = 'WFS'
    # typeName = 'footprint'
    # maxfeatures = 200000
    # srsname = 'EPSG:4326'
    # outputFormat = 'json'   
    # fc1 = "None"
    # strWMS_URL = '%s?request=%s&version=%s&service=%s&typeName=%s&maxfeatures=%s&srsname=%s&outputFormat=%s' % \
    #     (str_wfs_server, req, version, service, typeName,maxfeatures, srsname, outputFormat)
    
    # sb = pysb.SbSession()# Create the ScienceBase session
    # sb.login(strUsername1, strPassword)# log in to ScienceBase (you don't need to login to do certain things).
    # try:
    #     strResponseJSON = sb.getJson(strWMS_URL) #get the data 
    # except:
    #     return "Error" 
    
    # if strResponseJSON == "NoData":
    #     return "None"
    # time.sleep(0.2)
    
    # dictFeatures = strResponseJSON['features']

    # if "error" in dictFeatures: 
    #   return

    # i = 0
    # feattype = ""

    # arrayParamFeaturesPoly = []
    # arrayParamFeaturesLine = []
    # arrayParamFeaturesPoint = []

    # esrijsonPoly = ""
    # esrijsonPoint = ""
    # esrijsonLine = ""

    # featcntPoly = 1
    # featcntLine = 1
    # featcntPoint = 1

    # oidPolycnt = 1
    # oidPointcnt = 1
    # oidLinecnt = 1

    # oidPoly1 = ""
    # oidPoly2 = ""
    # oidLine1 = ""
    # oidLine2 = ""
    # oidPoint1 = ""
    # oidPoint2 = ""

    # xmax = 0
    # xmin = 0
    # ymax = 0
    # ymin = 0
    # xmid = 0
    # ymid = 0

    # #Prepare a list of spatial features to send back
    # SpatialFeatures = []

    
    # z=open(json_filePoly,'w')
    # z.close()
    # v=open(json_fileLine,'w')
    # v.close()
    # v1=open(json_fileLine1,'w')
    # v1.close()
    # r=open(json_filePoint,'w')
    # r.close()
    # q=open(json_fileLineTest,'w')
    # r.close()

    # for dictFeature in dictFeatures:
    #     z=open(json_filePoly,'a')
    #     v=open(json_fileLine,'a')
    #     v1=open(json_fileLine1,'a')
    #     r=open(json_filePoint,'a')
    #     DictJSONGeom1 = dictFeature['geometry']
    #     feattype = DictJSONGeom1['type']

    #     feattypePoly = ""
    #     feattypePoint = ""
    #     feattypeLine = ""

    #     print(feattype)
    #     if feattype == "Polygon" or feattype == "MultiPolygon":
    #         feattypePoly = "esriGeometryPolygon"
    #         if oidPolycnt == 1:
    #             esrijsonPoly = '{"displayFieldName":"","fieldAliases":{"OID":"OID","Name":"Name","Shape_Length":"Shape_Length","Shape_Area":"Shape_Area"},"geometryType":"' + feattypePoly + '","spatialReference":{"wkid":104199,"latestWkid":4326},"fields":[{"name":"OID","type":"esriFieldTypeOID","alias":"OID"},{"name":"Name","type":"esriFieldTypeString","alias":"Name","length":60},{"name":"Shape_Length","type":"esriFieldTypeDouble","alias":"Shape_Length"},{"name":"Shape_Area","type":"esriFieldTypeDouble","alias":"Shape_Area"}],"features":[' # Write the initial ESRI Json format
    #             z.write(str(esrijsonPoly))

        
    #     if feattype == "Line" or feattype == "Polyline" or feattype == "MultiLineString":
    #         return "Failed"
    #         # feattypeLine = "esriGeometryPolyline"
    #         # if oidLinecnt == 1:
    #         #     esrijsonLine = '{"displayFieldName":"","fieldAliases":{"OID":"OID","Name":"Name","Shape_Length":"Shape_Length"},"geometryType":"' + feattypeLine + '","spatialReference":{"wkid":104199,"latestWkid":4326},"fields":[{"name":"OID","type":"esriFieldTypeOID","alias":"OID"},{"name":"Name","type":"esriFieldTypeString","alias":"Name","length":60},{"name":"Shape_Length","type":"esriFieldTypeDouble","alias":"Shape_Length"}],"features":[' # Write the initial ESRI Json format
    #         #     v.write(str(esrijsonLine))

    #     if feattype == "Point" or feattype == "MultiPoint":
    #         return "Failed"
    #         # feattypePoint = "Multipoint"
    #         # if oidPointcnt == 1:
    #         #     esrijsonPoint = '{"displayFieldName":"","fieldAliases":{"OID":"OID","Name":"Name"},"geometryType":"esriGeometryMultipoint","spatialReference":{"wkid":104199,"latestWkid":4326},"fields":[{"name":"OID","type":"esriFieldTypeOID","alias":"OID"},{"name":"Name","type":"esriFieldTypeString","alias":"Name","length":60}],"features":[' # Write the initial ESRI Json format
    #         #     r.write(str(esrijsonPoint))
    #     print(feattypePoly)
    #     if feattypePoly == "esriGeometryPolygon":

    #         oidPoly1 = '{"attributes":{"OID":' + str(oidPolycnt) + ',"Name":"","Shape_Length":Null,"Shape_Area":Null},"geometry":{"rings":'
    #         oidPoly1a = '{"attributes":{"OID":' + str(oidPolycnt) + ',"Name":"","Shape_Length":Null,"Shape_Area":Null},"geometry":{"rings":[['
    #         oidPoly2 = '}},{"attributes":{"OID":' + str(oidPolycnt) + ',"Name":"","Shape_Length":Null,"Shape_Area":Null},"geometry":{"rings":'
    #         oidPoly2a = ']]}},{"attributes":{"OID":' + str(oidPolycnt) + ',"Name":"","Shape_Length":Null,"Shape_Area":Null},"geometry":{"rings":[['
    #         if oidPolycnt == 1: 
    #             esrijsonPoly = esrijsonPoly + oidPoly1 # Add geometry
    #             z.write(str(oidPoly1a))
    #         else:
    #             esrijsonPoly = esrijsonPoly + oidPoly2 # Add additional geometryDictJSONGeom1 = dictFeature['geometry']
    #             z.write(str(oidPoly2a))
    #         strRingsArray = DictJSONGeom1['coordinates']
            
    #         strRingsArray = str(strRingsArray)
    #         strRingsArray = strRingsArray[1:-1] # remove extra brakets for Polygons
    #         strRingsArray2 = strRingsArray[2:-2]
    #         strRingsArray3 = strRingsArray2.split("]")
    #         j = 0

    #         strRingsArray1 = []

    #         for array3 in strRingsArray3:
    #             arraytest = array3[0:5]
    #             array3 = array3.replace("[","")
    #             array4 = array3.replace(",","")
    #             array4 = array4.replace(" ",", ")
    #             if j == 0:
    #                 arrayf = "[" + array3 + "]"
    #                 arrayf1 = "[" + array4 + "]"
    #                 strRingsArray1.append(eval(arrayf.strip()))
    #                 z.write(str(arrayf1))
    #                 j = 1
    #             else:

    #                 if array3 > "":

    #                     if arraytest == ", [[[":
    #                         oidPolycnt = oidPolycnt + 1
                            
    #                         oidPoly2 = '}},{"attributes":{"OID":' + str(oidPolycnt) + ',"Name":"","Shape_Length":Null,"Shape_Area":Null},"geometry":{"rings":'
    #                         oidPoly3 = ']]}},{"attributes":{"OID":' + str(oidPolycnt) + ',"Name":"","Shape_Length":Null,"Shape_Area":Null},"geometry":{"rings":[['
    #                         # strRingsArray1.append(oidPoly2)
    #                         z.write(str(oidPoly3))
    #                     else:
    #                         z.write(str(", "))
    #                     arrayf = "[" + array3[2:] + "]"
    #                     arrayf1 = "[" + array4[2:] + "]"
    #                     z.write(str(arrayf1))
    #                     if arrayf != "]":
    #                         strRingsArray1.append(eval(arrayf.strip()))


    #         for x, y in strRingsArray1:
    #             if xmax == 0:
    #                 xmax = x
    #             else:
    #                 if xmax < x:
    #                     xmax = x
    #             if xmin == 0:
    #                 xmin = x
    #             else:
    #                 if xmin > x:
    #                     xmin = x
    #             if ymax == 0:
    #                 ymax = y
    #             else:
    #                 if ymax < y:
    #                     ymax = y
    #             if ymin == 0:
    #                 ymin = y
    #             else:
    #                 if ymin > y:
    #                     ymin = y

    #         esrijsonPoly = esrijsonPoly + strRingsArray # Add geometry data
    #         oidPolycnt = oidPolycnt + 1
            
            
    #     elif feattypeLine == "esriGeometryPolyline":
    #         oidLine1 = '{"attributes":{"OID":' + str(oidLinecnt) + ',"Name":"","Shape_Length":Null},"geometry":{"paths":'
    #         oidLine1a = '{"attributes":{"OID":' + str(oidLinecnt) + ',"Name":"","Shape_Length":Null},"geometry":{"paths":[['
    #         oidLine2 = '}},{"attributes":{"OID":' + str(oidLinecnt) + ',"Name":"","Shape_Length":Null},"geometry":{"paths":'
    #         oidLine2a = ']]}},{"attributes":{"OID":' + str(oidLinecnt) + ',"Name":"","Shape_Length":Null},"geometry":{"paths":[['
    #         if oidLinecnt == 1: 
    #             esrijsonLine = esrijsonLine + oidLine1 # Add geometry
    #             v.write(str(oidLine1a))
    #         else:
    #             esrijsonLine = esrijsonLine + oidLine2 # Add additional geometry
    #             v.write(str(oidLine2a))
    #         DictJSONGeom1 = dictFeature['geometry']
    #         strRingsArray = DictJSONGeom1['coordinates']
    #         strRingsArray = str(strRingsArray)

    #         strRingsArray2 = strRingsArray[2:-2]
            
    #         strRingsArray3 = strRingsArray2.split(", [-1, [")

    #         strRingsArray4 = str(strRingsArray3[0])
    #         strRingsArray4 = strRingsArray4.replace("[","")
    #         strRingsArray4 = strRingsArray4.replace("], ",";")
            
    #         strRingsArray4 = str(strRingsArray4)


    #         strRingsArray9 = strRingsArray4.split("];")
    #         arraycnt = 0
    #         for str9 in strRingsArray9:
    #             q=open(json_fileLineTest,'a')
    #             q.write("Arraycnt: " + str(arraycnt))
    #             q.close()

    #             if arraycnt == 1:
    #                 oidLinecnt = oidLinecnt + 1
    #                 oidLine4 = ']]}},{"attributes":{"OID":' + str(oidLinecnt) + ',"Name":"","Shape_Length":Null},"geometry":{"paths":[['
    #                 v.write(str(oidLine4))
                
    #             str9 = str(str9)
            
    #             strRingsArray5 = str9.replace("]","")
    #             q=open(json_fileLineTest,'a')
    #             q.write("strRingsArray5: " + str(strRingsArray5))
    #             q.close()
    #             strRingsArray5 = strRingsArray5.split(";")
    #             j = 0
    #             strRingsArray1 = []
                
                
    #             for array3 in strRingsArray5:
                    
    #                 arraytest = array3[0:5]
    #                 array3 = array3.replace("[","")
    #                 array4 = array3.replace(",","")
    #                 array4 = array4.replace(" ",", ")
    #                 array4 = array4.replace("]","")

    #                 if j == 0:

    #                     arrayf = "[" + array3 + "]"
    #                     arrayf1 = "[" + array4 + "]"
    #                     strRingsArray1.append(eval(arrayf.strip()))
    #                     v.write(str(arrayf1))
    #                     j = 1

    #                 else:

    #                     if array3 != "":

    #                         if arraytest == ", [[[":
    #                             oidLinecnt = oidLinecnt + 1
                                
    #                             oidLine2 = '}},{"attributes":{"OID":' + str(oidLinecnt) + ',"Name":"","Shape_Length":Null},"geometry":{"paths":'
    #                             oidLine3 = ']]}},{"attributes":{"OID":' + str(oidLinecnt) + ',"Name":"","Shape_Length":Null},"geometry":{"paths":[['
    #                             # strRingsArray1.append(oidPoly2)
    #                             v.write(str(oidLine3))
    #                         else:
    #                             v.write(str(", "))
    #                         arrayf = "[" + array3 + "]"
    #                         arrayf1 = "[" + array4 + "]"
    #                         v.write(str(arrayf1))
    #                         if arrayf != "]":
    #                             strRingsArray1.append(eval(arrayf.strip()))
    #             arraycnt = arraycnt + 1

    #         for x, y in strRingsArray1:
    #             if xmax == 0:
    #                 xmax = x
    #             else:
    #                 if xmax < x:
    #                     xmax = x
    #             if xmin == 0:
    #                 xmin = x
    #             else:
    #                 if xmin > x:
    #                     xmin = x
    #             if ymax == 0:
    #                 ymax = y
    #             else:
    #                 if ymax < y:
    #                     ymax = y
    #             if ymin == 0:
    #                 ymin = y
    #             else:
    #                 if ymin > y:
    #                     ymin = y
    #         esrijsonLine = esrijsonLine + strRingsArray # Add geometry data
    #         oidLinecnt = oidLinecnt + 1

    #     elif feattypePoint == "Multipoint":
    #         if oidPointcnt == 1: 
    #             oidPoint1 = '{"attributes":{"OID":' + str(oidPointcnt) + ',"Name":""},"geometry":{"points":[['


    #         DictJSONGeom1 = dictFeature['geometry']
    #         feattype = DictJSONGeom1['type']

    #         strRingsArray = DictJSONGeom1['coordinates']
    #         strRingsArray = str(strRingsArray)
    #         strRingsArray = strRingsArray.replace("[","")
    #         strRingsArray = strRingsArray.replace("], ",";")
    #         strRingsArray = strRingsArray.split(";")
    #         try:
    #             for ads in strRingsArray:
    #                 ads1 = str(ads)
    #                 ads2 = ads1.replace(", ",";")
    #                 ads2 = str(ads2)
    #                 ads3 = ads2.split(";")
                    
    #                 x = ads3[0]
    #                 y = ads3[1]


    #                 if oidPointcnt == 1 and overallcount == 0:
    #                     oidPoint2 = '{"attributes":{"OID":' + str(oidPointcnt) + ',"Name":""},"geometry":{"points":[['
    #                     r.write(str(oidPoint2) + str(x) + ',' + str(y))
    #                     oidPointcnt = oidPointcnt + 1
    #                     overallcount = 1
    #                 else:
    #                     oidPoint3 = ']]}},{"attributes":{"OID":' + str(oidPointcnt) + ',"Name":""},"geometry":{"points":[['
    #                     r.write(oidPoint3 + str(x) + ',' + str(y))
    #                     oidPointcnt = oidPointcnt + 1
    #         except:
    #             badluck = "Badluck"


                           

    #             if xmax == 0:
    #                 xmax = x
    #             else:
    #                 if xmax < x:
    #                     xmax = x
    #             if xmin == 0:
    #                 xmin = x
    #             else:
    #                 if xmin > x:
    #                     xmin = x
    #             if ymax == 0:
    #                 ymax = y
    #             else:
    #                 if ymax < y:
    #                     ymax = y
    #             if ymin == 0:
    #                 ymin = y
    #             else:
    #                 if ymin > y:
    #                     ymin = y
    #         # esrijsonPoint = esrijsonPoint + strRingsArray # Add geometry data
    #         # oidPointcnt = oidPointcnt + 1
    #     z.close()
    #     v.close()
    #     r.close()
    #     i += 1
    #     if (i > 50):
    #         break

    # xmid = (xmax + xmin) / 2
    # ymid = (ymax + ymin) / 2
    # xdiff = (xmax - xmin)
    # ydiff = (ymax - ymin)

    # zoomlevel = 1.5
    # if xdiff > ydiff:
    #     zoomlevel = xdiff
    # else:
    #     zoomlevel = ydiff

    # zoom = 7
    # if zoomlevel < 0.01:
    #     zoom = 11
    # elif zoomlevel >=0.01 and zoomlevel < 0.1:
    #     zoom = 10
    # elif zoomlevel >= 0.1 and zoomlevel < 0.25:
    #     zoom = 9
    # elif zoomlevel >= 0.25 and zoomlevel < 1.0:
    #     zoom = 8
    # elif zoomlevel >= 1.0 and zoomlevel < 3.0:
    #     zoom = 7
    # elif zoomlevel >= 3.0 and zoomlevel < 6.0:
    #     zoom = 6
    # elif zoomlevel >= 6.0 and zoomlevel < 12.0:
    #     zoom = 5
    # elif zoomlevel >= 12.0:
    #     zoom = 4

    # SpatialFeatures.append(str(xmid))
    # SpatialFeatures.append(str(ymid))
    # SpatialFeatures.append(str(zoom))

    
    # if esrijsonPoly != "":
    #     esrijsonPoly = esrijsonPoly + '}}]}'
    #     z=open(json_filePoly,'a')
    #     z.write(']]}}]}')
    #     z.close()
    # if esrijsonLine != "":
    #     esrijsonLine = esrijsonLine + '}}]}'
    #     v=open(json_fileLine,'a')
    #     v.write(']]}}]}')
    #     v.close()

    #     v = open(json_fileLine, 'r')
    #     v1 = open(json_fileLine1, 'ab')
    #     print("Writing Lines")
    #     for line in v:
    #         v1.write(line.replace('][', '], ['))
    #     v.close()
    #     v1.close()
    #     if os.path.isfile(json_fileLine):
    #         os.remove(json_fileLine)
    #     v1 = open(json_fileLine1, 'r')
    #     v = open(json_fileLine, 'ab')
    #     print("Writing Lines")
    #     for line in v1:
    #         v.write(line)
    #     v.close()
    #     v1.close()

    # if esrijsonPoint != "":
    #     esrijsonPoint = esrijsonPoint + '}}]}'
    #     r=open(json_filePoint,'a')
    #     r.write('}}]}')
    #     r.close()
    #     with open (json_filePoint, "r") as myfile:
    #         datareplace=myfile.read().replace('\n', '')
    #         datareplace1 = datareplace.replace("]]]]","]]")
    #     r=open(json_filePoint,'w')
    #     r.write(datareplace1)
    #     r.close()

    # # Write the feature files
    # if esrijsonPoly != "":
    #     ## Convert Json to feature
    #     arcpy.env.workspace = testspace + "\\JsonConversion.gdb"
    #     res=arcpy.JSONToFeatures_conversion(json_filePoly,fcPoly)
    #     try:
    #         arcpy.Delete_management(fc1Poly)
    #     except:
    #         print("The projected feature is not deleting")
    #     outCS = arcpy.SpatialReference('WGS 1984 Web Mercator (Auxiliary Sphere)')
    #     res1 = arcpy.Project_management(fcPoly, fc1Poly, outCS)
    #     SpatialFeatures.append(fc1Poly)
    #     try:
    #         arcpy.Delete_management(fcPoly)
    #     except:
    #         print("Nothing to delete")
    # if esrijsonLine != "":
    #     ## Convert Json to feature
    #     arcpy.env.workspace = testspace + "\\JsonConversion.gdb"
        
    #     res=arcpy.JSONToFeatures_conversion(json_fileLine,fcLine)
    #     try:
    #         arcpy.Delete_management(fc1Line)
    #     except:
    #         print("The projected feature is not deleting")
    #     outCS = arcpy.SpatialReference('WGS 1984 Web Mercator (Auxiliary Sphere)')
    #     res1 = arcpy.Project_management(fcLine, fc1Line, outCS)
    #     SpatialFeatures.append(fc1Line)
    #     try:
    #         arcpy.Delete_management(fcLine)
    #     except:
    #         print("Nothing to delete")

    # if esrijsonPoint != "":
    #     ## Convert Json to feature
    #     arcpy.env.workspace = testspace + "\\JsonConversion.gdb"
        
        
    #     res=arcpy.JSONToFeatures_conversion(json_filePoint,fcPoint)
    #     try:
    #         arcpy.Delete_management(fc1Point)
    #     except:
    #         print("The projected feature is not deleting")
    #     outCS = arcpy.SpatialReference('WGS 1984 Web Mercator (Auxiliary Sphere)')
    #     res1 = arcpy.Project_management(fcPoint, fc1Point, outCS)
    #     SpatialFeatures.append(fc1Point)
    #     try:
    #         arcpy.Delete_management(fcPoint)
    #     except:
    #         print("Nothing to delete")

    # strRingsArray1 = []
    return "Done"

def featurecount(SciBaseID):

    str_wfs_serverVal1 = "https://www.sciencebase.gov/catalogMaps/mapping/ows"
    strUsername1 = strUsername
    strPassword = strPwd
    str_wfs_server = str_wfs_serverVal1 + "/" + SciBaseID
    req = 'GetFeature' # request
    version = '1.2.4'
    service = 'WFS'
    typeName = 'footprint'
    maxfeatures = 200000
    srsname = 'EPSG:4326'
    outputFormat = 'json'   
    fc1 = "None"
    strWMS_URL = '%s?request=%s&version=%s&service=%s&typeName=%s&maxfeatures=%s&srsname=%s&outputFormat=%s' % \
        (str_wfs_server, req, version, service, typeName,maxfeatures, srsname, outputFormat)
    
    sb = pysb.SbSession()# Create the ScienceBase session
    sb.login(strUsername1, strPassword)# log in to ScienceBase (you don't need to login to do certain things).

    try:
        strResponseJSON = sb.getJson(strWMS_URL) #get the data 
    except: 
        return "None"
    if strResponseJSON == "NoData":
        return "None"
    time.sleep(0.2)
    dictFeatures = strResponseJSON['features']

    if "error" in dictFeatures: 
        return 1

    i = 0
    feattype = ""

    #Prepare a list of spatial features to send back
    SpatialFeatures = []

    for dictFeature in dictFeatures:
        DictJSONGeom1 = dictFeature['geometry']
        feattype = DictJSONGeom1['type']

      
        if feattype == "Polygon" or feattype == "MultiPolygon":
            featcnt = 1
        elif feattype == "Line" or feattype == "Polyline" or feattype == "MultiLineString":
            featcnt = "NotPoly"
        elif feattype == "Point" or feattype == "MultiPoint":
            featcnt = "NotPoly"
        else:
            featcnt = 0
        
    return featcnt 

