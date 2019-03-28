SET FOREIGN_KEY_CHECKS=0;

insert into ced_main_state (id, state, statename) values
(9827,'NM','New Mexico'),
(20000,'SK','Saskatchewan');

alter table ced_main_project_info add COLUMN Start_Date date;
alter table ced_main_project_info add COLUMN End_Date date;
alter table ced_main_project_info add COLUMN Oil_Gas_Explain longtext;
alter table ced_main_project_info add COLUMN Feral_Equids_Explain longtext;
alter table ced_main_project_info add COLUMN Infrastructure_Explain longtext;
alter table ced_main_project_info add COLUMN Mining_Explain longtext;
alter table ced_main_project_info add COLUMN Recreation_Explain longtext;
alter table ced_main_project_info add COLUMN Urban_Devel_Explain longtext;
alter table ced_main_project_info add COLUMN Fire_Explain longtext;
alter table ced_main_project_info add COLUMN Improper_Grazing_Explain longtext;
alter table ced_main_project_info add COLUMN Isolated_Explain longtext;
alter table ced_main_project_info add COLUMN Invasives_Explained longtext;
alter table ced_main_project_info add COLUMN Sagebrush_Loss_Explain longtext;
alter table ced_main_project_info add COLUMN GIS_Acres double;
alter table ced_main_project_info add COLUMN Conifer_Encroach_Explain longtext;
alter table ced_main_project_info add COLUMN Ag_Conversion_Explain longtext;

delete from ced_main_typeact;
insert into ced_main_typeact (id, typeact) values
(1,'---Select an Effort Type---'),
(2,'Non-Spatial Plan'),
(3,'Non-Spatial Project'), 
(4,'Spatial Project');

delete from ced_main_activity;
insert into ced_main_activity (id,activity,typeact) values
(1,'---Select an Activity---','Null'),
(2,'NON-REGULATORY CONSERVATION PLANS (Strategies, BMPs)','Non-Spatial Plan'),
(3,'REGULATORY MECHANISMS: Plans, Policies','Non-Spatial Plan'),
(4,'SAGEBRUSH PROTECTION','Both Project'),
(5,'RESTORATION: Infrastructure Removal and Modification','Non-Spatial Project'),
(6,'RESTORATION: Livestock & Rangeland Management','Both Project'),
(7,'RESTORATION: Travel Management','Non-Spatial Project'),
(8,'RESTORATION: Population Augmentation','Non-Spatial Project'),
(9,'RESTORATION: Wild Equid Management','Non-Spatial Project'),
(10,'RESTORATION: Non-Fire Related: Habitat Improvement / Restoration','Spatial Project'),
(11,'RESTORATION: Fire-Related: Habitat Restoration and/or Pre-Supression Efforts','Spatial Project'),
(12,'RESTORATION: Habitat Restoration (Fire)','Spatial Project'),
(13,'RESTORATION: Conifer Removal','Spatial Project');

delete from ced_main_subactivity;
insert into ced_main_subactivity (id,SubActivity,Activity,TypeAct) values
(1,'---Select an Activity---','Null','Null'),
(2,'---Select a Subactivity---','Null','Null'),
(3,'Federal Land Use Plan','REGULATORY MECHANISMS: Plans, Policies','Non-Spatial Plan'),
(4,'State Conservation Plan','REGULATORY MECHANISMS: Plans, Policies','Non-Spatial Plan'),
(5,'County/Local Government Plan','REGULATORY MECHANISMS: Plans, Policies','Non-Spatial Plan'),
(6,'Programmatic Candidate Conservation Agreement','REGULATORY MECHANISMS: Plans, Policies','Non-Spatial Plan'),
(7,'Programmatic Candidate Conservation Agreement with Assurances','REGULATORY MECHANISMS: Plans, Policies','Non-Spatial Plan'),
(8,'Grazing and Rangeland Management Plans (Regulatory)','REGULATORY MECHANISMS: Plans, Policies','Non-Spatial Plan'),
(9,'Wild horse and burro control/removal strategy','REGULATORY MECHANISMS: Plans, Policies','Non-Spatial Plan'),
(10,'Compensatory Mitigation Plans','REGULATORY MECHANISMS: Plans, Policies','Non-Spatial Plan'),
(11,'Conservation Banking / Advanced Crediting Systems','REGULATORY MECHANISMS: Plans, Policies','Non-Spatial Plan'),
(12,'Reclamation Plan','REGULATORY MECHANISMS: Plans, Policies','Non-Spatial Plan'),
(13,'Fire Related Conservation Strategy (Pre-suppression Plans)','REGULATORY MECHANISMS: Plans, Policies','Non-Spatial Plan'),
(14,'Fire Mutual Aid Agreement','REGULATORY MECHANISMS: Plans, Policies','Non-Spatial Plan'),
(15,'Sage-grouse Harvest Regulation','REGULATORY MECHANISMS: Plans, Policies','Non-Spatial Plan'),
(16,'Zoning Regulation (Urban and Agriculture)','REGULATORY MECHANISMS: Plans, Policies','Non-Spatial Plan'),
(17,'Non-regulatory Conservation Strategies','NON-REGULATORY CONSERVATION PLANS (Strategies, BMPs)','Non-Spatial Plan'),
(18,'Minimization and Avoidance Strategies / BMPs','NON-REGULATORY CONSERVATION PLANS (Strategies, BMPs)','Non-Spatial Plan'),
(19,'Grazing and Rangeland Management Plans (Non-Regulatory)','NON-REGULATORY CONSERVATION PLANS (Strategies, BMPs)','Non-Spatial Plan'),
(20,'Grazing Management Practices and Avoidance','NON-REGULATORY CONSERVATION PLANS (Strategies, BMPs)','Non-Spatial Plan'),
(21,'Conservation Agreements (includes CCAs, CCAAs, Farm Bill and other Incentive-based programs)','SAGEBRUSH PROTECTION','Non-Spatial Project'),
(22,'Conservation Easement','SAGEBRUSH PROTECTION','Spatial Project'),
(23,'Land Acquisition','SAGEBRUSH PROTECTION','Spatial Project'),
(24,'Structure Removal','RESTORATION: Infrastructure Removal and Modification','Non-Spatial Project'),
(25,'Powerline Burial','RESTORATION: Infrastructure Removal and Modification','Non-Spatial Project'),
(26,'Powerline Retrofitting / Modification','RESTORATION: Infrastructure Removal and Modification','Non-Spatial Project'),
(27,'Fence Modification','RESTORATION: Infrastructure Removal and Modification','Non-Spatial Project'),
(28,'Fence Marking','RESTORATION: Infrastructure Removal and Modification','Non-Spatial Project'),
(29,'Fence Removal','RESTORATION: Infrastructure Removal and Modification','Non-Spatial Project'),
(30,'Improved Grazing Practices (Rest, Rotation, Etc.)','RESTORATION: Livestock & Rangeland Management','Non-Spatial Project'),
(31,'Improved Grazing Practices (Rest, Rotation, Etc.) (Spatial)','RESTORATION: Livestock & Rangeland Management','Spatial Project'),
(32,'Road and Trail closure','RESTORATION: Travel Management','Non-Spatial Project'),
(33,'Rerouted Roads and/or Trails','RESTORATION: Travel Management','Non-Spatial Project'),
(34,'Translocation','RESTORATION: Population Augmentation','Non-Spatial Project'),
(35,'Wild Equid Population Control','RESTORATION: Wild Equid Management','Non-Spatial Project'),
(36,'Wild Equid Gather','RESTORATION: Wild Equid Management','Non-Spatial Project'),
(37,'Area Closure (Area and/or Seasonal)','RESTORATION: Non-Fire Related: Habitat Improvement / Restoration','Spatial Project'),
(38,'Vegetation Management / Habitat Enhancement','RESTORATION: Non-Fire Related: Habitat Improvement / Restoration','Spatial Project'),
(39,'Annual Grass (Cheatgrass) Treatments','RESTORATION: Non-Fire Related: Habitat Improvement / Restoration','Spatial Project'),
(40,'Non-fire restroration (only native seedings, plantings)','RESTORATION: Non-Fire Related: Habitat Improvement / Restoration','Spatial Project'),
(41,'Non-fire restroration (only non-native seedings, plantings)','RESTORATION: Non-Fire Related: Habitat Improvement / Restoration','Spatial Project'),
(42,'Non-fire restoration (native/non-native seeding mixes, plantings)','RESTORATION: Non-Fire Related: Habitat Improvement / Restoration','Spatial Project'),
(43,'Fuels Management / Cheatgrass Treatments','RESTORATION: Fire-Related: Habitat Restoration and/or Pre-Supression Efforts','Spatial Project'),
(44,'Fire Breaks (Spatial)','RESTORATION: Fire-Related: Habitat Restoration and/or Pre-Supression Efforts','Spatial Project'),
(45,'Post-fire restoration (only native seeding, plantings)','RESTORATION: Habitat Restoration (Fire)','Spatial Project'),
(46,'Post-fire restoration (only non-native seeding, plantings)','RESTORATION: Habitat Restoration (Fire)','Spatial Project'),
(47,'Post-fire restoration (native/non-native seeding mix)','RESTORATION: Habitat Restoration (Fire)','Spatial Project'),
(48,'Conifer Removal (all phases)','RESTORATION: Conifer Removal','Spatial Project');


delete from ced_main_metric;
insert into ced_main_metric (id, metric, text) values
(1,'Acres','Acres'),
(2,'Miles','Miles');

drop table if exists ced_main_threat_values;
create table ced_main_threat_values (id int(11), Threats varchar(75), TypeAct varchar(20));
insert into ced_main_threat_values (id, Threats, TypeAct) values
(1,'AGRICULTURAL CONVERSION (Tillage Risk)','Spatial'),
(2,'CONIFER ENCROACHMENT','Spatial'),
(3,'OIL & GAS DEVELOPMENT','All'),
(4,'FIRE','All'),
(5,'FERAL EQUIDS','Non-Spatial'),
(6,'IMPROPER GRAZING / RANGE MANAGEMENT','Non-Spatial'),
(7,'INFRASTRUCTURE (Roads, Powerlines, Renewable Energy)','Non-Spatial'),
(8,'ISOLATED / SMALL POPULATION SIZE','Non-Spatial'),
(9,'MINING','Non-Spatial'),
(10,'INVASIVES (Annual Grasses and Noxious Weeds)','All'),
(11,'RECREATION','Non-Spatial'),
(12,'SAGEBRUSH LOSS or DEGRADATION','All'),
(13,'URBAN DEVELOPMENT','Non-Spatial');

SET FOREIGN_KEY_CHECKS=1;
