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
    srulist = (('1', 'OR: Trout Creeks'), ('2', 'OR: Beatys'), ('3', 'OR: Louse - Soldier'), ('4', 'OR: Steens - Pueblos'), ('5', 'OR: Warners - Tucker'), ('6', 'OR: Picture Rock'), ('7', 'OR: Dry Valley'), ('8', 'OR: Alvord - Folly'), ('9', 'OR: Cow Lakes'), ('10', 'OR: Crowley'), ('11', 'OR: Brothers'), ('12', 'OR: Burns'), ('13', 'OR: Drewsey'), ('14', 'OR: Paulina'), ('15', 'OR: Prineville'), ('16', 'OR: Bully - Cow Valley'), ('17', 'OR: Baker'), ('18', 'ID: Bear Lake'), ('19', 'ID: Bennett Hills'), ('20', 'ID: Timmerman Hills'), ('21', 'ID: Craters of the Moon'), ('22', 'ID: Big Desert'), ('23', 'ID: Antelope Flats_Big Lost'), ('24', 'ID: Little Lost_Pahsimeroi'), ('25', 'ID: Hat Creek_Morgan Creek'), ('26', 'ID: Lemhi River'), ('27', 'ID: Inside Desert'), ('28', 'ID: Goose Creek'), ('29', 'ID: Upper Raft River Valley'), ('30', 'ID: Greater Curlew'), ('31', 'ID: Weiser'), ('32', 'ID: Cow Lakes'), ('33', 'ID: Muldoon'), ('34', 'ID: Browns Bench'), ('35', 'ID: East Idaho Upland'), ('36', 'ID: Antelope Ridge'), ('37', 'ID: Louse Canyon - Owyhee Desert - Owyhee Canyonlands'), ('39', 'ID: Soldier Creek'), ('44', 'ID: Other (Idaho) 3'), ('100', 'WA: Lek Cluster - 155'), ('101', 'WA: Lek Cluster - 160'), ('102', 'WA: Lek Cluster - 170'), ('103', 'WA: Lek Cluster - 445'), ('104', 'ND: Lek Cluster - 143, 552, 556'), ('105', 'ND: Lek Cluster - 553'), ('106', 'SD: Lek Cluster - 419'), ('107', 'SD: Lek Cluster - 168, 193, 195'), ('110', 'SD: Lek Cluster - 192, 422'), ('111', 'MT: Lek Cluster - 154'), ('112', 'MT: Lek Cluster - 154, 175, 176, 177'), ('113', 'MT: Lek Cluster - 187'), ('114', 'MT: Lek Cluster - 411'), ('115', 'MT: Lek Cluster - 130, 131'), ('120', 'MT: Lek Cluster - 147, 149, 178, 180, 181, 182, 416'), ('121', 'CO: Lek Cluster - 19, 28, 281'), ('122', 'CO: Lek Cluster - 25, 448'), ('123', 'CO: Lek Cluster - 259'), ('124', 'CO: Lek Cluster - 465'), ('125', 'CO: Lek Cluster - 450, 451'), ('126', 'CO: Lek Cluster - 279, 280'), ('127', 'CO: Lek Cluster - 455'), ('128', 'CO: Lek Cluster - 255, 458, 460'), ('131', 'CO: Lek Cluster - 461'), ('133', 'CO: Lek Cluster - 278'), ('44', 'ID: Other (Idaho) 1'), ('44', 'ID: Other (Idaho) 2'), ('44', 'ID: Other (Idaho) 4'), ('230', 'SD: Lek Cluster - 96'), ('231', 'SD: Lek Cluster - 138, 143, 188, 425'), ('232', 'MT: Lek Cluster - 127, 140, 379, 407'), ('233', 'MT: Lek Cluster - 126'), ('235', 'MT: Lek Cluster - 134'), ('236', 'MT: Lek Cluster - 138'), ('237', 'MT: Lek Cluster - 144'), ('238', 'MT: Lek Cluster - 146'), ('239', 'MT: Lek Cluster - 148'), ('240', 'MT: Lek Cluster - 150'), ('241', 'MT: Lek Cluster - 151'), ('242', 'MT: Lek Cluster - 152'), ('243', 'MT: Lek Cluster - 153'), ('244', 'MT: Lek Cluster - 156'), ('246', 'MT: Lek Cluster - 157'), ('247', 'MT: Lek Cluster - 158'), ('249', 'MT: Lek Cluster - 159'), ('250', 'MT: Lek Cluster - 161'), ('251', 'MT: Lek Cluster - 162'), ('252', 'MT: Lek Cluster - 163'), ('253', 'MT: Lek Cluster - 164'), ('254', 'MT: Lek Cluster - 165'), ('255', 'MT: Lek Cluster - 169'), ('256', 'MT: Lek Cluster - 171'), ('257', 'MT: Lek Cluster - 172'), ('258', 'MT: Lek Cluster - 173'), ('259', 'MT: Lek Cluster - 174'), ('260', 'MT: Lek Cluster - 179'), ('261', 'MT: Lek Cluster - 183'), ('262', 'MT: Lek Cluster - 184'), ('263', 'MT: Lek Cluster - 186'), ('264', 'MT: Lek Cluster - 188'), ('265', 'MT: Lek Cluster - 194'), ('267', 'MT: Lek Cluster - 196'), ('268', 'MT: Lek Cluster - 362'), ('269', 'MT: Lek Cluster - 419'), ('270', 'MT: Lek Cluster - 420'), ('271', 'MT: Lek Cluster - 421'), ('272', 'MT: Lek Cluster - 422'), ('273', 'MT: Lek Cluster - 423'), ('274', 'MT: Lek Cluster - 425'), ('275', 'MT: Lek Cluster - 426'), ('276', 'MT: Lek Cluster - 427'), ('277', 'MT: Lek Cluster - 428'), ('278', 'MT: Lek Cluster - 429'), ('279', 'MT: Lek Cluster - 430'), ('280', 'MT: Lek Cluster - 431'), ('281', 'MT: Lek Cluster - 432'), ('282', 'MT: Lek Cluster - 433'), ('283', 'MT: Lek Cluster - 434'), ('284', 'MT: Lek Cluster - 435'), ('285', 'MT: Lek Cluster - 436'), ('286', 'MT: Lek Cluster - 437'), ('287', 'MT: Lek Cluster - 438'), ('288', 'MT: Lek Cluster - 439'), ('289', 'MT: Lek Cluster - 440'), ('290', 'MT: Lek Cluster - 441'), ('291', 'MT: Lek Cluster - 442'), ('292', 'MT: Lek Cluster - 443'), ('293', 'MT: Lek Cluster - 444'), ('294', 'MT: Lek Cluster - 418'), ('295', 'CO: Lek Cluster - 43'), ('298', 'CO: Lek Cluster - 263'), ('299', 'CO: Lek Cluster - 267'), ('300', 'CO: Lek Cluster - 271'), ('301', 'CO: Lek Cluster - 273'), ('302', 'CO: Lek Cluster - 446'), ('304', 'CO: Lek Cluster - 447'), ('307', 'CO: Lek Cluster - 454'), ('308', 'CO: Lek Cluster - 470'), ('309', 'CO: Lek Cluster - 463'), ('310', 'CO: Lek Cluster - 464'), ('311', 'CO: Lek Cluster - 467'), ('314', 'CO: Lek Cluster - 468'), ('43', 'ID: Twin Buttes'), ('41', 'ID: Sand Creek'), ('42', 'ID: Medicine Lodge'), ('334', 'MT: Lek Cluster - 132'), ('335', 'CA: Lek Cluster - 11'), ('336', 'CA: Lek Cluster - 11, 288'), ('337', 'CA: Lek Cluster - 13'), ('338', 'CA: Lek Cluster - 14'), ('339', 'CA: Lek Cluster - 26'), ('340', 'CA: Lek Cluster - 37'), ('341', 'CA: Lek Cluster - 64, 76'), ('343', 'CA: Lek Cluster - 83, 85'), ('344', 'CA: Lek Cluster - 84'), ('346', 'CA: Lek Cluster - 88'), ('347', 'CA: Lek Cluster - 92'), ('349', 'CA: Lek Cluster - 93'), ('350', 'CA: Lek Cluster - 167'), ('351', 'CA: Lek Cluster - 222, 337'), ('352', 'CA: Lek Cluster - 225'), ('353', 'CA: Lek Cluster - 286'), ('355', 'CA: Lek Cluster - 334'), ('357', 'CA: Lek Cluster - 449'), ('360', 'NV: Lek Cluster - 5, 7'), ('361', 'NV: Lek Cluster - 6'), ('363', 'NV: Lek Cluster - 10'), ('364', 'NV: Lek Cluster - 11'), ('365', 'NV: Lek Cluster - 13'), ('366', 'NV: Lek Cluster - 15'), ('367', 'NV: Lek Cluster - 17'), ('368', 'NV: Lek Cluster - 18'), ('369', 'NV: Lek Cluster - 20'), ('370', 'NV: Lek Cluster - 22'), ('371', 'NV: Lek Cluster - 23'), ('372', 'NV: Lek Cluster - 24'), ('373', 'NV: Lek Cluster - 27'), ('374', 'NV: Lek Cluster - 29'), ('375', 'NV: Lek Cluster - 31'), ('376', 'NV: Lek Cluster - 34'), ('377', 'NV: Lek Cluster - 35'), ('378', 'NV: Lek Cluster - 37'), ('379', 'NV: Lek Cluster - 38'), ('380', 'NV: Lek Cluster - 39'), ('381', 'NV: Lek Cluster - 40'), ('382', 'NV: Lek Cluster - 41, 45'), ('383', 'NV: Lek Cluster - 42'), ('385', 'NV: Lek Cluster - 47'), ('386', 'NV: Lek Cluster - 48, 264'), ('387', 'NV: Lek Cluster - 51'), ('388', 'NV: Lek Cluster - 52'), ('389', 'NV: Lek Cluster - 53'), ('390', 'NV: Lek Cluster - 54'), ('391', 'NV: Lek Cluster - 55'), ('392', 'NV: Lek Cluster - 56'), ('393', 'NV: Lek Cluster - 57'), ('394', 'NV: Lek Cluster - 58'), ('395', 'NV: Lek Cluster - 60'), ('396', 'NV: Lek Cluster - 61'), ('397', 'NV: Lek Cluster - 64'), ('398', 'NV: Lek Cluster - 67'), ('399', 'NV: Lek Cluster - 68'), ('400', 'NV: Lek Cluster - 72'), ('401', 'NV: Lek Cluster - 73, 241'), ('402', 'NV: Lek Cluster - 73'), ('403', 'NV: Lek Cluster - 74'), ('404', 'NV: Lek Cluster - 75'), ('405', 'NV: Lek Cluster - 76'), ('406', 'NV: Lek Cluster - 76'), ('407', 'NV: Lek Cluster - 76'), ('408', 'NV: Lek Cluster - 77'), ('409', 'NV: Lek Cluster - 79'), ('410', 'NV: Lek Cluster - 81'), ('411', 'NV: Lek Cluster - 81'), ('412', 'NV: Lek Cluster - 83, 85'), ('414', 'NV: Lek Cluster - 91'), ('415', 'NV: Lek Cluster - 93'), ('416', 'NV: Lek Cluster - 97'), ('417', 'NV: Lek Cluster - 97'), ('418', 'NV: Lek Cluster - 222, 337'), ('419', 'NV: Lek Cluster - 234'), ('420', 'NV: Lek Cluster - 234'), ('421', 'NV: Lek Cluster - 238'), ('422', 'NV: Lek Cluster - 239'), ('424', 'NV: Lek Cluster - 242'), ('425', 'NV: Lek Cluster - 245'), ('426', 'NV: Lek Cluster - 246'), ('427', 'NV: Lek Cluster - 247'), ('428', 'NV: Lek Cluster - 252'), ('429', 'NV: Lek Cluster - 254'), ('430', 'NV: Lek Cluster - 256'), ('431', 'NV: Lek Cluster - 257'), ('432', 'NV: Lek Cluster - 258'), ('433', 'NV: Lek Cluster - 260'), ('434', 'NV: Lek Cluster - 261'), ('435', 'NV: Lek Cluster - 262'), ('438', 'NV: Lek Cluster - 266'), ('439', 'NV: Lek Cluster - 268'), ('440', 'NV: Lek Cluster - 269'), ('441', 'NV: Lek Cluster - 272'), ('442', 'NV: Lek Cluster - 274'), ('443', 'NV: Lek Cluster - 275'), ('444', 'NV: Lek Cluster - 276'), ('445', 'NV: Lek Cluster - 282'), ('446', 'NV: Lek Cluster - 283'), ('447', 'NV: Lek Cluster - 284'), ('448', 'NV: Lek Cluster - 285'), ('450', 'NV: Lek Cluster - 287'), ('451', 'NV: Lek Cluster - 294'), ('452', 'NV: Lek Cluster - 297'), ('453', 'NV: Lek Cluster - 298, 305, 326'), ('454', 'NV: Lek Cluster - 300'), ('455', 'NV: Lek Cluster - 304, 311'), ('457', 'NV: Lek Cluster - 307'), ('458', 'NV: Lek Cluster - 308'), ('459', 'NV: Lek Cluster - 310'), ('460', 'NV: Lek Cluster - 313'), ('461', 'NV: Lek Cluster - 314'), ('462', 'NV: Lek Cluster - 315'), ('463', 'NV: Lek Cluster - 316'), ('464', 'NV: Lek Cluster - 317'), ('465', 'NV: Lek Cluster - 318'), ('466', 'NV: Lek Cluster - 319, 320'), ('470', 'NV: Lek Cluster - 323'), ('473', 'NV: Lek Cluster - 327'), ('474', 'NV: Lek Cluster - 328'), ('475', 'NV: Lek Cluster - 329'), ('476', 'NV: Lek Cluster - 332'), ('477', 'NV: Lek Cluster - 333'), ('478', 'NV: Lek Cluster - 334'), ('479', 'NV: Lek Cluster - 336'), ('481', 'NV: Lek Cluster - 449'), ('484', 'NV: Lek Cluster - 452'), ('485', 'NV: Lek Cluster - 453'), ('486', 'NV: Lek Cluster - 457'), ('487', 'NV: Lek Cluster - 472'), ('488', 'NV: Lek Cluster - 473'), ('489', 'NV: Lek Cluster - 303'), ('491', 'UT: Lek Cluster - 1'), ('492', 'UT: Lek Cluster - 2'), ('493', 'UT: Lek Cluster - 3'), ('494', 'UT: Lek Cluster - 4'), ('496', 'UT: Lek Cluster - 5'), ('497', 'UT: Lek Cluster - 8'), ('500', 'UT: Lek Cluster - 9'), ('502', 'UT: Lek Cluster - 12'), ('504', 'UT: Lek Cluster - 16'), ('509', 'UT: Lek Cluster - 21'), ('511', 'UT: Lek Cluster - 30'), ('513', 'UT: Lek Cluster - 32'), ('515', 'UT: Lek Cluster - 33'), ('520', 'UT: Lek Cluster - 36'), ('521', 'UT: Lek Cluster - 39, 48, 258'), ('522', 'UT: Lek Cluster - 44'), ('523', 'UT: Lek Cluster - 46'), ('525', 'UT: Lek Cluster - 49'), ('526', 'UT: Lek Cluster - 50'), ('527', 'UT: Lek Cluster - 59'), ('529', 'UT: Lek Cluster - 62'), ('530', 'UT: Lek Cluster - 65'), ('531', 'UT: Lek Cluster - 66'), ('533', 'UT: Lek Cluster - 78'), ('534', 'UT: Lek Cluster - 86'), ('535', 'UT: Lek Cluster - 166'), ('536', 'UT: Lek Cluster - 231, 232'), ('538', 'UT: Lek Cluster - 240'), ('539', 'UT: Lek Cluster - 244'), ('541', 'UT: Lek Cluster - 248'), ('542', 'UT: Lek Cluster - 250'), ('543', 'UT: Lek Cluster - 253'), ('544', 'UT: Lek Cluster - 255, 459, 460'), ('546', 'UT: Lek Cluster - 265'), ('547', 'UT: Lek Cluster - 270'), ('548', 'UT: Lek Cluster - 273'), ('549', 'UT: Lek Cluster - 277'), ('551', 'UT: Lek Cluster - 289'), ('552', 'UT: Lek Cluster - 290'), ('553', 'UT: Lek Cluster - 292'), ('554', 'UT: Lek Cluster - 299'), ('555', 'UT: Lek Cluster - 304'), ('556', 'UT: Lek Cluster - 310'), ('557', 'UT: Lek Cluster - 331'), ('558', 'UT: Lek Cluster - 373'), ('559', 'UT: Lek Cluster - 387'), ('560', 'UT: Lek Cluster - 404'), ('561', 'UT: Lek Cluster - 454'), ('562', 'UT: Lek Cluster - 455'), ('563', 'UT: Lek Cluster - 456'), ('564', 'UT: Lek Cluster - 10'), ('567', 'UT: Lek Cluster - 284'), ('568', 'WY: Lek Cluster - 62'), ('569', 'WY: Lek Cluster - 63'), ('570', 'WY: Lek Cluster - 66'), ('571', 'WY: Lek Cluster - 69, 253'), ('572', 'WY: Lek Cluster - 70'), ('573', 'WY: Lek Cluster - 71'), ('574', 'WY: Lek Cluster - 80'), ('575', 'WY: Lek Cluster - 82'), ('576', 'WY: Lek Cluster - 87'), ('577', 'WY: Lek Cluster - 89'), ('578', 'WY: Lek Cluster - 90'), ('579', 'WY: Lek Cluster - 94, 373'), ('581', 'WY: Lek Cluster - 95'), ('582', 'WY: Lek Cluster - 96'), ('583', 'WY: Lek Cluster - 98'), ('584', 'WY: Lek Cluster - 99'), ('585', 'WY: Lek Cluster - 101'), ('586', 'WY: Lek Cluster - 102'), ('587', 'WY: Lek Cluster - 103'), ('588', 'WY: Lek Cluster - 104'), ('589', 'WY: Lek Cluster - 105'), ('590', 'WY: Lek Cluster - 106, 110'), ('591', 'WY: Lek Cluster - 107'), ('594', 'WY: Lek Cluster - 113'), ('595', 'WY: Lek Cluster - 126'), ('596', 'WY: Lek Cluster - 127, 379, 407'), ('597', 'WY: Lek Cluster - 196, 202'), ('599', 'WY: Lek Cluster - 204'), ('600', 'WY: Lek Cluster - 207'), ('601', 'WY: Lek Cluster - 209'), ('602', 'WY: Lek Cluster - 211'), ('603', 'WY: Lek Cluster - 213'), ('604', 'WY: Lek Cluster - 215'), ('605', 'WY: Lek Cluster - 218, 395'), ('606', 'WY: Lek Cluster - 219'), ('607', 'WY: Lek Cluster - 220'), ('608', 'WY: Lek Cluster - 223'), ('609', 'WY: Lek Cluster - 224'), ('610', 'WY: Lek Cluster - 229'), ('611', 'WY: Lek Cluster - 230'), ('612', 'WY: Lek Cluster - 233'), ('613', 'WY: Lek Cluster - 235'), ('614', 'WY: Lek Cluster - 236'), ('615', 'WY: Lek Cluster - 237'), ('616', 'WY: Lek Cluster - 243'), ('617', 'WY: Lek Cluster - 249'), ('618', 'WY: Lek Cluster - 251'), ('620', 'WY: Lek Cluster - 255'), ('621', 'WY: Lek Cluster - 259'), ('622', 'WY: Lek Cluster - 293'), ('623', 'WY: Lek Cluster - 295'), ('624', 'WY: Lek Cluster - 296'), ('625', 'WY: Lek Cluster - 342'), ('626', 'WY: Lek Cluster - 362'), ('627', 'WY: Lek Cluster - 363'), ('629', 'WY: Lek Cluster - 365'), ('630', 'WY: Lek Cluster - 366'), ('631', 'WY: Lek Cluster - 367'), ('632', 'WY: Lek Cluster - 370'), ('633', 'WY: Lek Cluster - 371'), ('634', 'WY: Lek Cluster - 372'), ('636', 'WY: Lek Cluster - 374'), ('637', 'WY: Lek Cluster - 375'), ('638', 'WY: Lek Cluster - 376'), ('639', 'WY: Lek Cluster - 377'), ('641', 'WY: Lek Cluster - 378'), ('643', 'WY: Lek Cluster - 380'), ('644', 'WY: Lek Cluster - 381'), ('645', 'WY: Lek Cluster - 382'), ('646', 'WY: Lek Cluster - 383'), ('647', 'WY: Lek Cluster - 384'), ('648', 'WY: Lek Cluster - 385'), ('649', 'WY: Lek Cluster - 386'), ('650', 'WY: Lek Cluster - 388'), ('651', 'WY: Lek Cluster - 389'), ('652', 'WY: Lek Cluster - 390'), ('653', 'WY: Lek Cluster - 391'), ('654', 'WY: Lek Cluster - 393'), ('655', 'WY: Lek Cluster - 394'), ('657', 'WY: Lek Cluster - 396'), ('658', 'WY: Lek Cluster - 397'), ('659', 'WY: Lek Cluster - 398'), ('660', 'WY: Lek Cluster - 399'), ('661', 'WY: Lek Cluster - 400'), ('662', 'WY: Lek Cluster - 401'), ('663', 'WY: Lek Cluster - 402'), ('664', 'WY: Lek Cluster - 403'), ('665', 'WY: Lek Cluster - 404'), ('666', 'WY: Lek Cluster - 405'), ('667', 'WY: Lek Cluster - 406'), ('669', 'WY: Lek Cluster - 408'), ('670', 'WY: Lek Cluster - 409'), ('671', 'WY: Lek Cluster - 410'), ('672', 'WY: Lek Cluster - 419, 423'), ('674', 'WY: Lek Cluster - 458'), ('675', 'WY: Lek Cluster - 459'), ('676', 'WY: Lek Cluster - 462'), ('677', 'WY: Lek Cluster - 465'), ('678', 'WY: Lek Cluster - 466'), ('679', 'WY: Lek Cluster - 467'), ('680', 'WY: Lek Cluster - 468'), ('681', 'WY: Lek Cluster - 469'), ('682', 'WY: Lek Cluster - 471'), ('684', 'WY: Lek Cluster - 392')
)

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
        print(1)
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