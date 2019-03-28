DELIMITER $$

CREATE OR REPLACE VIEW `qry_ced2ags_project` AS
SELECT
  `p`.`Project_ID`                 AS `Project_ID`,
  `p`.`Project_Name`               AS `Project_Name`,
  `p`.`Entry_Type`                 AS `Entry_Type`,
  `p`.`Shapefile`                  AS `Shapefile`,
  `p`.`Metadata`                   AS `Metadata`,
  `p`.`activity`                   AS `Activity`,
  LEFT(`p`.`subactivity`,100)      AS `SubActivity`,
  `p`.`Objectives_Desc`            AS `Objectives_Desc`,
  `p`.`Effects_Desc`               AS `Effects_Desc`,
  LEFT(`p`.`Implementing_Party`,30) AS `Implementing_Party`,
  `p`.`Office`                     AS `Office`,
  `p`.`Date_Created`               AS `Date_Created`,
  `p`.`Project_Status`             AS `Project_Status`,
  `p`.`Last_Updated`               AS `Last_Updated`,
  `p`.`Approved`                   AS `Approved`,
  `p`.`Date_Approved`              AS `Date_Approved`,
  `p`.`TypeAct`                    AS `TypeAct`,
  `p`.`PageLoc`                    AS `PageLoc`,
  `p`.`LCMItem`                    AS `LCMItem`,
  `p`.`LC_Zoom`                    AS `LC_Zoom`,
  `p`.`LC_Center_X`                AS `LC_Center_X`,
  `p`.`LC_Center_Y`                AS `LC_Center_Y`,
  `p`.`Notes`                      AS `Notes`,
  `p`.`Agreement_Length`           AS `Agreement_Length`,
  `p`.`Agreement_Penalty`          AS `Agreement_Penalty`,
  `p`.`Wobble_GIS`                 AS `Wobble_GIS`,
  `s1`.`Imp_Status`                AS `Imp_Status`,
  `s1`.`Start_Date`                AS `Start_Date`,
  `s1`.`Finish_Date`               AS `Finish_Date`,
  `s1`.`In_Perpetuity`             AS `In_Perpetuity`,
  `s1`.`Effective_Determined`      AS `Effective_Determined`,
  `s1`.`Effective_Explained`       AS `Effective_Explained`,
  `s1`.`Reas_Certain`              AS `Reas_Certain`,
  `s1`.`Legal_Authority`           AS `Legal_Authority`,
  `s1`.`Staff_Available`           AS `Staff_Available`,
  `s1`.`Regulatory_Mech`           AS `Regulatory_Mech`,
  `s1`.`Compliance`                AS `Compliance`,
  `s1`.`Vol_Incentives`            AS `Vol_Incentives`,
  `s1`.`Reduce_Threats`            AS `Reduce_Threats`,
  `s1`.`Incremental_Objectives`    AS `Incremental_Objectives`,
  `s1`.`Quantifiable_Measures`     AS `Quantifiable_Measures`,
  `s1`.`AD_Strategy`               AS `AD_Strategy`,
  `s1`.`Imp_and_Effect_Correct`    AS `Imp_and_Effect_Correct`,
  `s1`.`Imp_and_Effect_Cor_Explan` AS `Imp_and_Effect_Cor_Explan`,
  `s1`.`Date_Entered`              AS `Date_Entered_Imp_Info`,
  `s2`.`TotalAcres`                AS `TotalAcres`,
  `s2`.`TotalMiles`                AS `TotalMiles`,
  `s2`.`Date_Entered`              AS `Date_Entered_Metrics`,
  `s3`.`id`                        AS `IP_ID`,
  `s4`.`id`                        AS `ACT_ID`,
  `s5`.`id`                        AS `SACT_ID`,
  `s6`.`id`                        AS `TA_ID`,
  `p`.`Wobbled_GIS`                AS `Wobbled_GIS`,
  `p`.`Batch_Upload`               AS `Batch_Upload`,
  `s7`.`id`                        AS `FO_ID`
FROM (((((((`ced_main_project_info` `p`
         LEFT JOIN `ced_main_implementation_info` `s1`
           ON ((`s1`.`Project_ID` = `p`.`Project_ID`)))
        LEFT JOIN `ced_main_metrics_view` `s2`
          ON ((`p`.`Project_ID` = `s2`.`Project_ID`)))
       LEFT JOIN `ced_main_imp_party_values` `s3`
         ON ((`p`.`Implementing_Party` = `s3`.`Implementation_Party`)))
      LEFT JOIN `activity_lut` `s4`
        ON ((`p`.`activity` = `s4`.`activity`)))
     LEFT JOIN `subactivity_lut` `s5`
       ON ((`p`.`subactivity` = `s5`.`subactivity`)))
    LEFT JOIN `typeact_lut` `s6`
      ON ((`p`.`TypeAct` = `s6`.`typeact`)))
   LEFT JOIN `accounts_office_values` `s7`
     ON ((`p`.`Office` = `s7`.`office`)))
WHERE (`p`.`Mark_For_Deletion` = 0)$$

DELIMITER ;

quit