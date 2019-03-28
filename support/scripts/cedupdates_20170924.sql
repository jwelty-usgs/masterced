create or replace view ced_main_activity AS
select distinct a.id, a. activity, b.typeact,
  concat(a. activity, " (", b.typeact, ")") as Activity_Query_Label
from activity_lut a, typeact_lut b
where a.typeact_id=b.id;

create or replace view ced_main_subactivity AS
select distinct a.id, a.subactivity, b.activity, c.typeact,
  concat(a.subactivity, " (", b.activity, ")") as SubActivity_Query_Label
from subactivity_lut a, activity_lut b, typeact_lut c
where a.activity_id=b.id and b.typeact_id=c.id;

rename table ced_main_metrics to ced_main_metrics_fy17;

create table ced_main_metrics as
  select distinct Project_ID, TotalAcres, TotalMiles, Date_Entered, User
  from ced_main_metrics_fy17;

CREATE INDEX ced_main_metrics_indx ON ced_main_metrics(Project_ID);

update ced_main_metrics set TotalAcres=15 where Project_ID = 7542;