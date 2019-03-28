CREATE TABLE `accounts_elidgbleusers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `userdisplay` varchar(250) NOT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE `accounts_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE `accounts_office_values` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `office` varchar(100) NOT NULL,
  `state` varchar(2) NOT NULL,
  `agency` varchar(75) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `office` (`office`)
) 

CREATE TABLE `accounts_useredits` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_useredits_936913d1` (`userid_id`),
  CONSTRAINT `userid_id_refs_id_8f5c93b3` FOREIGN KEY (`userid_id`) REFERENCES `auth_user` (`id`)
)

CREATE TABLE `accounts_useredits_editinguser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `useredits_id` int(11) NOT NULL,
  `elidgbleusers_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `useredits_id` (`useredits_id`,`elidgbleusers_id`),
  KEY `accounts_useredits_editinguser_7b80a08a` (`useredits_id`),
  KEY `accounts_useredits_editinguser_962b0353` (`elidgbleusers_id`),
  CONSTRAINT `elidgbleusers_id_refs_id_1e264b10` FOREIGN KEY (`elidgbleusers_id`) REFERENCES `accounts_elidgbleusers` (`id`),
  CONSTRAINT `useredits_id_refs_id_1f3a909d` FOREIGN KEY (`useredits_id`) REFERENCES `accounts_useredits` (`id`)
)

CREATE TABLE `accounts_usergroups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_usergroups_936913d1` (`userid_id`)
)

CREATE TABLE `accounts_usergroups_groupid` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usergroups_id` int(11) NOT NULL,
  `groups_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usergroups_id` (`usergroups_id`,`groups_id`),
  KEY `accounts_usergroups_groupid_8e8` (`usergroups_id`),
  KEY `accounts_usergroups_groupid_909` (`groups_id`)
)

CREATE TABLE `accounts_userprofile` (
  `User_id` int(11) NOT NULL,
  `User_Phone_Number` varchar(25) NOT NULL,
  `Agency` varchar(50) NOT NULL,
  `Field_Office` varchar(100) NOT NULL,
  `Approving_Official` varchar(50) DEFAULT NULL,
  `Date_Approved` datetime DEFAULT NULL,
  `Waiver_Approved` int(11) NOT NULL,
  `User_Approved` int(11) DEFAULT NULL,
  `Date_Waiver_Approved` datetime DEFAULT NULL,
  `Attempts_Remaining` int(11) NOT NULL DEFAULT '3',
  `Waiver_V2_Approved` int(1) DEFAULT NULL,
  `Date_V2_Waiver_Approved` datetime DEFAULT NULL,
  PRIMARY KEY (`User_id`),
  UNIQUE KEY `User_id` (`User_id`)
)

CREATE TABLE `activity_lut` (
  `id` int(11) NOT NULL DEFAULT '0',
  `activity` varchar(200) DEFAULT NULL,
  `typeact_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `typeact_id` (`typeact_id`),
  CONSTRAINT `activity_lut_ibfk_1` FOREIGN KEY (`typeact_id`) REFERENCES `typeact_lut` (`id`)
)

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
)

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`)
)

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`)
)

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) DEFAULT NULL,
  `last_name` varchar(30) DEFAULT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
)

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`)
)

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340` (`user_id`),
  KEY `auth_user_user_permissions_83d7` (`permission_id`)
)

CREATE TABLE `ced_main_activity_plan_values` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Activity` varchar(100) DEFAULT NULL,
  `SubActivity` varchar(150) DEFAULT NULL,
  `Metric` varchar(100) DEFAULT NULL,
  `TypeAct` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE `ced_main_agreement_protect` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Project_ID` int(11) NOT NULL,
  `Sage_Elim` double DEFAULT '0',
  `Ag_Conv` double DEFAULT '0',
  `Improper_Graze` double DEFAULT '0',
  `Infastructure` double DEFAULT '0',
  `Energy_Development` double DEFAULT '0',
  `Mining` double DEFAULT '0',
  `Recreation` double DEFAULT '0',
  `Urbanization_SubDevel` double DEFAULT '0',
  `Date_Entered` datetime NOT NULL,
  `User` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ced_main_agreement_protect_01bf33d5` (`Project_ID`),
  CONSTRAINT `ced_main_agreement_protect_ibfk_1` FOREIGN KEY (`Project_ID`) REFERENCES `ced_main_project_info` (`Project_ID`) ON DELETE CASCADE
)

CREATE TABLE `ced_main_batchupload` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `FolderName` varchar(200) DEFAULT NULL,
  `FileName` varchar(200) DEFAULT NULL,
  `LCMItem` varchar(50) DEFAULT NULL,
  `UploadStatus` varchar(20) DEFAULT NULL,
  `Upload_Date` datetime DEFAULT NULL,
  `Uploading_User` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE `ced_main_batchupload_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Batch_Group_ID` int(11) DEFAULT NULL,
  `BatchUpload_ID` int(11) DEFAULT NULL,
  `Group_Designation` varchar(100) DEFAULT NULL,
  `Effort_ID_List` varchar(100) DEFAULT NULL,
  `Type_Act` varchar(30) DEFAULT NULL,
  `Group_Status` varchar(100) DEFAULT NULL,
  `Upload_Date` datetime DEFAULT NULL,
  `Uploading_User` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE `ced_main_collab_party` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Project_ID` int(11) NOT NULL,
  `Date_Entered` datetime NOT NULL,
  `User` varchar(50) NOT NULL,
  `Collab_Party` varchar(75) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ced_main_collab_party_01bf33d5` (`Project_ID`),
  CONSTRAINT `ced_main_collab_party_ibfk_1` FOREIGN KEY (`Project_ID`) REFERENCES `ced_main_project_info` (`Project_ID`) ON DELETE CASCADE
)

CREATE TABLE `ced_main_collab_party_collab_party` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `collab_party_id` int(11) NOT NULL,
  `imp_party_values_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `collab_party_id` (`collab_party_id`,`imp_party_values_id`),
  KEY `ced_main_collab_party_Collab_Party_c5dc17d6` (`collab_party_id`),
  KEY `ced_main_collab_party_Collab_Party_1b8bc056` (`imp_party_values_id`),
  CONSTRAINT `ced_main_collab_party_collab_party_ibfk_1` FOREIGN KEY (`collab_party_id`) REFERENCES `ced_main_collab_party` (`id`) ON DELETE CASCADE,
  CONSTRAINT `imp_party_values_id_refs_id_129a6b6d` FOREIGN KEY (`imp_party_values_id`) REFERENCES `ced_main_imp_party_values` (`id`)
)

CREATE TABLE `ced_main_county` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `County` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE `ced_main_county_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Project_ID` int(11) NOT NULL,
  `Date_Entered` datetime NOT NULL,
  `User` varchar(50) NOT NULL,
  `County_Value` varchar(52) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ced_main_county_info_01bf33d5` (`Project_ID`),
  CONSTRAINT `ced_main_county_info_ibfk_1` FOREIGN KEY (`Project_ID`) REFERENCES `ced_main_project_info` (`Project_ID`) ON DELETE CASCADE
)

CREATE TABLE `ced_main_county_info_county_value` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `county_info_id` int(11) NOT NULL,
  `state_county_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `county_info_id` (`county_info_id`,`state_county_id`),
  KEY `ced_main_county_info_County_Value_114a09d6` (`county_info_id`),
  KEY `ced_main_county_info_County_Value_22060fb4` (`state_county_id`),
  CONSTRAINT `ced_main_county_info_county_value_ibfk_1` FOREIGN KEY (`county_info_id`) REFERENCES `ced_main_county_info` (`id`) ON DELETE CASCADE,
  CONSTRAINT `state_county_id_refs_id_d2b81f64` FOREIGN KEY (`state_county_id`) REFERENCES `ced_main_state_county` (`id`)
)

CREATE TABLE `ced_main_documentation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Project_ID` int(11) DEFAULT NULL,
  `File_Type` varchar(255) DEFAULT NULL,
  `Document_Description` varchar(255) DEFAULT NULL,
  `Document_Name` varchar(255) DEFAULT NULL,
  `Date_Entered` datetime DEFAULT NULL,
  `User` varchar(50) NOT NULL,
  `LCMItem` varchar(50) DEFAULT NULL,
  `LCJason` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_doc_proj` (`Project_ID`),
  CONSTRAINT `ced_main_documentation_ibfk_1` FOREIGN KEY (`Project_ID`) REFERENCES `ced_main_project_info` (`Project_ID`) ON DELETE CASCADE
)

CREATE TABLE `ced_main_documentation_values` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `File_Type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE `ced_main_fwsreview` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Project_ID` int(11) NOT NULL,
  `Threat` varchar(60) NOT NULL,
  `Date_Certified` datetime NOT NULL,
  `Certifier_Name` varchar(255) NOT NULL,
  `Service_Assessment` longtext NOT NULL,
  `Service_Assessment_Explained` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_fwsrev_proj` (`Project_ID`),
  CONSTRAINT `ced_main_fwsreview_ibfk_1` FOREIGN KEY (`Project_ID`) REFERENCES `ced_main_project_info` (`Project_ID`) ON DELETE CASCADE
)

CREATE TABLE `ced_main_huc12` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `HUC_12` varchar(50) NOT NULL,
  `HUC12_Name` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE `ced_main_huc12_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Project_ID` int(11) NOT NULL,
  `Date_Entered` datetime NOT NULL,
  `User` varchar(50) NOT NULL,
  `HUC12_Value` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ced_main_huc12_info_01bf33d5` (`Project_ID`),
  CONSTRAINT `ced_main_huc12_info_ibfk_1` FOREIGN KEY (`Project_ID`) REFERENCES `ced_main_project_info` (`Project_ID`) ON DELETE CASCADE
)

CREATE TABLE `ced_main_huc12_info_huc12_value` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `huc12_info_id` int(11) NOT NULL,
  `state_county_huc12_values_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `huc12_info_id` (`huc12_info_id`,`state_county_huc12_values_id`),
  KEY `ced_main_huc12_info_HUC12_Value_52886997` (`huc12_info_id`),
  KEY `ced_main_huc12_info_HUC12_Value_8b64839e` (`state_county_huc12_values_id`),
  CONSTRAINT `ced_main_huc12_info_huc12_value_ibfk_1` FOREIGN KEY (`huc12_info_id`) REFERENCES `ced_main_huc12_info` (`id`) ON DELETE CASCADE,
  CONSTRAINT `state_county_huc12_values_id_refs_id_5f3dfbe9` FOREIGN KEY (`state_county_huc12_values_id`) REFERENCES `ced_main_state_county_huc12_values` (`id`)
)

CREATE TABLE `ced_main_imp_party_values` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Implementation_Party` varchar(75) NOT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE `ced_main_implementation_info` (
  `Project_ID` int(11) NOT NULL,
  `Imp_Status` int(11) DEFAULT NULL,
  `Start_Date` date DEFAULT NULL,
  `Finish_Date` date DEFAULT NULL,
  `In_Perpetuity` tinyint(1) DEFAULT NULL,
  `Effective_Determined` int(11) DEFAULT NULL,
  `Effective_Explained` longtext,
  `Reas_Certain` int(11) DEFAULT NULL,
  `Legal_Authority` int(11) DEFAULT NULL,
  `Staff_Available` int(11) DEFAULT NULL,
  `Regulatory_Mech` int(11) DEFAULT NULL,
  `Compliance` int(11) DEFAULT NULL,
  `Vol_Incentives` int(11) DEFAULT NULL,
  `Reduce_Threats` int(11) DEFAULT NULL,
  `Incremental_Objectives` int(11) DEFAULT NULL,
  `Quantifiable_Measures` int(11) DEFAULT NULL,
  `AD_Strategy` int(11) DEFAULT NULL,
  `Imp_and_Effect_Correct` int(11) DEFAULT NULL,
  `Imp_and_Effect_Cor_Explan` longtext,
  `Date_Entered` datetime NOT NULL,
  `User` varchar(50) NOT NULL,
  `Prj_ID` int(11) DEFAULT NULL,
  `Project_Name` varchar(255) DEFAULT NULL,
  `Methods_Explained` longtext,
  PRIMARY KEY (`Project_ID`)
)

CREATE TABLE `ced_main_location_check` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `State` varchar(2) NOT NULL,
  `County` varchar(50) NOT NULL,
  `HUC12` varchar(50) NOT NULL,
  `Pop_Name` varchar(50) NOT NULL,
  `WAFWA_Zone` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE `ced_main_location_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Project_ID` int(11) NOT NULL,
  `Loc_Type` varchar(50) NOT NULL,
  `Loc_Value` varchar(100) NOT NULL,
  `Date_Entered` datetime NOT NULL,
  `User` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ced_main_location_info_01bf33d5` (`Project_ID`),
  CONSTRAINT `ced_main_location_info_ibfk_1` FOREIGN KEY (`Project_ID`) REFERENCES `ced_main_project_info` (`Project_ID`) ON DELETE CASCADE
)

CREATE TABLE `ced_main_metric` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Metric` varchar(100) NOT NULL,
  `Text` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_name` (`Metric`)
)

CREATE TABLE `ced_main_metrics` (
  `Project_ID` int(11) NOT NULL,
  `TotalAcres` double DEFAULT NULL,
  `TotalMiles` double DEFAULT NULL,
  `Date_Entered` datetime NOT NULL,
  `User` varchar(100) NOT NULL,
  KEY `ced_main_metrics_indx` (`Project_ID`),
  CONSTRAINT `ced_main_metrics_ibfk_1` FOREIGN KEY (`Project_ID`) REFERENCES `ced_main_project_info` (`Project_ID`) ON DELETE CASCADE
)

CREATE TABLE `ced_main_ownership_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Project_ID` int(11) NOT NULL,
  `Date_Entered` datetime NOT NULL,
  `User` varchar(50) NOT NULL,
  `Owner_Value` varchar(75) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ced_main_ownership_info_01bf33d5` (`Project_ID`),
  CONSTRAINT `ced_main_ownership_info_ibfk_1` FOREIGN KEY (`Project_ID`) REFERENCES `ced_main_project_info` (`Project_ID`) ON DELETE CASCADE
)

CREATE TABLE `ced_main_ownership_info_owner_value` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ownership_info_id` int(11) NOT NULL,
  `ownership_values_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ownership_info_id` (`ownership_info_id`,`ownership_values_id`),
  KEY `ced_main_ownership_info_Owner_Value_ff2f8fbd` (`ownership_info_id`),
  KEY `ced_main_ownership_info_Owner_Value_65611d9b` (`ownership_values_id`),
  CONSTRAINT `ced_main_ownership_info_owner_value_ibfk_1` FOREIGN KEY (`ownership_info_id`) REFERENCES `ced_main_ownership_info` (`id`) ON DELETE CASCADE,
  CONSTRAINT `ownership_values_id_refs_id_5ab549d8` FOREIGN KEY (`ownership_values_id`) REFERENCES `ced_main_ownership_values` (`id`)
)

CREATE TABLE `ced_main_ownership_values` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Owners` varchar(75) NOT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE `ced_main_population_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Project_ID` int(11) NOT NULL,
  `Date_Entered` datetime NOT NULL,
  `User` varchar(50) NOT NULL,
  `Population_Value` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ced_main_population_info_01bf33d5` (`Project_ID`),
  CONSTRAINT `ced_main_population_info_ibfk_1` FOREIGN KEY (`Project_ID`) REFERENCES `ced_main_project_info` (`Project_ID`) ON DELETE CASCADE
)

CREATE TABLE `ced_main_population_info_population_value` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `population_info_id` int(11) NOT NULL,
  `population_values_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `population_info_id` (`population_info_id`,`population_values_id`),
  KEY `ced_main_population_info_Population_Value_d33ea740` (`population_info_id`),
  KEY `ced_main_population_info_Population_Value_3b63ad42` (`population_values_id`),
  CONSTRAINT `ced_main_population_info_population_value_ibfk_1` FOREIGN KEY (`population_info_id`) REFERENCES `ced_main_population_info` (`id`) ON DELETE CASCADE,
  CONSTRAINT `population_values_id_refs_id_0f4eb96d` FOREIGN KEY (`population_values_id`) REFERENCES `ced_main_population_values` (`id`)
)

CREATE TABLE `ced_main_population_values` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Populations` varchar(100) NOT NULL,
  `Pop_Name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE `ced_main_project_info` (
  `Project_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Project_Name` varchar(75) DEFAULT NULL,
  `Entry_Type` int(11) DEFAULT NULL,
  `Shapefile` varchar(255) DEFAULT NULL,
  `Metadata` varchar(255) DEFAULT NULL,
  `Location_Info` varchar(255) DEFAULT NULL,
  `Location_Desc` longtext,
  `activity` varchar(100) DEFAULT NULL,
  `subactivity` varchar(200) DEFAULT NULL,
  `Metric` varchar(60) DEFAULT NULL,
  `Metric_Value` double DEFAULT NULL,
  `Objectives_Desc` longtext,
  `Effects_Desc` longtext,
  `Implementing_Party` varchar(50) DEFAULT NULL,
  `Office` varchar(100) DEFAULT NULL,
  `Created_By` varchar(50) DEFAULT NULL,
  `Date_Created` datetime DEFAULT NULL,
  `User_Phone_Number` varchar(12) DEFAULT NULL,
  `User_Email` varchar(100) DEFAULT NULL,
  `Project_Status` int(11) DEFAULT NULL,
  `Last_Updated` datetime DEFAULT NULL,
  `Updating_User` varchar(50) DEFAULT NULL,
  `Approved` int(11) DEFAULT NULL,
  `Approving_Official` varchar(50) DEFAULT NULL,
  `Date_Approved` datetime DEFAULT NULL,
  `TypeAct` varchar(40) DEFAULT NULL,
  `PageLoc` varchar(15) DEFAULT 'None',
  `LCMItem` varchar(50) DEFAULT NULL,
  `LC_Zoom` int(11) DEFAULT NULL,
  `LC_Center_X` double DEFAULT NULL,
  `LC_Center_Y` double DEFAULT NULL,
  `Notes` longtext,
  `Agreement_Length` int(11) DEFAULT '0',
  `Agreement_Penalty` int(11) DEFAULT '0',
  `Mark_For_Deletion` tinyint(1) DEFAULT '0',
  `Wobble_GIS` tinyint(1) DEFAULT '0',
  `Batch_Upload` tinyint(1) DEFAULT '0',
  `Wobbled_GIS` tinyint(1) DEFAULT '0',
  `Start_Date` date DEFAULT NULL,
  `End_Date` date DEFAULT NULL,
  `Oil_Gas_Explain` longtext,
  `Feral_Equids_Explain` longtext,
  `Infrastructure_Explain` longtext,
  `Mining_Explain` longtext,
  `Recreation_Explain` longtext,
  `Urban_Devel_Explain` longtext,
  `Fire_Explain` longtext,
  `Improper_Grazing_Explain` longtext,
  `Isolated_Explain` longtext,
  `Invasives_Explained` longtext,
  `Sagebrush_Loss_Explain` longtext,
  `GIS_Acres` double DEFAULT NULL,
  `Conifer_Encroach_Explain` longtext,
  `Ag_Conversion_Explain` longtext,
  `Fire_Break_Width_ft` int(11) DEFAULT NULL,
  `CCAA_Num_Permit_Holders` int(11) DEFAULT NULL,
  `Type_of_Powerline` varchar(15) DEFAULT NULL,
  `BatchUploadFileName` varchar(255) DEFAULT NULL,
  `BatchUploadFolderName` varchar(255) DEFAULT NULL,
  `BatchUploadOBJECTID` int(11) DEFAULT NULL,
  `Prj_ID` int(11) DEFAULT NULL,
  `subactivity_id` int(11) DEFAULT NULL,
  `seeding_type` varchar(60) DEFAULT NULL,
  `post_fire` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Project_ID`)
)

CREATE TABLE `ced_main_project_query` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Project_ID` int(11) NOT NULL,
  `Project_Name` varchar(75) NOT NULL,
  `User` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_projqry_proj` (`Project_ID`),
  CONSTRAINT `ced_main_project_query_ibfk_1` FOREIGN KEY (`Project_ID`) REFERENCES `ced_main_project_info` (`Project_ID`) ON DELETE CASCADE
)

CREATE TABLE `ced_main_seeding` (
  `project_id` int(11) DEFAULT NULL,
  `seeding_type` varchar(20) DEFAULT NULL
)

CREATE TABLE `ced_main_state` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `State` varchar(2) NOT NULL,
  `StateName` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_name` (`State`)
)

CREATE TABLE `ced_main_state_county` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `State` varchar(2) NOT NULL,
  `County` varchar(50) NOT NULL,
  `Cnty_St` varchar(52) NOT NULL,
  PRIMARY KEY (`id`,`County`,`Cnty_St`)
)

CREATE TABLE `ced_main_state_county_huc12_values` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `State` varchar(2) NOT NULL,
  `County` varchar(50) NOT NULL,
  `HUC12` varchar(45) NOT NULL,
  `HUC12_Cnty_State` varchar(60) NOT NULL,
  `Cnty_St` varchar(52) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `HUC12_Cnty_State` (`HUC12_Cnty_State`)
)

CREATE TABLE `ced_main_state_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Project_ID` int(11) NOT NULL,
  `Date_Entered` datetime NOT NULL,
  `User` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ced_main_state_info_01bf33d5` (`Project_ID`),
  CONSTRAINT `ced_main_state_info_ibfk_1` FOREIGN KEY (`Project_ID`) REFERENCES `ced_main_project_info` (`Project_ID`) ON DELETE CASCADE
)

CREATE TABLE `ced_main_state_info_state_value` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `state_info_id` int(11) NOT NULL,
  `state_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `state_info_id` (`state_info_id`,`state_id`),
  KEY `ced_main_state_info_State_Value_0d5d64e7` (`state_info_id`),
  KEY `ced_main_state_info_State_Value_5654bf12` (`state_id`),
  CONSTRAINT `ced_main_state_info_state_value_ibfk_1` FOREIGN KEY (`state_info_id`) REFERENCES `ced_main_state_info` (`id`) ON DELETE CASCADE,
  CONSTRAINT `state_id_refs_id_2b1ecab5` FOREIGN KEY (`state_id`) REFERENCES `ced_main_state` (`id`)
)

CREATE TABLE `ced_main_subactivity_effective_state` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Date_Entered` datetime DEFAULT NULL,
  `User` varchar(50) DEFAULT NULL,
  `Effectiveness_Statement` varchar(200) DEFAULT NULL,
  `Project_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_subeffect_proj` (`Project_ID`),
  CONSTRAINT `ced_main_subactivity_effective_state_ibfk_1` FOREIGN KEY (`Project_ID`) REFERENCES `ced_main_project_info` (`Project_ID`) ON DELETE CASCADE
)

CREATE TABLE `ced_main_subactivity_methods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Date_Entered` datetime DEFAULT NULL,
  `User` varchar(50) DEFAULT NULL,
  `Method` varchar(200) DEFAULT NULL,
  `Project_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_submeth_proj` (`Project_ID`),
  CONSTRAINT `ced_main_subactivity_methods_ibfk_1` FOREIGN KEY (`Project_ID`) REFERENCES `ced_main_project_info` (`Project_ID`) ON DELETE CASCADE
)

CREATE TABLE `ced_main_subactivity_objectives` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Date_Entered` datetime DEFAULT NULL,
  `User` varchar(50) DEFAULT NULL,
  `Objective` varchar(200) DEFAULT NULL,
  `Project_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_subobj_proj` (`Project_ID`),
  CONSTRAINT `ced_main_subactivity_objectives_ibfk_1` FOREIGN KEY (`Project_ID`) REFERENCES `ced_main_project_info` (`Project_ID`) ON DELETE CASCADE
)

CREATE TABLE `ced_main_subactivity_old` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `SubActivity` varchar(100) NOT NULL,
  `Activity` varchar(100) NOT NULL,
  `TypeAct` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_name` (`SubActivity`)
)

CREATE TABLE `ced_main_threat_values` (
  `id` int(11) DEFAULT NULL,
  `Threats` varchar(75) DEFAULT NULL,
  `TypeAct` varchar(20) DEFAULT NULL
)

CREATE TABLE `ced_main_threats` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Project_ID` int(11) NOT NULL,
  `Date_Entered` datetime NOT NULL,
  `User` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ced_main_threats_01bf33d5` (`Project_ID`),
  CONSTRAINT `ced_main_threats_ibfk_1` FOREIGN KEY (`Project_ID`) REFERENCES `ced_main_project_info` (`Project_ID`) ON DELETE CASCADE
)

CREATE TABLE `ced_main_threats_threat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `threats_id` int(11) NOT NULL,
  `threat_values_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `threats_id` (`threats_id`,`threat_values_id`),
  KEY `ced_main_threats_Threat_214ea0c2` (`threats_id`),
  KEY `ced_main_threats_Threat_73691a02` (`threat_values_id`)
)

CREATE TABLE `ced_main_typeact_legacy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `TypeAct` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_name` (`TypeAct`)
)

CREATE TABLE `ced_main_wafwa_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Project_ID` int(11) NOT NULL,
  `Date_Entered` datetime NOT NULL,
  `User` varchar(50) NOT NULL,
  `WAFWA_Value` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ced_main_wafwa_info_01bf33d5` (`Project_ID`),
  CONSTRAINT `ced_main_wafwa_info_ibfk_1` FOREIGN KEY (`Project_ID`) REFERENCES `ced_main_project_info` (`Project_ID`) ON DELETE CASCADE
)

CREATE TABLE `ced_main_wafwa_info_wafwa_value` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `wafwa_info_id` int(11) NOT NULL,
  `wafwa_zone_values_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `wafwa_info_id` (`wafwa_info_id`,`wafwa_zone_values_id`),
  KEY `ced_main_wafwa_info_WAFWA_Value_2fd02071` (`wafwa_info_id`),
  KEY `ced_main_wafwa_info_WAFWA_Value_3f2396f7` (`wafwa_zone_values_id`),
  CONSTRAINT `ced_main_wafwa_info_wafwa_value_ibfk_1` FOREIGN KEY (`wafwa_info_id`) REFERENCES `ced_main_wafwa_info` (`id`) ON DELETE CASCADE,
  CONSTRAINT `wafwa_zone_values_id_refs_id_51b422c8` FOREIGN KEY (`wafwa_zone_values_id`) REFERENCES `ced_main_wafwa_zone_values` (`id`)
)

CREATE TABLE `ced_main_wafwa_zone_values` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `WAFWA_Zone` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`)
)

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
)

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
)

CREATE TABLE `registration_registrationprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `activation_key` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
)

CREATE TABLE `subactivity_effective_state_data_lut` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `activity_id` int(11) DEFAULT NULL,
  `subactivity_id` int(11) DEFAULT NULL,
  `Effectiveness_Statement` varchar(200) DEFAULT NULL,
  `Ordering` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
)

CREATE TABLE `subactivity_effectiveness_rating_data_lut` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `activity_id` int(11) DEFAULT NULL,
  `subactivity_id` int(11) DEFAULT NULL,
  `Effectiveness_Rating` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE `subactivity_lut` (
  `id` int(11) NOT NULL DEFAULT '0',
  `subactivity` varchar(200) DEFAULT NULL,
  `activity_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT `subactivity_lut_ibfk_1` FOREIGN KEY (`activity_id`) REFERENCES `activity_lut` (`id`)
)

CREATE TABLE `subactivity_methods_data_lut` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `activity_id` int(11) DEFAULT NULL,
  `subactivity_id` int(11) DEFAULT NULL,
  `Method` varchar(200) DEFAULT NULL,
  `Ordering` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
)

CREATE TABLE `subactivity_objectives_data_lut` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `activity_id` int(11) DEFAULT NULL,
  `subactivity_id` int(11) DEFAULT NULL,
  `Objective` varchar(200) DEFAULT NULL,
  `Ordering` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
)

CREATE TABLE `typeact_lut` (
  `id` int(11) NOT NULL DEFAULT '0',
  `typeact` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
)

CREATE OR REPLACE VIEW `ced_main_activity` AS
select distinct `a`.`id` AS `id`,`a`.`activity` AS `activity`,
`b`.`typeact` AS `typeact`,concat(`a`.`activity`,' (',`b`.`typeact`,')') AS `Activity_Query_Label`
from (`activity_lut` `a` join `typeact_lut` `b`)
where (`a`.`typeact_id` = `b`.`id`);

CREATE OR REPLACE VIEW `ced_main_metrics_view` AS
select distinct `ced_main_project_info`.`Project_ID` AS `Project_ID`,
`ced_main_project_info`.`Metric_Value` AS `TotalAcres`,0 AS `TotalMiles`,
`ced_main_project_info`.`Date_Created` AS `Date_Entered`
from `ced_main_project_info`
where (`ced_main_project_info`.`Metric` = 'Acres')
union select distinct `ced_main_project_info`.`Project_ID` AS `Project_ID`,
0 AS `TotalAcres`,`ced_main_project_info`.`Metric_Value` AS `TotalMiles`,
`ced_main_project_info`.`Date_Created` AS `Date_Entered`
from `ced_main_project_info`
where (`ced_main_project_info`.`Metric` = 'Miles');

CREATE OR REPLACE VIEW `ced_main_subactivity` AS
select distinct `a`.`id` AS `id`,`a`.`subactivity` AS `subactivity`,`b`.`activity` AS `activity`,`c`.`typeact` AS `typeact`,concat(`a`.`subactivity`,' (',`b`.`activity`,')') AS `SubActivity_Query_Label` from ((`subactivity_lut` `a` join `activity_lut` `b`) join `typeact_lut` `c`) where ((`a`.`activity_id` = `b`.`id`) and (`b`.`typeact_id` = `c`.`id`));

CREATE OR REPLACE VIEW `ced_main_subactivity_effective_state_data` AS
select distinct `a`.`id` AS `id`,`c`.`activity` AS `activity`,`b`.`subactivity` AS `subactivity`,`a`.`Effectiveness_Statement` AS `Effectiveness_Statement`,`a`.`Ordering` AS `Ordering` from ((`subactivity_effective_state_data_lut` `a` join `subactivity_lut` `b`) join `activity_lut` `c`) where ((`a`.`subactivity_id` = `b`.`id`) and (`a`.`activity_id` = `c`.`id`));

CREATE OR REPLACE VIEW `ced_main_subactivity_effectiveness_rating_data` AS
select distinct `a`.`id` AS `id`,`b`.`activity` AS `Activity`,`c`.`subactivity` AS `SubActivity`,`a`.`Effectiveness_Rating` AS `Effectiveness_Rating` from ((`subactivity_effectiveness_rating_data_lut` `a` join `activity_lut` `b`) join `subactivity_lut` `c`) where ((`a`.`activity_id` = `b`.`id`) and (`a`.`subactivity_id` = `c`.`id`));

CREATE OR REPLACE VIEW `ced_main_subactivity_methods_data` AS
select distinct `a`.`id` AS `id`,`b`.`activity` AS `Activity`,`c`.`subactivity` AS `SubActivity`,`a`.`Method` AS `Method`,`a`.`Ordering` AS `Ordering` from ((`subactivity_methods_data_lut` `a` join `activity_lut` `b`) join `subactivity_lut` `c`) where ((`a`.`activity_id` = `b`.`id`) and (`a`.`subactivity_id` = `c`.`id`));

CREATE OR REPLACE VIEW `ced_main_subactivity_objectives_data` AS
select distinct `a`.`id` AS `id`,`b`.`activity` AS `Activity`,`c`.`subactivity` AS `SubActivity`,
`a`.`Objective` AS `Objective`,`a`.`Ordering` AS `Ordering` from ((`subactivity_objectives_data_lut` `a`
join `activity_lut` `b`) join `subactivity_lut` `c`) where ((`a`.`activity_id` = `b`.`id`)
and (`a`.`subactivity_id` = `c`.`id`));

CREATE OR REPLACE VIEW `ced_main_typeact` AS
select distinct `ced`.`typeact_lut`.`id` AS `id`,`ced`.`typeact_lut`.`typeact` AS `typeact`
from `typeact_lut`;

CREATE OR REPLACE VIEW `qry_ced2ags_agreement_protect` AS
select distinct `a`.`id` AS `id`,`a`.`Project_ID` AS `Project_ID`,
`a`.`Sage_Elim` AS `Sage_Elim`,`a`.`Ag_Conv` AS `Ag_Conv`,`a`.`Improper_Graze` AS `Improper_Graze`,
`a`.`Infastructure` AS `Infastructure`,`a`.`Energy_Development` AS `Energy_Development`,
`a`.`Mining` AS `Mining`,`a`.`Recreation` AS `Recreation`,
`a`.`Urbanization_SubDevel` AS `Urbanization_SubDevel`,`a`.`Date_Entered` AS `Date_Entered`
from `ced_main_agreement_protect` `a`;

CREATE OR REPLACE VIEW `qry_ced2ags_collaborators` AS
select `p`.`Project_ID` AS `Project_ID`,`t`.`Implementation_Party` AS `Implementation_Party`,
`t`.`id` AS `COL_ID`
from ((`ced_main_imp_party_values` `t` join `ced_main_collab_party_collab_party` `s`)
join `ced_main_collab_party` `p`)
where ((`t`.`id` = `s`.`imp_party_values_id`) and (`s`.`collab_party_id` = `p`.`id`));

CREATE OR REPLACE VIEW `qry_ced2ags_county` AS
select `p`.`Project_ID` AS `Project_ID`,`t`.`State` AS `State`,`t`.`County` AS `County`,
`t`.`Cnty_St` AS `Cnty_St`,`t`.`id` AS `Cnty_ID`
from ((`ced_main_county_info_county_value` `s`
join `ced_main_county_info` `p`) join `ced_main_state_county` `t`)
where ((`s`.`county_info_id` = `p`.`id`) and (`s`.`state_county_id` = `t`.`id`));

CREATE OR REPLACE VIEW `qry_ced2ags_documentation` AS
select `a`.`id` AS `id`,`a`.`Project_ID` AS `Project_ID`,`a`.`File_Type` AS `File_Type`,
`a`.`Document_Description` AS `Document_Description`,`a`.`Document_Name` AS `Document_Name`,
`a`.`Date_Entered` AS `Date_Entered`,`a`.`LCMItem` AS `LCMItem`,`a`.`LCJason` AS `LCJason`
from `ced_main_documentation` `a`;

CREATE OR REPLACE VIEW `qry_ced2ags_huc12` AS
select `p`.`Project_ID` AS `Project_ID`,`t`.`State` AS `State`,`t`.`County` AS `County`,
`t`.`HUC12` AS `HUC12`,`t`.`HUC12_Cnty_State` AS `HUC12_Cnty_State`,`t`.`Cnty_St` AS `Cnty_St`
from ((`ced_main_huc12_info` `p` join `ced_main_huc12_info_huc12_value` `s`)
join `ced_main_state_county_huc12_values` `t`)
where ((`s`.`state_county_huc12_values_id` = `t`.`id`) and (`s`.`huc12_info_id` = `p`.`id`));

CREATE OR REPLACE VIEW `qry_ced2ags_office` AS
select `a`.`User_id` AS `User_id`,`a`.`User_Phone_Number` AS `User_Phone_Number`,
`a`.`Agency` AS `Agency`,`a`.`Field_Office` AS `Field_Office`,`s1`.`id` AS `FO_ID`
from (`accounts_userprofile` `a` join `accounts_office_values` `s1`)
where ((`s1`.`office` = `a`.`Field_Office`) and (`a`.`User_Phone_Number` <> ''));

CREATE OR REPLACE VIEW `qry_ced2ags_ownership` AS
select `p`.`Project_ID` AS `Project_ID`,`t`.`Owners` AS `Owners`,`t`.`id` AS `O_ID`
from ((`ced_main_ownership_info` `p` join `ced_main_ownership_info_owner_value` `s`)
join `ced_main_ownership_values` `t`)
where ((`p`.`id` = `s`.`ownership_info_id`) and (`s`.`ownership_values_id` = `t`.`id`));

CREATE OR REPLACE VIEW `qry_ced2ags_population` AS
select `p`.`Project_ID` AS `Project_ID`,`t`.`Populations` AS `Populations`,`t`.`Pop_Name` AS `Pop_Name`,
`t`.`id` AS `Pop_ID`
from ((`ced_main_population_info` `p` join `ced_main_population_info_population_value` `s`)
join `ced_main_population_values` `t`)
where ((`p`.`id` = `s`.`population_info_id`) and (`s`.`population_values_id` = `t`.`id`));

CREATE OR REPLACE VIEW `qry_ced2ags_state` AS
select `p`.`Project_ID` AS `Project_ID`,`t`.`State` AS `State`,`t`.`id` AS `ST_ID`
from ((`ced_main_state_info_state_value` `s` join `ced_main_state_info` `p`)
join `ced_main_state` `t`)
where ((`s`.`state_info_id` = `p`.`id`) and (`s`.`state_id` = `t`.`id`));

CREATE OR REPLACE VIEW `qry_ced2ags_threats` AS
select `p`.`Project_ID` AS `Project_ID`,`t`.`Threats` AS `Threats`,`t`.`id` AS `T_ID`
from ((`ced_main_threats_threat` `s` join `ced_main_threats` `p`) join `ced_main_threat_values` `t`)
where ((`s`.`threats_id` = `p`.`id`) and (`s`.`threat_values_id` = `t`.`id`));

CREATE OR REPLACE VIEW `qry_ced2ags_wafwa` AS
select `p`.`Project_ID` AS `Project_ID`,`t`.`WAFWA_Zone` AS `WAFWA_Zone`,`t`.`id` AS `WAFWA_ID`
from ((`ced_main_wafwa_info` `p` join `ced_main_wafwa_info_wafwa_value` `s`)
join `ced_main_wafwa_zone_values` `t`)
where ((`p`.`id` = `s`.`wafwa_info_id`) and (`s`.`wafwa_zone_values_id` = `t`.`id`));

