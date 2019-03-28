alter table ced_main_project_info modify column post_fire varchar(50);

-- Change activity_plan_values to view
drop table if exists metric_lut;
drop table if exists subactivity_metric_lut;
drop table if exists ced_main_activity_plan_values;

create table subactivity_metric_lut(
id int(11) NOT NULL AUTO_INCREMENT,
subactivity_id int(11),
metric varchar(100),
PRIMARY KEY (`id`)
);

LOAD DATA LOCAL INFILE 'metric_lut.csv'
INTO TABLE subactivity_metric_lut
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n';

create or replace view ced_main_activity_plan_values as
select distinct a.id, b.Activity, c.SubActivity, a.Metric, d.typeact
from subactivity_metric_lut a, activity_lut b, subactivity_lut c, typeact_lut d
where c.activity_id=b.id and a.subactivity_id=c.id and b.typeact_id=d.id;

-- Create LUTs


CREATE OR REPLACE VIEW ced_main_metrics_view as
select distinct Project_ID, Metric_Value AS TotalAcres,
0 AS TotalMiles, Date_Created AS Date_Entered
from ced_main_project_info where Metric = 'Acres'
union
select distinct Project_ID,0 AS TotalAcres,
Metric_Value as TotalMiles, Date_Created as Date_Entered
from ced_main_project_info where Metric = 'Miles';

-- add values
insert into subactivity_lut values(38,'Noxious Weed Treatments',10);
insert into subactivity_lut values(39,'Riparian, Wet Meadow or Spring Restoration',10);
update subactivity_lut set subactivity='Area Closure' where id = 31;
update subactivity_lut set subactivity='Annual Grass Treatments' where id = 30;

update ced_main_project_info set subactivity_id=30
where subactivity like '%Annual Grass, Forb, or Noxious Weed Treatments%';

update ced_main_project_info set subactivity_id=37
where subactivity like '%Mine reclamation with goal of sage brush restoration%';

update ced_main_project_info set subactivity_id=37
where subactivity like '%Oil and gas reclamation with goal of sage brush restoration%';

update ced_main_project_info
set subactivity = 'Energy development reclamation with the goal of sagebrush restoration'
where subactivity_id=37;

update ced_main_project_info
set subactivity = 'Annual Grass Treatments'
where subactivity_id=30;

update ced_main_project_info
set subactivity = '--Select a SubActivity--'
where subactivity_id=1;

quit
