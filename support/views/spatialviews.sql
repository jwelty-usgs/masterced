CREATE OR REPLACE VIEW `qry_ced2ags_agreement_protect` AS
  select distinct `a`.`id` as `id`,
    `a`.`Project_ID` as `Project_ID`,
  `a`.`Sage_Elim` as `Sage_Elim`,
  `a`.`Ag_Conv` as `Ag_Conv`,
  `a`.`Improper_Graze` as `Improper_Graze`,
  `a`.`Infastructure` as `Infastructure`,
  `a`.`Energy_Development` as `Energy_Development`,
  `a`.`Mining` as `Mining`,
  `a`.`Recreation` as `Recreation`,
  `a`.`Urbanization_SubDevel` as `Urbanization_SubDevel`,
  `a`.`Date_Entered` as `Date_Entered`
from `ced_main_agreement_protect` `a`;

CREATE OR REPLACE VIEW `qry_ced2ags_collaborators` AS
  select `p`.`Project_ID` AS `Project_ID`,
         `t`.`Implementation_Party` AS `Implementation_Party`,
         `t`.`id` AS `COL_ID`
  from `ced_main_imp_party_values` `t`,
    `ced_main_collab_party_collab_party` `s`,
    `ced_main_collab_party` `p`
  where `t`.`id` = `s`.`imp_party_values_id`
        and `s`.`collab_party_id` = `p`.`id`;

CREATE OR REPLACE VIEW `qry_ced2ags_county` AS
  select `p`.`Project_ID` AS `Project_ID`,
         `t`.`State` AS `State`,
         `t`.`County` AS `County`,
         `t`.`Cnty_St` AS `Cnty_St`,
         `t`.`id` AS `Cnty_ID`
  from `ced_main_county_info_county_value` `s`,
    `ced_main_county_info` `p`,
    `ced_main_state_county` `t`
  where `s`.`county_info_id` = `p`.`id`
        and `s`.`state_county_id` = `t`.`id`;

CREATE OR REPLACE VIEW `qry_ced2ags_documentation` AS
  select `a`.`id` AS `id`,
         `a`.`Project_ID` AS `Project_ID`,
         `a`.`File_Type` AS `File_Type`,
         `a`.`Document_Description` AS `Document_Description`,
         `a`.`Document_Name` AS `Document_Name`,
         `a`.`Date_Entered` AS `Date_Entered`,
         `a`.`LCMItem` AS `LCMItem`,
         `a`.`LCJason` AS `LCJason`
  from `ced_main_documentation` `a`;

CREATE OR REPLACE VIEW `qry_ced2ags_huc12` AS
  select `p`.`Project_ID` AS `Project_ID`,
         `t`.`State` AS `State`,
         `t`.`County` AS `County`,
         `t`.`HUC12` AS `HUC12`,
         `t`.`HUC12_Cnty_State` AS `HUC12_Cnty_State`,
         `t`.`Cnty_St` AS `Cnty_St`
  from `ced_main_huc12_info` `p`,
    `ced_main_huc12_info_huc12_value` `s`,
    `ced_main_state_county_huc12_values` `t`
where `s`.`state_county_huc12_values_id` = `t`.`id`
and `s`.`huc12_info_id` = `p`.`id`;

CREATE OR REPLACE VIEW `qry_ced2ags_office` AS
  select `a`.`User_id` AS `User_id`,
         `a`.`User_Phone_Number` AS `User_Phone_Number`,
         `a`.`Agency` AS `Agency`,
         `a`.`Field_Office` AS `Field_Office`,
         `s1`.`id` AS `FO_ID`
  from `accounts_userprofile` `a`,
    `accounts_office_values` `s1`
  where `s1`.`office` = `a`.`Field_Office`
        and `a`.`User_Phone_Number` <> '';

CREATE OR REPLACE VIEW `qry_ced2ags_ownership` AS
  select `p`.`Project_ID` AS `Project_ID`,
         `t`.`Owners` AS `Owners`,
         `t`.`id` AS `O_ID`
  from `ced_main_ownership_info` `p`,
    `ced_main_ownership_info_owner_value` `s`,
    `ced_main_ownership_values` `t`
  where `p`.`id` = `s`.`ownership_info_id`
        and `s`.`ownership_values_id` = `t`.`id`;

CREATE OR REPLACE VIEW  `qry_ced2ags_population` AS
  select `p`.`Project_ID` AS `Project_ID`,
         `t`.`Populations` AS `Populations`,
         `t`.`Pop_Name` AS `Pop_Name`,
         `t`.`id` AS `Pop_ID`
  from `ced_main_population_info` `p`,`ced_main_population_info_population_value` `s`,
    `ced_main_population_values` `t`
  where `p`.`id` = `s`.`population_info_id`and `s`.`population_values_id` = `t`.`id`;

CREATE OR REPLACE VIEW `qry_ced2ags_project` AS
  select `p`.`Project_ID` AS `Project_ID`,
          `p`.`Project_Name` AS `Project_Name`,
          `p`.`Entry_Type` AS `Entry_Type`,
          `p`.`Shapefile` AS `Shapefile`,
          `p`.`Metadata` AS `Metadata`,
          `p`.`activity` AS `Activity`,
          `p`.`subactivity` AS `SubActivity`,
          `p`.`Objectives_Desc` AS `Objectives_Desc`,
          `p`.`Effects_Desc` AS `Effects_Desc`,
          left(`p`.`Implementing_Party`,30) AS `Implementing_Party`,
          `p`.`Office` AS `Office`,
          `p`.`Date_Created` AS `Date_Created`,
          `p`.`Project_Status` AS `Project_Status`,
          `p`.`Last_Updated` AS `Last_Updated`,
          `p`.`Approved` AS `Approved`,
          `p`.`Date_Approved` AS `Date_Approved`,
          `p`.`TypeAct` AS `TypeAct`,
          `p`.`PageLoc` AS `PageLoc`,
          `p`.`LCMItem` AS `LCMItem`,
          `p`.`LC_Zoom` AS `LC_Zoom`,
          `p`.`LC_Center_X` AS `LC_Center_X`,
          `p`.`LC_Center_Y` AS `LC_Center_Y`,
          `p`.`Notes` AS `Notes`,
          `p`.`Agreement_Length` AS `Agreement_Length`,
          `p`.`Agreement_Penalty` AS `Agreement_Penalty`,
          `p`.`Wobble_GIS` AS `Wobble_GIS`,
          `s1`.`Imp_Status` AS `Imp_Status`,
          `s1`.`Start_Date` AS `Start_Date`,
          `s1`.`Finish_Date` AS `Finish_Date`,
          `s1`.`In_Perpetuity` AS `In_Perpetuity`,
          `s1`.`Effective_Determined` AS `Effective_Determined`,
          `s1`.`Effective_Explained` AS `Effective_Explained`,
          `s1`.`Reas_Certain` AS `Reas_Certain`,
          `s1`.`Legal_Authority` AS `Legal_Authority`,
          `s1`.`Staff_Available` AS `Staff_Available`,
          `s1`.`Regulatory_Mech` AS `Regulatory_Mech`,
          `s1`.`Compliance` AS `Compliance`,
          `s1`.`Vol_Incentives` AS `Vol_Incentives`,
          `s1`.`Reduce_Threats` AS `Reduce_Threats`,
          `s1`.`Incremental_Objectives` AS `Incremental_Objectives`,
          `s1`.`Quantifiable_Measures` AS `Quantifiable_Measures`,
          `s1`.`AD_Strategy` AS `AD_Strategy`,
          `s1`.`Imp_and_Effect_Correct` AS `Imp_and_Effect_Correct`,
          `s1`.`Imp_and_Effect_Cor_Explan` AS `Imp_and_Effect_Cor_Explan`,
          `s1`.`Date_Entered` AS `Date_Entered_Imp_Info`,
          `s2`.`BreedingNestingAcres` AS `BreedingNestingAcres`,
          `s2`.`BroodRearingAcres` AS `BroodRearingAcres`,
          `s2`.`WinterAcres` AS `WinterAcres`,
          `s2`.`TotalAcres` AS `TotalAcres`,
          `s2`.`BreedingNestingMiles` AS `BreedingNestingMiles`,
          `s2`.`BroodRearingMiles` AS `BroodRearingMiles`,
          `s2`.`WinterMiles` AS `WinterMiles`,
          `s2`.`TotalMiles` AS `TotalMiles`,
          `s2`.`BreedingNestingNumberBirds` AS `BreedingNestingNumberBirds`,
          `s2`.`BroodRearingNumberBirds` AS `BroodRearingNumberBirds`,
          `s2`.`WinterNumberBirds` AS `WinterNumberBirds`,
          `s2`.`TotalNumberBirds` AS `TotalNumberBirds`,
          `s2`.`BreedingNestingNumberRemoved` AS `BreedingNestingNumberRemoved`,
          `s2`.`BroodRearingNumberRemoved` AS `BroodRearingNumberRemoved`,
          `s2`.`WinterNumberRemoved` AS `WinterNumberRemoved`,
          `s2`.`TotalNumberRemoved` AS `TotalNumberRemoved`,
          `s2`.`BreedingNestingNumberKilled` AS `BreedingNestingNumberKilled`,
          `s2`.`BroodRearingNumberKilled` AS `BroodRearingNumberKilled`,
          `s2`.`WinterNumberKilled` AS `WinterNumberKilled`,
          `s2`.`TotalNumberKilled` AS `TotalNumberKilled`,
          `s2`.`BreedingNestingEquids` AS `BreedingNestingEquids`,
          `s2`.`BroodRearingEquids` AS `BroodRearingEquids`,
          `s2`.`WinterEquids` AS `WinterEquids`,
          `s2`.`TotalEquids` AS `TotalEquids`,
          `s2`.`Date_Entered` AS `Date_Entered_Metrics`,
          `s3`.`id` AS `IP_ID`,
          `s4`.`id` AS `ACT_ID`,
          `s5`.`id` AS `SACT_ID`,
          `s6`.`id` AS `TA_ID`,
          `p`.`Wobbled_GIS` AS `Wobbled_GIS`,
          `p`.`Batch_Upload` AS `Batch_Upload`,
          `s7`.`id` AS `FO_ID`
   from `ced_main_project_info` `p`,
     `ced_main_implementation_info` `s1`,
     `ced_main_metrics` `s2`,
     `ced_main_imp_party_values` `s3`,
     `ced_main_activity` `s4`,
     `ced_main_subactivity` `s5`,
     `ced_main_typeact` `s6`,
     `accounts_office_values` `s7`
   where `s1`.`Project_ID` = `p`.`Project_ID`
         and `p`.`Project_ID` = `s2`.`Project_ID`
         and `p`.`Implementing_Party` = `s3`.`Implementation_Party`
         and `p`.`activity` = `s4`.`activity`
         and `p`.`subactivity` = `s5`.`subactivity`
         and `p`.`TypeAct` = `s6`.`typeact`
         and `p`.`Office` = `s7`.`office`
         and `p`.`Mark_For_Deletion` = 0;

CREATE OR REPLACE VIEW `qry_ced2ags_project2` AS
  select `p`.`Project_ID` AS `Project_ID`,
         `p`.`Project_Name` AS `Project_Name`,
         `p`.`Entry_Type` AS `Entry_Type`,
         `p`.`Shapefile` AS `Shapefile`,
         `p`.`Metadata` AS `Metadata`,
         `p`.`activity` AS `Activity`,
         `p`.`subactivity` AS `SubActivity`,
         `p`.`Objectives_Desc` AS `Objectives_Desc`,
         `p`.`Effects_Desc` AS `Effects_Desc`,
         `p`.`Implementing_Party` AS `Implementing_Party`,
         `p`.`Office` AS `Office`,
         `p`.`Date_Created` AS `Date_Created`,
         `p`.`Project_Status` AS `Project_Status`,
         `p`.`Last_Updated` AS `Last_Updated`,
         `p`.`Approved` AS `Approved`,
         `p`.`Date_Approved` AS `Date_Approved`,
         `p`.`TypeAct` AS `TypeAct`,
         `p`.`PageLoc` AS `PageLoc`,
         `p`.`LCMItem` AS `LCMItem`,
         `p`.`LC_Zoom` AS `LC_Zoom`,
         `p`.`LC_Center_X` AS `LC_Center_X`,
         `p`.`LC_Center_Y` AS `LC_Center_Y`,
         `p`.`Notes` AS `Notes`,
         `p`.`Agreement_Length` AS `Agreement_Length`,
         `p`.`Agreement_Penalty` AS `Agreement_Penalty`,
         `p`.`Wobble_GIS` AS `Wobble_GIS`,
         `s1`.`Imp_Status` AS `Imp_Status`,
         `s1`.`Start_Date` AS `Start_Date`,
         `s1`.`Finish_Date` AS `Finish_Date`,
         `s1`.`In_Perpetuity` AS `In_Perpetuity`,
         `s1`.`Effective_Determined` AS `Effective_Determined`,
         `s1`.`Effective_Explained` AS `Effective_Explained`,
         `s1`.`Reas_Certain` AS `Reas_Certain`,`s1`.`Legal_Authority` AS `Legal_Authority`,
         `s1`.`Staff_Available` AS `Staff_Available`,
         `s1`.`Regulatory_Mech` AS `Regulatory_Mech`,
         `s1`.`Compliance` AS `Compliance`,
         `s1`.`Vol_Incentives` AS `Vol_Incentives`,
         `s1`.`Reduce_Threats` AS `Reduce_Threats`,
         `s1`.`Incremental_Objectives` AS `Incremental_Objectives`,
         `s1`.`Quantifiable_Measures` AS `Quantifiable_Measures`,
         `s1`.`AD_Strategy` AS `AD_Strategy`,
         `s1`.`Imp_and_Effect_Correct` AS `Imp_and_Effect_Correct`,
         `s1`.`Imp_and_Effect_Cor_Explan` AS `Imp_and_Effect_Cor_Explan`,
         `s1`.`Date_Entered` AS `Date_Entered_Imp_Info`,
         `s2`.`BreedingNestingAcres` AS `BreedingNestingAcres`,
         `s2`.`BroodRearingAcres` AS `BroodRearingAcres`,
         `s2`.`WinterAcres` AS `WinterAcres`,
         `s2`.`TotalAcres` AS `TotalAcres`,
         `s2`.`BreedingNestingMiles` AS `BreedingNestingMiles`,
         `s2`.`BroodRearingMiles` AS `BroodRearingMiles`,
         `s2`.`WinterMiles` AS `WinterMiles`,
         `s2`.`TotalMiles` AS `TotalMiles`,
         `s2`.`BreedingNestingNumberBirds` AS `BreedingNestingNumberBirds`,
         `s2`.`BroodRearingNumberBirds` AS `BroodRearingNumberBirds`,
         `s2`.`WinterNumberBirds` AS `WinterNumberBirds`,
         `s2`.`TotalNumberBirds` AS `TotalNumberBirds`,
         `s2`.`BreedingNestingNumberRemoved` AS `BreedingNestingNumberRemoved`,
         `s2`.`BroodRearingNumberRemoved` AS `BroodRearingNumberRemoved`,
         `s2`.`WinterNumberRemoved` AS `WinterNumberRemoved`,
         `s2`.`TotalNumberRemoved` AS `TotalNumberRemoved`,
         `s2`.`BreedingNestingNumberKilled` AS `BreedingNestingNumberKilled`,
         `s2`.`BroodRearingNumberKilled` AS `BroodRearingNumberKilled`,
         `s2`.`WinterNumberKilled` AS `WinterNumberKilled`,
         `s2`.`TotalNumberKilled` AS `TotalNumberKilled`,
         `s2`.`BreedingNestingEquids` AS `BreedingNestingEquids`,
         `s2`.`BroodRearingEquids` AS `BroodRearingEquids`,
         `s2`.`WinterEquids` AS `WinterEquids`,
         `s2`.`TotalEquids` AS `TotalEquids`,
         `s2`.`Date_Entered` AS `Date_Entered_Metrics`,
         `s3`.`id` AS `IP_ID`,
         `s4`.`id` AS `ACT_ID`,
         `s5`.`id` AS `SACT_ID`,
         `s6`.`id` AS `TA_ID`
  from `ced_main_project_info` `p`,
    `ced_main_implementation_info` `s1`,
    `ced_main_metrics` `s2`,
  `ced_main_imp_party_values` `s3`,`ced_main_activity` `s4`, `ced_main_subactivity` `s5`,
  `ced_main_typeact` `s6`
where `s1`.`Project_ID` = `p`.`Project_ID`
and `p`.`Project_ID` = `s2`.`Project_ID`
and `p`.`Implementing_Party` = `s3`.`Implementation_Party`
and `p`.`activity` = `s4`.`activity`
and `p`.`subactivity` = `s5`.`subactivity`
and `p`.`TypeAct` = `s6`.`typeact`
and `p`.`Mark_For_Deletion` = 0;

CREATE OR REPLACE VIEW `qry_ced2ags_state` AS
  select `p`.`Project_ID` AS `Project_ID`,
         `t`.`State` AS `State`,
         `t`.`id` AS `ST_ID`
  from `ced_main_state_info_state_value` `s`,
    `ced_main_state_info` `p`,
    `ced_main_state` `t`
  where `s`.`state_info_id` = `p`.`id`
        and `s`.`state_id` = `t`.`id`;

CREATE OR REPLACE VIEW `qry_ced2ags_threats` AS
  select `p`.`Project_ID` AS `Project_ID`,
         `t`.`Threats` AS `Threats`,
         `t`.`id` AS `T_ID`
  from `ced_main_threats_threat` `s`,
  `ced_main_threats` `p`,
  `ced_main_threat_values` `t`
where `s`.`threats_id` = `p`.`id`
and `s`.`threat_values_id` = `t`.`id`;

CREATE OR REPLACE VIEW `qry_ced2ags_wafwa` AS
  select `p`.`Project_ID` AS `Project_ID`,
         `t`.`WAFWA_Zone` AS `WAFWA_Zone`,
         `t`.`id` AS `WAFWA_ID`
  from `ced_main_wafwa_info` `p`,
    `ced_main_wafwa_info_wafwa_value` `s`,
    `ced_main_wafwa_zone_values` `t`
  where `p`.`id` = `s`.`wafwa_info_id`
        and `s`.`wafwa_zone_values_id` = `t`.`id`;
