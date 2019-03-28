-- noinspection SqlDialectInspectionForFile

create table typeact_lut (
id integer,
typeact varchar(60),
primary key(id)
);

insert into typeact_lut values(1,'---Select an Effort Type---');
insert into typeact_lut values(2,'Non-Spatial Plan');
insert into typeact_lut values(3,'Non-Spatial Project');
insert into typeact_lut values(4,'Spatial Project');

alter table ced_main_typeact rename to ced_main_typeact_legacy;

create or replace view ced_main_typeact AS
select distinct id, typeact from typeact_lut;

create table activity_lut (
id integer,
activity varchar(200),
typeact_id integer,
primary key(id),
foreign key (typeact_id) references typeact_lut (id)
);

insert into activity_lut values(1,'--Select an Activity--',1);
insert into activity_lut values(2,'NON-REGULATORY MECHANISMS: (Plans, Strategies, BMPs)',2);
insert into activity_lut values(3,'REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders)',2);
insert into activity_lut values(4,'RESTORATION: Infrastructure Removal and Modification',3);
insert into activity_lut values(5,'RESTORATION: Livestock & Rangeland Management',3);
insert into activity_lut values(6,'RESTORATION: Population Augmentation',3);
insert into activity_lut values(7,'RESTORATION: Travel Management',3);
insert into activity_lut values(8,'RESTORATION: Wild Equid Management',3);
insert into activity_lut values(9,'RESTORATION: Conifer Removal',4);
insert into activity_lut values(10,'RESTORATION: Post-Disturbance and/or Habitat Enhancement',4);
insert into activity_lut values(11,'SAGEBRUSH PROTECTION',4);

alter table ced_main_activity rename to ced_main_activity_legacy;

create or replace view ced_main_activity AS
select distinct a.id, a. activity, b.typeact
from activity_lut a, typeact_lut b
where a.typeact_id=b.id;

create table subactivity_lut (
id integer,
subactivity varchar(200),
activity_id integer,
primary key(id),
foreign key (activity_id) references activity_lut (id)
);

insert into subactivity_lut values(1,'--Select a SubActivity--',1);
insert into subactivity_lut values(2,'--Select an Activity--',1);
insert into subactivity_lut values(3,'Minimization  and Avoidance Strategies / BMPs',2);
insert into subactivity_lut values(4,'Non-regulatory Conservation Strategies',2);
insert into subactivity_lut values(5,'Compensatory Mitigation Plans',3);
insert into subactivity_lut values(6,'Conservation Agreements (including but not limited to: CCAs, CCAAs, Farm Bill and other Incentive-based programs)',3);
insert into subactivity_lut values(7,'Conservation Banking / Advanced Crediting Systems',3);
insert into subactivity_lut values(8,'County/Local Government Plan',3);
insert into subactivity_lut values(9,'Federal Land Use Plan',3);
insert into subactivity_lut values(10,'Fire Mutual Aid Agreement',3);
insert into subactivity_lut values(11,'Fire Related Conservation Strategy (Pre-suppression Plans)',3);
insert into subactivity_lut values(12,'Grazing and Rangeland Management Plans (Regulatory)',3);
insert into subactivity_lut values(13,'Programmatic Candidate Conservation Agreement',3);
insert into subactivity_lut values(14,'Programmatic Candidate Conservation Agreement with Assurances',3);
insert into subactivity_lut values(15,'Reclamation Plan',3);
insert into subactivity_lut values(16,'State Conservation Plan',3);
insert into subactivity_lut values(18,'Fence Marking',4);
insert into subactivity_lut values(19,'Fence Modification',4);
insert into subactivity_lut values(20,'Fence Removal',4);
insert into subactivity_lut values(21,'Powerline Burial',4);
insert into subactivity_lut values(22,'Powerline Retrofitting / Modification',4);
insert into subactivity_lut values(23,'Structure Removal',4);
insert into subactivity_lut values(24,'Improved Grazing Practices (Rest, Rotation, Etc.)',5);
insert into subactivity_lut values(25,'Translocation',6);
insert into subactivity_lut values(26,'Rerouted Roads and/or Trails',7);
insert into subactivity_lut values(27,'Road and Trail closure',7);
insert into subactivity_lut values(28,'Wild Equid Gather',8);
insert into subactivity_lut values(29,'Wild Equid Population Control',8);
insert into subactivity_lut values(17,'Conifer Removal (All Phases)',9);
insert into subactivity_lut values(30,'Annual Grass, Forb, or Noxious Weed Treatments',10);
insert into subactivity_lut values(31,'Area Closure (Area and/or Seasonal)',10);
insert into subactivity_lut values(32,'Fuels Management',10);
insert into subactivity_lut values(33,'Vegetation Management / Habitat Enhancement',10);
insert into subactivity_lut values(34,'Conservation Easement',11);
insert into subactivity_lut values(35,'Fuel Breaks',11);
insert into subactivity_lut values(36,'Land Acquisition',11);

alter table ced_main_subactivity rename to ced_main_subactivity_legacy;

create or replace view ced_main_subactivity AS
select distinct a.id, a.subactivity, b.activity, c.typeact
from subactivity_lut a, activity_lut b, typeact_lut c
where a.activity_id=b.id and b.typeact_id=c.id;

alter table ced_main_project_info add column subactivity_id integer;
alter table ced_main_project_info modify column subactivity varchar(200);
alter table ced_main_project_info add column seeding_type varchar(60);
alter table ced_main_project_info add column post_fire integer(1);

update ced_main_project_info set subactivity_id=0;

UPDATE ced_main_project_info a
INNER JOIN ced_main_subactivity b
ON a.activity=b.activity
AND a.subactivity=b.subactivity
SET a.subactivity_id = b.id;