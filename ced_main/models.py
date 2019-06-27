from django.db import models

import datetime
now = datetime.datetime.now()

def_max_length = 255

class project_info(models.Model):
    Project_ID = models.AutoField(primary_key=True)
    Project_Name = models.CharField(unique=True, max_length=75)
    Entry_Type = models.IntegerField(default=0)
    Shapefile = models.CharField(max_length=255)
    Metadata = models.CharField(max_length=255)
    Location_Info = models.CharField(max_length=255)
    Location_Desc = models.TextField()
    TypeAct = models.CharField(max_length=30)
    Activity = models.CharField(max_length=75)
    SubActivity = models.CharField(max_length=100)
    seeding_type = models.CharField(max_length=60)
    post_fire = models.CharField(max_length=50)
    mitigation = models.CharField(max_length=20)
    Start_Date = models.DateField()
    End_Date = models.DateField()
    Objectives_Desc = models.TextField()
    Effects_Desc = models.TextField()
    Implementing_Party = models.TextField()
    Metric = models.CharField(max_length=10)
    Metric_Value = models.IntegerField(default=0)
    GIS_Acres = models.FloatField(default=0)
    Office = models.CharField(max_length=100)
    Created_By = models.CharField(max_length=50)
    Date_Created = models.DateTimeField(default=now)
    User_Phone_Number = models.CharField(max_length=12)
    User_Email = models.CharField(max_length=100)
    Project_Status = models.IntegerField(default=0)
    Last_Updated = models.DateTimeField(default=now)
    Updating_User = models.CharField(max_length=50)
    Approved = models.IntegerField(default=0)
    Approving_Official = models.CharField(max_length=50)
    Date_Approved = models.DateTimeField()
    PageLoc = models.CharField(max_length=15, default='None')
    LCMItem  = models.CharField(max_length=50)
    LC_Zoom = models.IntegerField(default=7)
    LC_Center_X = models.FloatField(default=0)
    LC_Center_Y = models.FloatField(default=0)
    Notes = models.TextField()
    Agreement_Length = models.IntegerField(default=0)
    Agreement_Penalty = models.IntegerField(default=0)
    Mark_For_Deletion = models.BooleanField(default=False)
    Wobble_GIS = models.BooleanField(default=False)
    Batch_Upload = models.BooleanField(default=False)
    Wobbled_GIS = models.BooleanField(default=False)

    Ag_Conversion_Explain = models.TextField()
    Conifer_Encroach_Explain = models.TextField()
    Oil_Gas_Explain = models.TextField()
    Feral_Equids_Explain = models.TextField()
    Infrastructure_Explain = models.TextField()
    Mining_Explain = models.TextField()
    Recreation_Explain = models.TextField()
    Urban_Devel_Explain = models.TextField()
    Fire_Explain = models.TextField()
    Improper_Grazing_Explain = models.TextField()
    Isolated_Explain = models.TextField()
    Invasives_Explained = models.TextField()
    Sagebrush_Loss_Explain = models.TextField()

    Fire_Break_Width_ft = models.IntegerField(default=0)
    CCAA_Num_Permit_Holders = models.IntegerField(default=0)
    Type_of_Powerline = models.TextField()
    BatchUploadFileName = models.TextField()
    BatchUploadFolderName = models.TextField()
    BatchUploadOBJECTID = models.IntegerField(default=0)
    Prj_ID = models.IntegerField(default=0)
   
    def __str__(self):
        return "%s" % self.Project_ID

class project_query(models.Model):
    Project_ID = models.IntegerField()
    Project_Name = models.CharField(max_length=75)
    User = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % self.Project_ID

class metrics(models.Model):
    Project_ID = models.IntegerField(primary_key=True, unique=True)
    BreedingNestingAcres = models.FloatField()
    BroodRearingAcres = models.FloatField()
    WinterAcres = models.FloatField()
    TotalAcres = models.FloatField()
    BreedingNestingMiles = models.FloatField()
    BroodRearingMiles = models.FloatField()
    WinterMiles = models.FloatField()
    TotalMiles = models.FloatField()
    BreedingNestingNumberBirds = models.FloatField()
    BroodRearingNumberBirds = models.FloatField()
    WinterNumberBirds = models.FloatField()
    TotalNumberBirds = models.FloatField()
    BreedingNestingNumberRemoved = models.FloatField()
    BroodRearingNumberRemoved = models.FloatField()
    WinterNumberRemoved = models.FloatField()
    TotalNumberRemoved = models.FloatField()
    BreedingNestingNumberKilled = models.FloatField()
    BroodRearingNumberKilled = models.FloatField()
    WinterNumberKilled = models.FloatField()
    TotalNumberKilled = models.FloatField()
    BreedingNestingEquids = models.FloatField()
    BroodRearingEquids = models.FloatField()
    WinterEquids = models.FloatField()
    TotalEquids = models.FloatField()
    Target_Species = models.CharField(max_length=75)
    Date_Entered = models.DateTimeField()
    User = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % self.Project_ID 

class agreement_protect(models.Model):
    Project_ID = models.IntegerField(primary_key=True, unique=True)
    Sage_Elim = models.FloatField(default=0)
    Ag_Conv = models.FloatField(default=0)
    Improper_Graze = models.FloatField(default=0)
    Infastructure = models.FloatField(default=0)
    Energy_Development = models.FloatField(default=0)
    Mining = models.FloatField(default=0)
    Recreation = models.FloatField(default=0)
    Urbanization_SubDevel = models.FloatField(default=0)
    Date_Entered = models.DateTimeField()
    User = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % self.Project_ID 

class location_info(models.Model):
    Project_ID = models.ForeignKey('project_info', on_delete=models.PROTECT, db_column='Project_ID')
    Loc_Type = models.CharField(max_length=50)
    Loc_Value = models.CharField(max_length=100)
    Date_Entered = models.DateTimeField()
    User = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.Project_ID

class state_info(models.Model):
    Project_ID = models.ForeignKey('project_info', on_delete=models.PROTECT, db_column='Project_ID')
    state_value = models.ManyToManyField('state', db_column='State')
    Date_Entered = models.DateTimeField()
    User = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.Project_ID

class county_info(models.Model):
    Project_ID = models.ForeignKey('project_info', on_delete=models.PROTECT, db_column='Project_ID')
    county_value = models.ManyToManyField('state_county', db_column='Cnty_St')
    Date_Entered = models.DateTimeField()
    User = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.Project_ID

class huc12_info(models.Model):
    Project_ID = models.ForeignKey('project_info', on_delete=models.PROTECT, db_column='Project_ID')
    huc12_value = models.ManyToManyField('state_county_huc12_values', db_column='HUC12_Cnty_State')
    Date_Entered = models.DateTimeField()
    User = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.Project_ID

class wafwa_info(models.Model):
    Project_ID = models.ForeignKey('project_info', on_delete=models.PROTECT, db_column='Project_ID')
    wafwa_value = models.ManyToManyField('wafwa_zone_values', db_column='WAFWA_Zone')
    Date_Entered = models.DateTimeField()
    User = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.Project_ID

class population_info(models.Model):
    Project_ID = models.ForeignKey('project_info', on_delete=models.PROTECT, db_column='Project_ID')
    population_value = models.ManyToManyField('population_values', db_column='Populations')
    Date_Entered = models.DateTimeField()
    User = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.Project_ID

class ownership_info(models.Model):
    Project_ID = models.ForeignKey('project_info', on_delete=models.PROTECT, db_column='Project_ID')
    owner_value = models.ManyToManyField('ownership_values', db_column='Owners')
    Date_Entered = models.DateTimeField()
    User = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.Project_ID

class threats(models.Model):
    Project_ID = models.ForeignKey('project_info', on_delete=models.PROTECT, db_column='Project_ID')
    threat = models.ManyToManyField('threat_values', db_column='Threats')
    Date_Entered = models.DateTimeField()
    User = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.Project_ID

class collab_party(models.Model):
    Project_ID = models.ForeignKey('project_info', on_delete=models.PROTECT, db_column='Project_ID')
    collab_party = models.ManyToManyField('imp_party_values', db_column='Implementation_Party')
    Date_Entered = models.DateTimeField()
    User = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.Project_ID

class implementation_info(models.Model):
    Project_ID = models.IntegerField(primary_key=True, unique=True)
    Prj_ID = models.IntegerField(default=0)
    Project_Name = models.TextField()
    Imp_Status = models.IntegerField(default=0)
    Start_Date = models.DateField()
    Finish_Date = models.DateField()
    In_Perpetuity = models.BooleanField()
    Methods_Explained = models.TextField()
    Effective_Determined = models.IntegerField(default=0)
    Effective_Explained = models.TextField()
    
    Reas_Certain = models.IntegerField(default=0)
    Legal_Authority = models.IntegerField(default=0)
    Staff_Available = models.IntegerField(default=0)
    Regulatory_Mech = models.IntegerField(default=0)
    Compliance = models.IntegerField(default=0)
    Vol_Incentives = models.IntegerField(default=0)
    
    Reduce_Threats = models.IntegerField(default=0)
    Incremental_Objectives = models.IntegerField(default=0)
    Quantifiable_Measures = models.IntegerField(default=0)
    AD_Strategy = models.IntegerField(default=0)
    
    Imp_and_Effect_Correct = models.IntegerField(default=0)
    Imp_and_Effect_Cor_Explan = models.TextField()
    
    Date_Entered = models.DateTimeField()
    User = models.CharField(max_length=50)
    
    def __str__(self):
        return "%s" % self.Project_ID

class subactivity_objectives(models.Model):
    Project_ID = models.ForeignKey('project_info', on_delete=models.PROTECT, db_column='Project_ID')
    objective = models.ManyToManyField('subactivity_objectives_data', db_column='Objective')
    Date_Entered = models.DateTimeField()
    User = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.Project_ID

class subactivity_methods(models.Model):
    Project_ID = models.ForeignKey('project_info', on_delete=models.PROTECT, db_column='Project_ID')
    method = models.ManyToManyField('subactivity_methods_data', db_column='Method')
    Date_Entered = models.DateTimeField()
    User = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.Project_ID

class subactivity_effective_state(models.Model):
    Project_ID = models.ForeignKey('project_info', on_delete=models.PROTECT, db_column='Project_ID')
    effectiveness_statement = models.ManyToManyField('subactivity_effective_state_data', db_column='Effectiveness_Statement')
    Date_Entered = models.DateTimeField()
    User = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.Project_ID

class documentation_values(models.Model):
    File_Type = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % self.File_Type

class activity_plan_values(models.Model):
    TypeAct = models.CharField(max_length=20)
    Activity = models.CharField(max_length=100)
    SubActivity = models.CharField(max_length=150)
    Metric = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % self.Metric

class typeact(models.Model):
    TypeAct = models.CharField(max_length=20)

    def __str__(self):
        return "%s" % self.TypeAct

class activity(models.Model):
    Activity = models.CharField(max_length=100)
    TypeAct = models.CharField(max_length=20)
    Activity_Query_Label = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % self.Activity

class subactivity(models.Model):
    SubActivity = models.CharField(max_length=100)
    Activity = models.CharField(max_length=100)
    TypeAct = models.CharField(max_length=20)
    SubActivity_Query_Label = models.CharField(max_length=250)

    def __str__(self):
        return "%s" % self.SubActivity


class metric(models.Model):
    Metric = models.CharField(max_length=100)
    Text = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.Metric

class ownership_values(models.Model):
    Owners = models.CharField(max_length=75)

    def __str__(self):
        return "%s" % self.Owners

class imp_party_values(models.Model):
    Implementation_Party = models.CharField(max_length=75)

    def __str__(self):
        return "%s" % self.Implementation_Party

class threat_values(models.Model):
    Threats = models.CharField(max_length=75)
    TypeAct = models.CharField(max_length=20)

    def __str__(self):
        return "%s" % self.Threats

class wafwa_zone_values(models.Model):
    WAFWA_Zone = models.CharField(max_length=10)

    def __str__(self):
        return "%s" % self.WAFWA_Zone

class population_values(models.Model):
    Populations = models.CharField(max_length=50)
    Pop_Name = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.Populations

class state(models.Model):
    State = models.CharField(max_length=2)
    StateName = models.CharField(max_length=30)

    def __str__(self):
        return "%s" % self.State


class county(models.Model):
    County = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.County

class huc12(models.Model):
    HUC_12 = models.CharField(max_length=50)
    HUC12_Name = models.CharField(max_length=40)

    def __str__(self):
        return "%s" % self.HUC_12

class state_county_huc12_values(models.Model):
    State = models.CharField(max_length=2)
    County = models.CharField(max_length=50)
    HUC12 = models.CharField(max_length=50)
    HUC12_Cnty_State = models.CharField(max_length=60)
    Cnty_St = models.CharField(max_length=52)

    def __str__(self):
        return "%s" % self.HUC12_Cnty_State

class state_county(models.Model):
    State = models.CharField(max_length=2)
    County = models.CharField(max_length=50)
    Cnty_St = models.CharField(max_length=52)

    def __str__(self):
        return "%s" % self.Cnty_St

class location_check(models.Model):
    State = models.CharField(max_length=2)
    County = models.CharField(max_length=50)
    HUC12 = models.CharField(max_length=50)
    Pop_Name = models.CharField(max_length=50)
    WAFWA_Zone = models.CharField(max_length=10)


class documentation(models.Model):
    Project_ID = models.IntegerField()
    File_Type = models.CharField(max_length=255)
    Document_Description = models.CharField(max_length=255)
    Document_Name = models.CharField(max_length=255)
    Date_Entered = models.DateTimeField()
    User = models.CharField(max_length=50)
    LCMItem = models.CharField(max_length=50)
    LCJason = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.Project_ID

class fwsreview(models.Model):
    Project_ID = models.IntegerField()
    Threat = models.CharField(max_length=60)
    Date_Certified = models.DateTimeField()
    Certifier_Name = models.CharField(max_length=255)
    Service_Assessment = models.CharField(max_length=255)
    Service_Assessment_Explained = models.TextField()

    def __str__(self):
        return "%s" % self.Project_ID

class batchupload(models.Model):
    FolderName = models.CharField(max_length=200)
    FileName = models.CharField(max_length=200)
    LCMItem  = models.CharField(max_length=50)
    UploadStatus  = models.CharField(max_length=20)
    Upload_Date = models.DateTimeField(default=now)
    Uploading_User = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.Uploading_User

class batchupload_groups(models.Model):
    Batch_Group_ID = models.IntegerField()
    BatchUpload_ID = models.IntegerField()
    Group_Designation = models.CharField(max_length=100)
    Effort_ID_List  = models.CharField(max_length=100)
    Type_Act = models.CharField(max_length=30)
    Group_Status  = models.CharField(max_length=100)
    Upload_Date = models.DateTimeField(default=now)
    Uploading_User = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.Uploading_User

class subactivity_objectives_data(models.Model):
    Activity = models.CharField(max_length=100)
    SubActivity = models.CharField(max_length=100)
    Objective = models.CharField(max_length=200)
    Ordering = models.IntegerField()

    def __str__(self):
        return "%s" % self.Objective

class subactivity_methods_data(models.Model):
    Activity = models.CharField(max_length=100)
    SubActivity = models.CharField(max_length=100)
    Method = models.CharField(max_length=200)
    Ordering = models.IntegerField()

    def __str__(self):
        return "%s" % self.Method

class subactivity_effectiveness_rating_data(models.Model):
    Activity = models.CharField(max_length=100)
    SubActivity = models.CharField(max_length=100)
    Effectiveness_Rating = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % self.Effectiveness_Rating

class subactivity_effective_state_data(models.Model):
    Activity = models.CharField(max_length=100)
    SubActivity = models.CharField(max_length=100)
    Effectiveness_Statement = models.CharField(max_length=200)
    Ordering = models.IntegerField()

    def __str__(self):
        return "%s" % self.Effectiveness_Statement