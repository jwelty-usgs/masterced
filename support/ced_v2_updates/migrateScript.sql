BEGIN;
--
-- Create model batchupload
--
CREATE TABLE `ced_main_batchupload`
(`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
`FolderName` varchar(200) NOT NULL,
`FileName` varchar(200) NOT NULL,
`LCMItem` varchar(50) NOT NULL,
`UploadStatus` varchar(20) NOT NULL,
`Upload_Date` datetime(6) NOT NULL,
`Uploading_User` varchar(50) NOT NULL);
--
-- Create model batchupload_groups
--
CREATE TABLE `ced_main_batchupload_groups`
(`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
`Batch_Group_ID` integer NOT NULL,
`BatchUpload_ID` integer NOT NULL,
`Group_Designation` varchar(100) NOT NULL,
`Effort_ID_List` varchar(100) NOT NULL,
`Type_Act` varchar(30) NOT NULL,
`Group_Status` varchar(100) NOT NULL,
`Upload_Date` datetime(6) NOT NULL,
`Uploading_User` varchar(50) NOT NULL);
--
-- Keys
--
ALTER TABLE `ced_main_state_info`
ADD CONSTRAINT `ced_main_state_info_Project_ID_4431e358_fk_ced_main_`
FOREIGN KEY (`Project_ID`)
REFERENCES `ced_main_project_info` (`Project_ID`);

ALTER TABLE `ced_main_state_info_State_Value`
ADD CONSTRAINT `ced_main_state_info__state_info_id_54180216_fk_ced_main_`
FOREIGN KEY (`state_info_id`)
REFERENCES `ced_main_state_info` (`id`);

ALTER TABLE `ced_main_state_info_State_Value`
ADD CONSTRAINT `ced_main_state_info__state_id_a71c6f63_fk_ced_main_`
FOREIGN KEY (`state_id`)
REFERENCES `ced_main_state` (`id`);

ALTER TABLE `ced_main_state_info_State_Value`
ADD CONSTRAINT `ced_main_state_info_Stat_state_info_id_state_id_57617fea_uniq`
UNIQUE (`state_info_id`, `state_id`);

ALTER TABLE `ced_main_threats`
ADD CONSTRAINT `ced_main_threats_Project_ID_7e989311_fk_ced_main_`
FOREIGN KEY (`Project_ID`)
REFERENCES `ced_main_project_info` (`Project_ID`);

alter table ced_main_threat_values add primary key(id);

ALTER TABLE `ced_main_threats_Threat`
ADD CONSTRAINT `ced_main_threats_Thr_threat_values_id_9f1b6072_fk_ced_main_`
FOREIGN KEY (`threat_values_id`)
REFERENCES `ced_main_threat_values` (`id`);

ALTER TABLE `ced_main_threats_Threat`
ADD CONSTRAINT `ced_main_threats_Threat_threats_id_threat_values_f4036197_uniq`
UNIQUE (`threats_id`, `threat_values_id`);

ALTER TABLE `ced_main_wafwa_info`
ADD CONSTRAINT `ced_main_wafwa_info_Project_ID_af8e3b05_fk_ced_main_`
FOREIGN KEY (`Project_ID`)
REFERENCES `ced_main_project_info` (`Project_ID`);

ALTER TABLE `ced_main_wafwa_info_WAFWA_Value`
ADD CONSTRAINT `ced_main_wafwa_info__wafwa_info_id_77cd5c1e_fk_ced_main_`
FOREIGN KEY (`wafwa_info_id`)
REFERENCES `ced_main_wafwa_info` (`id`);

ALTER TABLE `ced_main_wafwa_info_WAFWA_Value`
ADD CONSTRAINT `ced_main_wafwa_info__wafwa_zone_values_id_cd4a45d6_fk_ced_main_`
FOREIGN KEY (`wafwa_zone_values_id`)
REFERENCES `ced_main_wafwa_zone_values` (`id`);

ALTER TABLE `ced_main_wafwa_info_WAFWA_Value`
ADD CONSTRAINT `ced_main_wafwa_info_WAFW_wafwa_info_id_wafwa_zone_9ce9940e_uniq`
UNIQUE (`wafwa_info_id`, `wafwa_zone_values_id`);

ALTER TABLE `ced_main_population_info_Population_Value`
ADD CONSTRAINT `ced_main_population__population_info_id_2b818e3e_fk_ced_main_`
FOREIGN KEY (`population_info_id`)
REFERENCES `ced_main_population_info` (`id`);

ALTER TABLE `ced_main_population_info_Population_Value`
ADD CONSTRAINT `ced_main_population__population_values_id_e475ee91_fk_ced_main_`
FOREIGN KEY (`population_values_id`)
REFERENCES `ced_main_population_values` (`id`);

ALTER TABLE `ced_main_population_info_Population_Value`
ADD CONSTRAINT `ced_main_population_info_population_info_id_popul_424554c9_uniq`
UNIQUE (`population_info_id`, `population_values_id`);

ALTER TABLE `ced_main_population_info`
ADD CONSTRAINT `ced_main_population__Project_ID_f943e661_fk_ced_main_`
FOREIGN KEY (`Project_ID`)
REFERENCES `ced_main_project_info` (`Project_ID`);

ALTER TABLE `ced_main_ownership_info_Owner_Value`
ADD CONSTRAINT `ced_main_ownership_i_ownership_info_id_30d11495_fk_ced_main_`
FOREIGN KEY (`ownership_info_id`)
REFERENCES `ced_main_ownership_info` (`id`);

ALTER TABLE `ced_main_ownership_info_Owner_Value`
ADD CONSTRAINT `ced_main_ownership_i_ownership_values_id_006c5149_fk_ced_main_`
FOREIGN KEY (`ownership_values_id`)
REFERENCES `ced_main_ownership_values` (`id`);

ALTER TABLE `ced_main_ownership_info_Owner_Value`
ADD CONSTRAINT `ced_main_ownership_info__ownership_info_id_owners_1ee823c4_uniq`
UNIQUE (`ownership_info_id`, `ownership_values_id`);

ALTER TABLE `ced_main_ownership_info`
ADD CONSTRAINT `ced_main_ownership_i_Project_ID_44dac255_fk_ced_main_`
FOREIGN KEY (`Project_ID`)
REFERENCES `ced_main_project_info` (`Project_ID`);

ALTER TABLE `ced_main_location_info`
ADD CONSTRAINT `ced_main_location_in_Project_ID_31316d5c_fk_ced_main_`
FOREIGN KEY (`Project_ID`)
REFERENCES `ced_main_project_info` (`Project_ID`);

ALTER TABLE `ced_main_huc12_info_HUC12_Value`
ADD CONSTRAINT `ced_main_huc12_info__huc12_info_id_3512ee7d_fk_ced_main_`
FOREIGN KEY (`huc12_info_id`)
REFERENCES `ced_main_huc12_info` (`id`);

ALTER TABLE `ced_main_huc12_info_HUC12_Value`
ADD CONSTRAINT `ced_main_huc12_info__state_county_huc12_v_0684ae9b_fk_ced_main_`
FOREIGN KEY (`state_county_huc12_values_id`)
REFERENCES `ced_main_state_county_huc12_values` (`id`);

ALTER TABLE `ced_main_huc12_info_HUC12_Value`
ADD CONSTRAINT `ced_main_huc12_info_HUC1_huc12_info_id_state_coun_5e9da7a3_uniq`
UNIQUE (`huc12_info_id`, `state_county_huc12_values_id`);

ALTER TABLE `ced_main_huc12_info`
ADD CONSTRAINT `ced_main_huc12_info_Project_ID_c06c091b_fk_ced_main_`
FOREIGN KEY (`Project_ID`)
REFERENCES `ced_main_project_info` (`Project_ID`);

ALTER TABLE `ced_main_county_info_County_Value`
ADD CONSTRAINT `ced_main_county_info_county_info_id_850aa8f8_fk_ced_main_`
FOREIGN KEY (`county_info_id`)
REFERENCES `ced_main_county_info` (`id`);

ALTER TABLE `ced_main_county_info_County_Value`
ADD CONSTRAINT `ced_main_county_info_state_county_id_33679d9d_fk_ced_main_`
FOREIGN KEY (`state_county_id`)
REFERENCES `ced_main_state_county` (`id`);

ALTER TABLE `ced_main_county_info_County_Value`
ADD CONSTRAINT `ced_main_county_info_Cou_county_info_id_state_cou_42ed07c0_uniq`
UNIQUE (`county_info_id`, `state_county_id`);

ALTER TABLE `ced_main_county_info`
ADD CONSTRAINT `ced_main_county_info_Project_ID_68d9dfdc_fk_ced_main_`
FOREIGN KEY (`Project_ID`)
REFERENCES `ced_main_project_info` (`Project_ID`);

ALTER TABLE `ced_main_collab_party_Collab_Party`
ADD CONSTRAINT `ced_main_collab_part_collab_party_id_35376a16_fk_ced_main_`
FOREIGN KEY (`collab_party_id`)
REFERENCES `ced_main_collab_party` (`id`);

ALTER TABLE `ced_main_collab_party_Collab_Party`
ADD CONSTRAINT `ced_main_collab_part_imp_party_values_id_e3604a87_fk_ced_main_`
FOREIGN KEY (`imp_party_values_id`)
REFERENCES `ced_main_imp_party_values` (`id`);

ALTER TABLE `ced_main_collab_party_Collab_Party`
ADD CONSTRAINT `ced_main_collab_party_Co_collab_party_id_imp_part_9727ef77_uniq`
UNIQUE (`collab_party_id`, `imp_party_values_id`);
ALTER TABLE `ced_main_collab_party`

ADD CONSTRAINT `ced_main_collab_part_Project_ID_e694bdba_fk_ced_main_`
FOREIGN KEY (`Project_ID`)
REFERENCES `ced_main_project_info` (`Project_ID`);

--
-- Create model subactivity_objectives
--
CREATE TABLE `ced_main_subactivity_objectives`
(`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
`Date_Entered` datetime(6) NOT NULL,
`User` varchar(50) NOT NULL);

CREATE TABLE `ced_main_subactivity_objectives_Objective`
(`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
`subactivity_objectives_id` integer NOT NULL,
`subactivity_objectives_data_id` integer NOT NULL);

ALTER TABLE `ced_main_subactivity_objectives`
ADD COLUMN `Project_ID` integer NOT NULL;

ALTER TABLE `ced_main_subactivity_objectives_Objective`
ADD CONSTRAINT `ced_main_subactivity_subactivity_objectiv_37d161c2_fk_ced_main_`
FOREIGN KEY (`subactivity_objectives_id`)
REFERENCES `ced_main_subactivity_objectives` (`id`);

ALTER TABLE `ced_main_subactivity_objectives_Objective`
ADD CONSTRAINT `ced_main_subactivity_subactivity_objectiv_9018a30f_fk_ced_main_`
FOREIGN KEY (`subactivity_objectives_data_id`)
REFERENCES `subactivity_objectives_data_lut` (`id`);

ALTER TABLE `ced_main_subactivity_objectives_Objective`
ADD CONSTRAINT `ced_main_subactivity_obj_subactivity_objectives_i_62ca2520_uniq`
UNIQUE (`subactivity_objectives_id`, `subactivity_objectives_data_id`);

ALTER TABLE `ced_main_subactivity_objectives`
ADD CONSTRAINT `ced_main_subactivity_Project_ID_ca96c3e0_fk_ced_main_`
FOREIGN KEY (`Project_ID`)
REFERENCES `ced_main_project_info` (`Project_ID`);

--
-- Create model subactivity_effective_state
--
CREATE TABLE `ced_main_subactivity_effective_state`
(`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
`Date_Entered` datetime(6) NOT NULL,
`User` varchar(50) NOT NULL);

CREATE TABLE `ced_main_subactivity_effective_state_Effectiveness_Statement`
(`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
`subactivity_effective_state_id` integer NOT NULL,
`subactivity_effective_state_data_id` integer NOT NULL);
--
-- Create model subactivity_methods
--
CREATE TABLE `ced_main_subactivity_methods`
(`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
`Date_Entered` datetime(6) NOT NULL,
`User` varchar(50) NOT NULL);

CREATE TABLE `ced_main_subactivity_methods_Method`
(`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
`subactivity_methods_id` integer NOT NULL,
`subactivity_methods_data_id` integer NOT NULL);
--
-- Add field Project_ID to subactivity_methods
--
ALTER TABLE `ced_main_subactivity_methods`
ADD COLUMN `Project_ID` integer NOT NULL;
--
-- Add field Project_ID to subactivity_effective_state
--
ALTER TABLE `ced_main_subactivity_effective_state`
ADD COLUMN `Project_ID` integer NOT NULL;

ALTER TABLE `ced_main_subactivity_effective_state_Effectiveness_Statement`
ADD CONSTRAINT `ced_main_subactivity_subactivity_effectiv_5c70dc4a_fk_ced_main_`
FOREIGN KEY (`subactivity_effective_state_id`)
REFERENCES `ced_main_subactivity_effective_state` (`id`);

ALTER TABLE `ced_main_subactivity_effective_state_Effectiveness_Statement`
ADD CONSTRAINT `ced_main_subactivity_subactivity_effectiv_84fcaa3c_fk_ced_main_`
FOREIGN KEY (`subactivity_effective_state_data_id`)
REFERENCES `subactivity_effective_state_data_lut` (`id`);

ALTER TABLE `ced_main_subactivity_effective_state_Effectiveness_Statement`
ADD CONSTRAINT `ced_main_subactivity_eff_subactivity_effectivenes_b6b99686_uniq`
UNIQUE (`subactivity_effective_state_id`, `subactivity_effective_state_data_id`);

ALTER TABLE `ced_main_subactivity_methods_method`
ADD CONSTRAINT `ced_main_subactivity_subactivity_methods__6f65b24b_fk_ced_main_`
FOREIGN KEY (`subactivity_methods_id`)
REFERENCES `ced_main_subactivity_methods` (`id`);

ALTER TABLE `ced_main_subactivity_methods_method`
ADD CONSTRAINT `ced_main_subactivity_subactivity_methods__822a4e11_fk_ced_main_`
FOREIGN KEY (`subactivity_methods_data_id`)
REFERENCES `subactivity_methods_data_lut` (`id`);

ALTER TABLE `ced_main_subactivity_methods_method`
ADD CONSTRAINT `ced_main_subactivity_met_subactivity_methods_id_s_8b294d35_uniq`
UNIQUE (`subactivity_methods_id`, `subactivity_methods_data_id`);

ALTER TABLE `ced_main_subactivity_methods`
ADD CONSTRAINT `ced_main_subactivity_Project_ID_695a15b6_fk_ced_main_`
FOREIGN KEY (`Project_ID`)
REFERENCES `ced_main_project_info` (`Project_ID`);

ALTER TABLE `ced_main_subactivity_effective_state`
ADD CONSTRAINT `ced_main_subactivity_Project_ID_5f19f2d6_fk_ced_main_`
FOREIGN KEY (`Project_ID`)
REFERENCES `ced_main_project_info` (`Project_ID`);

--
-- Add field Methods_Explained to implementation_info
--
ALTER TABLE `ced_main_implementation_info`
ADD COLUMN `Methods_Explained`
longtext;

COMMIT;
